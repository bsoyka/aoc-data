"""Tests for the exceptions in aoc-data."""

from hypothesis import given
from hypothesis import strategies as st

from aoc_data.errors import DataNotFoundError


@given(
    year=st.integers(min_value=2015, max_value=2024),
    day=st.integers(min_value=1, max_value=25),
)
def test_data_not_found_error(year: int, day: int) -> None:
    """Test that the DataNotFoundError is raised with the correct message."""
    error = DataNotFoundError(year, day)
    assert error.year == year
    assert error.day == day
    assert str(error) == f'No data found for year {year}, day {day}.'
