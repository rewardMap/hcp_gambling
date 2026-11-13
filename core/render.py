from rewardgym.render import ImageDefinition, RectangleDefinition, TextDefinition
from rewardgym.render.routines import (
    ConditionedTextCard,
    FeedBackRoutine,
    PresentationRoutine,
)
from rewardgym.render.routines import ActionRoutine
from rewardgym.stimuli import fixation_cross


def get_render_info(
    random_state=111,
    key_dict=None,
    external_stimuli=None,
    fullpoints=None,
    **kwargs,
):
    if key_dict is None:
        key_dict = {"left": 0, "right": 1}
    reward_feedback = FeedBackRoutine(
        duration=1.0, name="reward", bar_total=fullpoints, rl_label="reward"
    )

    base_stim_iti = PresentationRoutine(
        stimulus_definitions=[
            ImageDefinition(
                name="fixation",
                autoDraw=True,
                image=fixation_cross()
            )
        ],
        duration=1.5,
        name="iti",
        rl_label='obs'
    )

    wait_after_response = PresentationRoutine(
        stimulus_definitions=[
            ImageDefinition(
                name="fixation",
                autoDraw=True,
                image=fixation_cross()
            )
        ],
        duration=1.5,
        name="delay",
    )

    rectangle =                         RectangleDefinition(
                            name="rect",
                            autoDraw=False,
                            width=250,
                            height=350,
                            fillColor="grey",
                            lineColor="white",
                            lineWidth=3
                        )
    text = TextDefinition(
                        name="text",
                        autoDraw=False,
                        height=150,
                        text="?",
                        color="white")

    info_dict = {
        0: {
            "psychopy": [
                PresentationRoutine(
                    stimulus_definitions=[
                        rectangle, text],
                        name="cue",
                        duration=None,
                        rl_label="obs"
                    ),
                ActionRoutine(name="response", duration=1.5, key_dict=key_dict, rl_label="action", flip=False),
            ]
        },
        1: {
            "psychopy": [
                wait_after_response,
                ConditionedTextCard(
                    text_definition= text,
                    background_definition= rectangle,
                    condition_text={1: [1, 2, 3, 4], -0.5: [6, 7, 8, 9], 0: [5]},
                    name="selection",
                    duration=1.0,
                ),
                reward_feedback,
                base_stim_iti,
            ]
        },
        2: {
            "psychopy": [
                wait_after_response,
                ConditionedTextCard(
                    text_definition= text,
                    background_definition= rectangle,
                    condition_text={1: [1, 2, 3, 4], -0.5: [6, 7, 8, 9], 0: [5]},
                    name="selection",
                    duration=1.0,
                ),
                reward_feedback,
                base_stim_iti,
            ]
        },
    }

    return info_dict, None
