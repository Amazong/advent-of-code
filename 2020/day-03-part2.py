import math
import os
import pathlib
from functools import reduce

from parse import parse


def parse_input(raw_input):
    def parse_line(line):
        return line[:-1]

    return [parse_line(line) for line in raw_input]


def solve(puzzle_input, slopeX, slopeY):
    def solve_line(line):
        pass

    def get_tree_or_snow(x, y):
        return puzzle_input[y][x % len(puzzle_input[0])]

    ys = list(range(0, len(puzzle_input), slopeY))
    max_x = slopeX * len(ys)
    xs = list(range(0, max_x, slopeX))  #[y * slopeX for y in ys]
    my_sled_path = [get_tree_or_snow(x, y) for x, y in zip(xs, ys)]

    return sum([1 for point in my_sled_path if point == '#'])


def main():
    path = pathlib.Path(os.path.dirname(os.path.abspath(__file__)))

    with (path / 'day-03.input').open() as f:
        # with (path / 'day-03_sample.input').open() as f:
        puzzle_input = f.readlines()

    puzzle_input = parse_input(puzzle_input)

    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    sols = [solve(puzzle_input, slope[0], slope[1]) for slope in slopes]
    sol = reduce(lambda x, y: x * y, sols)

    print(sol)


if __name__ == "__main__":
    main()
