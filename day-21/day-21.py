import os
from typing import Tuple


class DeterministicDice:
    def __init__(self) -> None:
        self.counter = 0

    def roll(self) -> int:
        number = 1 + (self.counter % 100)
        self.counter += 1
        return number

    def get_roll_count(self) -> int:
        return self.counter


def read_input_from_file(file_name: str) -> list:
    script_path = os.path.dirname(os.path.abspath(__file__))
    input_file = open(f"{script_path}/{file_name}", "r")
    data = input_file.readlines()
    data = [x.strip() for x in data]
    input_file.close()
    return data


def move_player(position: int, points: int, dice: DeterministicDice) -> Tuple[int, int]:
    for _ in range(3):
        position += dice.roll()
    while position > 10:
        position -= 10
    points += position
    return (position, points)


def get_starting_positions(data: list) -> Tuple[int, int]:
    a = int(data[0].split(": ")[1])
    b = int(data[1].split(": ")[1])
    return (a, b)


def part_1(data):
    position_a, position_b = get_starting_positions(data)
    points_a, points_b = 0, 0
    dice = DeterministicDice()
    while True:
        position_a, points_a = move_player(position_a, points_a, dice)
        if points_a >= 1000:
            return points_b * dice.get_roll_count()
        position_b, points_b = move_player(position_b, points_b, dice)
        if points_b >= 1000:
            return points_a * dice.get_roll_count()


def main() -> None:
    data = read_input_from_file("input.txt")

    result_1 = part_1(data)
    print(f"Part 1: {result_1}")


if __name__ == "__main__":
    main()
