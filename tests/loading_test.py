"""Tests for JSON loading functionality."""

from datetime import datetime, timezone

import pytest
from hypothesis import assume, given
from hypothesis import strategies as st

from aoc_data import _load_data_from_json
from aoc_data.errors import DataNotFoundError

current_year = datetime.now(tz=timezone.utc).year


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


@given(year=st.integers(), day=st.integers(min_value=1, max_value=25))
def test_load_data_from_nonexistent_years(year: int, day: int) -> None:
    """Test loading data from an impossible year."""
    assume(year < 2015 or year > current_year)

    with pytest.raises(DataNotFoundError):
        _load_data_from_json(year, day)


@given(year=st.integers(min_value=2015, max_value=current_year), day=st.integers())
def test_load_data_from_nonexistent_days(year: int, day: int) -> None:
    """Test loading data from an impossible day."""
    assume(day < 1 or day > 25)

    with pytest.raises(DataNotFoundError):
        _load_data_from_json(year, day)
