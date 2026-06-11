from report.models import Order
from report.report import calculate_top_n


def test_calculate_top_n(valid_orders: list[Order]) -> None:
    result = calculate_top_n(valid_orders, "customer", 5)

    assert result == [
        ("Sanne de Vries", 15273.44),
        ("Jan de Jong", 4540.65),
        ("Pieter van der Berg", 3643.4),
        ("Willem van Dijk", 1958.0),
        ("Emma van der Meer", 1954.92),
    ]


def test_revenue_per_category(valid_orders: list[Order]) -> None:
    result = calculate_top_n(valid_orders, "category", len(valid_orders))

    assert result == [
        ("Laptop", 10794.85),
        ("Smartphone", 6414.4),
        ("Tablet", 4762.4),
        ("E-Reader", 2879.84),
        ("Smartwatch", 2518.92),
    ]
