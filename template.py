import os
import pathlib

from parse import parse


def parse_input(raw_input):
    def parse_line(line):
        pass

    pass


def solve(puzzle_input):
    def solve_line(line):
        pass

    pass


def main():
    path = pathlib.Path(os.path.dirname(os.path.abspath(__file__)))

    with (path / 'day-xx.input').open() as f:
        puzzle_input = f.readlines()

    puzzle_input = parse_input(puzzle_input)

    solve(puzzle_input)


if __name__ == "__main__":
    main()
