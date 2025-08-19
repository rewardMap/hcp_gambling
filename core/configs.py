try:
    from rewardgym.utils import check_random_state
except ImportError:
    from ....utils import check_random_state


def get_configs(stimulus_set: str = "1"):
    seed = check_random_state(int(stimulus_set))
    condition_dict = {
        "win": {"reward": 1},
        "lose": {"reward": -0.5},
        "neutral": {"reward": 0},
    }
    # 0 = loss, 1, = neutral, 2= win 1
    lose1 = ["lose", "lose", "lose", "lose", "lose", "lose", "neutral", "neutral"]
    lose2 = ["lose", "lose", "lose", "lose", "lose", "lose", "win", "win"]
    lose3 = ["lose", "lose", "lose", "lose", "lose", "lose", "neutral", "win"]

    win1 = ["win", "win", "win", "win", "win", "win", "neutral", "neutral"]
    win2 = ["win", "win", "win", "win", "win", "win", "lose", "lose"]
    win3 = ["win", "win", "win", "win", "win", "win", "neutral", "lose"]

    block_order_win = (
        seed.permutation([win1, win2, win3]).tolist()
        + seed.choice([win1, win2, win3], size=1, replace=True).tolist()
    )

    block_order_lose = (
        seed.permutation([lose1, lose2, lose3]).tolist()
        + seed.choice([lose1, lose2, lose3], size=1, replace=False).tolist()
    )

    block_order1 = seed.permutation(block_order_win[:2] + block_order_lose[:2]).tolist()
    block_order2 = seed.permutation(block_order_win[2:] + block_order_lose[2:]).tolist()

    conditions = []
    for block in block_order1 + block_order2:
        conditions.extend(seed.choice(block, size=8, replace=False).tolist())

    config = {
        "name": "hcp",
        "stimulus_set": stimulus_set,
        "isi": [],
        "delay": [0.0] * len(conditions),
        "condition": conditions,
        "condition_dict": condition_dict,
        "ntrials": len(conditions),
        "update": ["delay"],
        "add_remainder": False,
        "breakpoints": [7, 15, 23, 31, 39, 47, 56],
        "break_duration": 15,
    }
    return config
