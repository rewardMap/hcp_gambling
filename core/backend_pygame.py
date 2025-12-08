from rewardgym.pygame_render import (
    BaseText,
    BaseDisplay,
    BaseAction,
    FormatText,
    feedback_block,
)


def get_pygame_info(action_map, window_size=256):
    base_position = (window_size // 2, window_size // 2)

    left_text = {1: [5], 2: [1, 2, 3, 4], 0: [6, 7, 8, 9]}
    right_text = {1: [5], 0: [1, 2, 3, 4], 2: [6, 7, 8, 9]}

    reward_disp, earnings_text = feedback_block(base_position)

    pygame_dict = {
        0: {
            "pygame": [
                BaseDisplay(None, 1),
                BaseText("+", 1000, textposition=base_position),
                BaseDisplay(None, 1),
                BaseText("< or >", 500, textposition=base_position),
                BaseAction(),
            ]
        },
        1: {
            "pygame": [
                BaseDisplay(None, 1),
                BaseText("<", 1000, textposition=base_position),
                FormatText(
                    "Card: {0}",
                    1000,
                    condition_text=left_text,
                    textposition=base_position,
                ),
                reward_disp,
                earnings_text,
            ]
        },
        2: {
            "pygame": [
                BaseDisplay(None, 1),
                BaseText(">", 1000, textposition=base_position),
                FormatText(
                    "Card: {0}",
                    1000,
                    condition_text=right_text,
                    textposition=base_position,
                ),
                reward_disp,
                earnings_text,
            ]
        },
    }

    return pygame_dict
