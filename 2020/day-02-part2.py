import os
import pathlib

from parse import parse


def parse_input(raw_input):
    def parse_line(line):
        p = parse("{}-{} {}: {}", line)

        return [int(p[0]), int(p[1]), p[2], p[3]]

    return [parse_line(line) for line in raw_input]


def solve(puzzle_input):
    def solve_line(line):
        return (line[3][line[0] - 1] == line[2]) ^ (line[3][line[1] - 1]
                                                    == line[2])

    print(sum([solve_line(line) for line in puzzle_input]))


def main():
    path = pathlib.Path(os.path.dirname(os.path.abspath(__file__)))

    with (path / 'day-02.input').open() as f:
        puzzle_input = f.readlines()

    puzzle_input = parse_input(puzzle_input)

    solve(puzzle_input)


if __name__ == "__main__":
    main()
