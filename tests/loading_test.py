"""Tests for JSON loading functionality."""

from aoc_data import _load_data_from_json


def test_load_data_from_json() -> None:
    """Test loading data from a JSON file."""
    year = 2024
    day = 1
    data = _load_data_from_json(year, day)

    assert isinstance(data, list)
    assert len(data) > 0
    assert 'input' in data[0]
    assert 'part1' in data[0]
    assert 'part2' in data[0]
