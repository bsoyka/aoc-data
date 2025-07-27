"""Real data to test your Advent of Code solutions."""

from dataclasses import dataclass


@dataclass
class AdventOfCodeData:
    """A single chunk of Advent of Code data, usable for a test case.

    This is the equivalent of one person's input and expected outputs for a given day's
    puzzles.

    Attributes:
        year: The year of the Advent of Code event.
        day: The day of the Advent of Code event.
        input_: The input data for the puzzle.
        part1: The expected output for the first part of the puzzle.
        part2: The expected output for the second part of the puzzle.
    """

    year: int
    day: int
    input_: str
    part1: str
    part2: str
