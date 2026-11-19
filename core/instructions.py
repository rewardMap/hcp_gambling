from rewardgym.render.routines.passive_routines import InstructionRoutine
from rewardgym.render.stimulus_definitions import TextDefinition, ImageDefinition, RectangleDefinition
from rewardgym.utils import NameCounter

import json
import pathlib

from rewardgym.render.stimuli import lose_cross, win_cross, zero_cross

instructions_path = (
    pathlib.Path(__file__).parent.resolve() / "assets" / "instructions_en.json"
)
instructions = json.loads(instructions_path.read_text())


def get_instructions(instructions=instructions):
    name = NameCounter()

    nothing = zero_cross(
        width=100, height=100, circle_radius_inner=10, circle_radius_outer=15
    )
    winning = win_cross(
        width=100, height=100, circle_radius_inner=10, circle_radius_outer=15
    )
    lose = lose_cross(
        width=100, height=100, circle_radius_inner=10, circle_radius_outer=15
    )

    part_0_0 = TextDefinition(
        name=name.name,
        text=instructions["0.0"],
        height=28,
        pos=(0, 250),
    )

    part_0_1 = TextDefinition(
        name=name.name,
        text=instructions["0.1"],
        height=28,
        pos=(0, -250),
    )

    quest = TextDefinition(
        name=name.name,
        text="?",
        color=[244, 244, 244],
        height=150,
    )

    aspect_ratio = 250 / 350

    card = RectangleDefinition(
        name=name.name,
        width=int(250 * aspect_ratio),
        height=250,
        fillColor="grey",
        lineWidth=3,
        lineColor="white",
    )

    part_0 = InstructionRoutine(
        name=name.name,
        stimulus_definitions=[card, quest, part_0_0, part_0_1]
    )

    start_pos = 280
    part_1_0 = TextDefinition(
        name=name.name,
        text=instructions["1.0"],
        height=28,
        pos=(0, start_pos),
    )

    start_pos -= 65

    part_1_1 = TextDefinition(
        name=name.name,
        text=instructions["1.1"],
        height=28,
        pos=(0, start_pos),
    )

    start_pos -= 75
    img2 = ImageDefinition(
        name=name.name, image=winning, pos=(0, start_pos), size=winning.shape[:2]
    )

    start_pos -= 85

    part_1_2 = TextDefinition(
        name=name.name,
        text=instructions["1.2"],
        height=28,
        pos=(0, start_pos),
    )

    start_pos -= 65
    img3 = ImageDefinition(name=name.name, image=lose, pos=(0, start_pos), size=lose.shape[:2])

    start_pos -= 85
    part_1_3 = TextDefinition(
        name=name.name,
        text=instructions["1.3"],
        height=28,
        pos=(0, start_pos),
    )

    start_pos -= 65
    img4 = ImageDefinition(
        name=name.name, image=nothing, pos=(0, start_pos), size=nothing.shape[:2]
    )

    part_1 = InstructionRoutine(
        name=name.name,
        stimulus_definitions=[part_1_0, part_1_1, part_1_2, part_1_3, img2, img3, img4]
    )

    part_2_0 = TextDefinition(
        name=name.name,
        text=instructions["2.0"],
        height=28,
        alignText="center",
    )

    part_2 = InstructionRoutine(
        name=name.name,
        stimulus_definitions=[part_2_0]
    )


    return [part_0, part_1, part_2], instructions
