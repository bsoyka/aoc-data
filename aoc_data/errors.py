"""Exception classes for aoc-data."""


class AocDataError(Exception):
    """Base exception class for aoc-data errors."""


class DataNotFoundError(AocDataError):
    """Exception raised when data for a specific year and day is not found."""

    def __init__(self, year: int, day: int) -> None:
        """Initialize the DataNotFoundError with the year and day.

        Args:
            year: The year of the Advent of Code event.
            day: The day of the Advent of Code event.
        """
        message = f'No data found for year {year}, day {day}.'
        super().__init__(message)
        self.year = year
        self.day = day
