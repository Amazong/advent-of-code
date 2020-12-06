import os
import pathlib


def parse_input(raw_input):
    return set([int(i) for i in raw_input])


def solve(puzzle_input):
    for i in puzzle_input:
        if 2020 - i in puzzle_input:
            print(i * (2020 - i))
            return

    print("Not found!")


def main():
    path = pathlib.Path(os.path.dirname(os.path.abspath(__file__)))

    with (path / 'day-01.input').open() as f:
        puzzle_input = f.readlines()

    puzzle_input = parse_input(puzzle_input)

    solve(puzzle_input)


if __name__ == "__main__":
    main()
