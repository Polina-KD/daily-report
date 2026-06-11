import logging

from report.models import ReportResult, Order

logger = logging.getLogger(__name__)


def create_report(orders: list[Order]) -> ReportResult:
    """
    Creates a report in the given list of read CSV file.

    :param orders: list of read CSV file.

    :return: report result object.
    """
    logger.info("Creating report...")
    return ReportResult(
        report_date=str(orders[0].date),
        total_orders=calculate_total_number_of_orders(orders),
        total_revenue=calculate_total_revenue(orders),
        top_products=calculate_top_n(orders, "product", 5),
        top_customers=calculate_top_n(orders, "customer", 5),
        revenue_by_category=calculate_top_n(orders, "category", len(orders)),
    )


def calculate_total_number_of_orders(orders: list[Order]) -> int:
    """
    Returns the total number of orders.

    :param orders: list of orders.

    :return: total number of orders.
    """
    return len(orders)


def calculate_total_revenue(orders: list[Order]) -> float:
    """
    Returns the total revenue.

    :param orders: list of orders.

    :return: total revenue.
    """
    revenue = 0.0
    for order in orders:
        revenue += order.price * order.quantity
    return revenue


def calculate_top_n(orders: list[Order], key_field: str, n: int) -> list[tuple[str, float]]:
    """
    Returns the top n aggregated values for the specified field.

    :param orders: list of orders.
    :param key_field: universal key for aggregation.
    :param n: number of products to return.

    :return: list of top n products by revenue.
    """
    list_of_pairs = []
    for order in orders:
        revenue = order.quantity * order.price
        list_of_pairs.append((getattr(order, key_field), revenue))
    aggregated_list = aggregate_by_key(list_of_pairs)
    sorted_list = sort_top(aggregated_list)
    if len(sorted_list) <= n:
        return sorted_list
    else:
        return sorted_list[:n]


def sort_top(list_with_tuples: list[tuple[str, float]]) -> list[tuple[str, float]]:
    """
    Sorts the list of tuples by revenue.

    :param list_with_tuples: list of tuples.

    :return: sorted list of top elements by revenue.
    """
    return sorted(list_with_tuples, key=lambda list_element: list_element[1], reverse=True)


def aggregate_by_key(non_unique_list: list[tuple[str, float]]) -> list[tuple[str, float]]:
    """
    Aggregates the list of non-unique tuples by revenue.

    :param non_unique_list: list of tuples which may contain duplicate entries.

    :return: list which can't contain duplicate entries.
    """
    uniq_dict: dict[str, float] = {}
    for key, value in non_unique_list:
        if key not in uniq_dict:
            uniq_dict[key] = value
        else:
            uniq_dict[key] += value
        uniq_dict[key] = round(uniq_dict[key], 2)
    uniq_list = list(uniq_dict.items())
    return uniq_list


