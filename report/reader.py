import csv
import datetime
import logging
from typing import Sequence

# from report.cli import logger
from report.exceptions import InvalidCsvError, MissingColumnError
from report.models import Order

logger = logging.getLogger(__name__)


def read_file(file_path: str) -> list[Order]:
    orders_list: list[Order] = []
    logger.info("Reading CSV file...")
    with open(str(file_path), 'r', encoding="utf-8") as file:
        reader = csv.DictReader(file)
        validate_required_columns(reader.fieldnames)
        for row in reader:
            orders_list.append(parse_order_row(row))
    logger.info(f"Read orders from {file_path} successfully.")
    # print("Order list", orders_list)
    return orders_list


def validate_required_columns(headers_list: Sequence[str] | None) -> None:
    if headers_list is None or headers_list == []:
        raise MissingColumnError("CSV contains no headers at all. Or the list of headers is empty.")
    required_columns: list[str] = ['order_id',
                                   'date',
                                   'customer',
                                   'product',
                                   'category',
                                   'quantity',
                                   'price']
    for required_column in required_columns:
        if required_column not in headers_list:
            raise MissingColumnError(f"Missing required column {required_column} in CSV file.")
    # for header in headers_list:
    #     if header not in required_columns:
    #         raise MissingColumnError(f'{header} is not a required column.')


def is_row_broken(row: dict[str, str]) -> None:
    if not row:
        raise InvalidCsvError(f"Empty row: {row}")
    for key, value in row.items():
        if value is None or str(value).strip() == "":
            raise InvalidCsvError(f"Broken {key} in row: {row}")


def parse_order_row(row: dict[str, str]) -> Order:
    try:
        is_row_broken(row)
        order = Order(order_id=int(row["order_id"]),
                      date=convert_str_to_date(row["date"]),
                      customer=row["customer"],
                      product=row["product"],
                      category=row["category"],
                      quantity=int(row["quantity"]),
                      price=parse_price(row["price"]))
        return order
    except ValueError:
        raise InvalidCsvError(f"Invalid row {row}.")


def convert_str_to_date(date: str) -> datetime.date:
    try:
        return datetime.datetime.strptime(date, "%d-%m-%Y").date()
    except ValueError:
        try:
            return datetime.datetime.strptime(date, "%Y-%m-%d").date()
        except ValueError:
            raise InvalidCsvError(f"Invalid date format in {date}.")


def parse_price(price: str) -> float:
    try:
        return float(price)
    except ValueError:
        # logger.error(f"Could not convert price {price} to float.")
        raise InvalidCsvError(f"Invalid price format in {price}.")

# read_orders = read_file("D:/PyPrograms/order.csv")
# print(read_orders)
