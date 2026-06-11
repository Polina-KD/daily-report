import pytest

from report.models import Order
from report.reader import read_file
from report.exceptions import MissingColumnError, InvalidCsvError


def test_valid_csv(valid_orders: list[Order]) -> None:
    file_path = "tests/data/valid_orders.csv"
    result = read_file(file_path)
    assert result == valid_orders


def test_invalid_csv() -> None:
    file_path = "tests/data/invalid_orders.csv"
    with pytest.raises(InvalidCsvError):
        read_file(file_path)


def test_empty_csv() -> None:
    file_path = "tests/data/empty_orders.csv"
    with pytest.raises(MissingColumnError):
        read_file(file_path)


def test_csv_with_missing_column() -> None:
    file_path = "tests/data/missing_column_orders.csv"
    with pytest.raises(MissingColumnError):
        read_file(file_path)


def test_csv_with_broken_row() -> None:
    file_path = "tests/data/broken_row.csv"
    with pytest.raises(InvalidCsvError):
        read_file(file_path)
