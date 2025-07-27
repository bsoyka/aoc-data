"""Real data to test your Advent of Code solutions."""

import json
from pathlib import Path
from typing import TypedDict, cast

from .errors import DataNotFoundError
from .models import AdventOfCodeData

__all__ = ['AdventOfCodeData']

_DATA_DIR = Path(__file__).parent / 'data'


class _AdventOfCodeDataDict(TypedDict):
    """Typed dictionary for raw Advent of Code data."""

    input: str
    part1: str
    part2: str


def _load_data_from_json(year: int, day: int) -> list[_AdventOfCodeDataDict]:
    """Load data from a JSON file for a specific year and day.

    Args:
        year: The year of the Advent of Code event.
        day: The day of the Advent of Code event.

    Returns:
        A list of dictionaries containing the input and expected outputs for the given
        year and day.

    Raises:
        DataNotFoundError: If the package does not contain data for the specified year
            and day.
    """
    file_path = _DATA_DIR / f'year{year}' / f'day{day:02}.json'
    if not file_path.exists():
        raise DataNotFoundError(year, day)

    with file_path.open(encoding='utf-8') as file:
        return cast('list[_AdventOfCodeDataDict]', json.load(file))


def get_aoc_data(year: int, day: int) -> list[AdventOfCodeData]:
    """Get Advent of Code data for a specific year and day.

    Args:
        year: The year of the Advent of Code event.
        day: The day of the Advent of Code event.

    Returns:
        A list of AdventOfCodeData objects containing the input and expected outputs
        for the given year and day.
    """
    raw_data = _load_data_from_json(year, day)
    return [
        AdventOfCodeData(
            year=year,
            day=day,
            input_=data['input'],
            part1=data['part1'],
            part2=data['part2'],
        )
        for data in raw_data
    ]
