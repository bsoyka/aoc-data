"""Tests for the AdventOfCodeData class."""

from hypothesis import given
from hypothesis import strategies as st

from aoc_data import AdventOfCodeData


@given(
    year=st.integers(min_value=2015, max_value=2024),
    day=st.integers(min_value=1, max_value=25),
    input_=st.text(),
    part1=st.text(),
    part2=st.text(),
)
def test_advent_of_code_data_init(
    year: int, day: int, input_: str, part1: str, part2: str
) -> None:
    """Test the initialization of the AdventOfCodeData class."""
    data = AdventOfCodeData(
        year=year,
        day=day,
        input_=input_,
        part1=part1,
        part2=part2,
    )

    assert data.year == year
    assert data.day == day
    assert data.input_ == input_
    assert data.part1 == part1
    assert data.part2 == part2
