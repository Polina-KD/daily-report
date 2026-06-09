import csv
import datetime

import logging

from report.exceptions import InvalidCsvError, MissingColumnError
from report.models import Order

logger = logging.getLogger(__name__)
logging.basicConfig(filename='report.log', )


def read_file(file_path) -> list[Order]:
    orders_list: list[Order] = []
    with open(str(file_path), 'r', encoding="utf-8") as file:
        reader = csv.DictReader(file)
        validate_required_columns(reader.fieldnames)
        for row in reader:
            orders_list.append(parse_order_row(row))
        return orders_list


def validate_required_columns(headers_list: list[str] | None) -> None:
    if headers_list is None:
        raise MissingColumnError("Here is no list of headers.")
    elif not headers_list:
        raise MissingColumnError("The list of headers is empty.")
    required_columns: list[str] = ['order_id',
                                   'date',
                                   'customer',
                                   'product',
                                   'category',
                                   'quantity',
                                   'price']
    for required_column in required_columns:
        if required_column not in headers_list:
            raise MissingColumnError(f'The column {required_column} is missed.')
    # for header in headers_list:
    #     if header not in required_columns:
    #         raise MissingColumnError(f'{header} is not a required column.')


def parse_order_row(row: dict[str, str]) -> Order:
    try:
        order = Order(order_id=int(row["order_id"]),
                      date=convert_str_to_date(row["date"]),
                      customer=row["customer"],
                      product=row["product"],
                      category=row["category"],
                      quantity=int(row["quantity"]),
                      price=parse_price(row["price"]))
        return order
    except ValueError:
        logger.error(f"{datetime.datetime.today()}:Invalid CSV format in {row}.")
        raise InvalidCsvError(f"Invalid CSV format in {row}.")

def convert_str_to_date(date: str) -> datetime.date:
    try:
        return datetime.datetime.strptime(date, "%d-%m-%Y").date()
    except ValueError:
        try:
            return datetime.datetime.strptime(date, "%Y-%m-%d").date()
        except ValueError:
            logger.error(f"{datetime.datetime.today()}:Invalid date format in {date}.")
            raise InvalidCsvError(f"Invalid date format in {date}.")


def parse_price(price: str) -> float:
    try:
        return float(price)
    except ValueError:
        logger.error(f"{datetime.datetime.today()}:Could not convert price {price} to float.")
        raise InvalidCsvError(f"Could not convert price {price} to float.")


# read_orders = read_file("D:/PyPrograms/orders.csv")
# print(read_orders)
