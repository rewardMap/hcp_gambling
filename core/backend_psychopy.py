try:
    from ....psychopy_render import (
        ImageStimulus,
        FeedBackStimulus,
        TextWithBorder,
        ActionStimulus,
    )

    from ....stimuli import fixation_cross

except ImportError:
    from rewardgym.psychopy_render import (
        ImageStimulus,
        FeedBackStimulus,
        TextWithBorder,
        ActionStimulus,
    )

    from rewardgym.stimuli import fixation_cross


def get_psychopy_info(
    seed=111,
    key_dict={"left": 0, "right": 1},
    external_stimuli=None,
    fullpoints=None,
    **kwargs,
):
    reward_feedback = FeedBackStimulus(
        1.0, text="{0}", target="reward", name="reward", bar_total=fullpoints, rl_label="reward"
    )

    base_stim_iti = ImageStimulus(
        image_paths=[fixation_cross()],
        duration=1.5,
        autodraw=True,
        name="iti",
    )

    wait_after_response = ImageStimulus(
        image_paths=[fixation_cross()],
        duration=1.5,
        autodraw=True,
        name="delay",
    )

    info_dict = {
        0: {
            "psychopy": [
                TextWithBorder(
                    "{0}",
                    {0: ["?"]},
                    name="cue",
                    duration=0.00,
                    rl_label="obs",
                ),
                ActionStimulus(duration=1.5, key_dict=key_dict, rl_label="action"),
            ]
        },
        1: {
            "psychopy": [
                wait_after_response,
                TextWithBorder(
                    "{0}",
                    condition_text={1: [1, 2, 3, 4], -0.5: [6, 7, 8, 9], 0: [5]},
                    name="selection",
                    rl_label="obs"
                ),
                reward_feedback,
                base_stim_iti,
            ]
        },
        2: {
            "psychopy": [
                wait_after_response,
                TextWithBorder(
                    "{0}",
                    condition_text={-0.5: [1, 2, 3, 4], 1: [6, 7, 8, 9], 0: [5]},
                    name="selection",
                    rl_label="obs"
                ),
                reward_feedback,
                base_stim_iti,
            ]
        },
    }

    return info_dict, None
