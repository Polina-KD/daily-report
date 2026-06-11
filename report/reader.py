import csv
import datetime
import logging
from typing import Sequence

from report.exceptions import MissingColumnError, InvalidCsvError
from report.models import Order

logger = logging.getLogger(__name__)


def read_file(file_path: str) -> list[Order]:
    """
    Read CSV file and return a list of Order objects.

    :param file_path: path to CSV file

    :return: list of Order objects
    """
    orders_list: list[Order] = []
    logger.info("Reading CSV file...")
    with open(str(file_path), "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        validate_required_columns(reader.fieldnames)
        for row in reader:
            orders_list.append(parse_order_row(row))
    logger.info(f"Read orders from {file_path} successfully.")
    # print("Order list", orders_list)
    return orders_list


def validate_required_columns(headers_list: Sequence[str] | None) -> None:
    """
    Validate required columns in CSV file.

    :param headers_list: headers to validate

    :return: None

    :raise: MissingColumnError: if the required columns are missing or headers list is empty.
    """
    if headers_list is None or headers_list == []:
        raise MissingColumnError("CSV contains no headers at all. Or the list of headers is empty.")
    required_columns: list[str] = [
        "order_id",
        "date",
        "customer",
        "product",
        "category",
        "quantity",
        "price",
    ]
    for required_column in required_columns:
        if required_column not in headers_list:
            raise MissingColumnError(f"Missing required column {required_column} in CSV file.")
    # for header in headers_list:
    #     if header not in required_columns:
    #         raise MissingColumnError(f'{header} is not a required column.')


def is_row_broken(row: dict[str, str]) -> None:
    """
    Check if a row is broken.

    :param row: row of DictReader object

    :return: None

    :raise: InvalidCsvError: if the row is empty or malformed.
    """
    if not row:
        raise InvalidCsvError(f"Empty row: {row}")
    for key, value in row.items():
        if value is None or str(value).strip() == "":
            raise InvalidCsvError(f"Broken {key} in row: {row}")


def parse_order_row(row: dict[str, str]) -> Order:
    """
    Convert a row of DictReader object into an Order object.

    :param row: row of DictReader object

    :return: Order object

    :raise: InvalidCsvError: if the row contains invalid values.
    """
    try:
        is_row_broken(row)
        order = Order(
            order_id=int(row["order_id"]),
            order_date=convert_str_to_date(row["date"]),
            customer=row["customer"],
            product=row["product"],
            category=row["category"],
            quantity=int(row["quantity"]),
            price=parse_price(row["price"]),
        )
        return order
    except ValueError:
        raise InvalidCsvError(f"Invalid row {row}.")


def convert_str_to_date(date: str) -> datetime.date:
    """
    Convert a date string into datetime.date object.

    :param date: string to convert to datetime.date object

    :return: datetime.date object

    :raise: InvalidCsvError: if the date is malformed.
    """
    try:
        return datetime.datetime.strptime(date, "%d-%m-%Y").date()
    except ValueError:
        try:
            return datetime.datetime.strptime(date, "%Y-%m-%d").date()
        except ValueError:
            raise InvalidCsvError(f"Invalid date format in {date}.")


def parse_price(price: str) -> float:
    """
    Convert a price string into float.

    :param price: price string

    :return: float price

    :raise: InvalidCsvError: if the price string is malformed.
    """
    try:
        return float(price)
    except ValueError:
        # logger.error(f"Could not convert price {price} to float.")
        raise InvalidCsvError(f"Invalid price format in {price}.")


