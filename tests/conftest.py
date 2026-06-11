import datetime

import pytest
from report.models import Order, ReportResult


@pytest.fixture
def valid_orders() -> list[Order]:
    return [
        Order(
            order_id=1,
            date=datetime.date(2026, 6, 8),
            customer="Jan de Jong",
            product="Samsung Galaxy S24",
            category="Smartphone",
            quantity=2,
            price=620.4,
        ),
        Order(
            order_id=2,
            date=datetime.date(2026, 6, 8),
            customer="Willem van Dijk",
            product="Apple iPad Pro",
            category="Tablet",
            quantity=1,
            price=1119.0,
        ),
        Order(
            order_id=3,
            date=datetime.date(2026, 6, 8),
            customer="Sanne de Vries",
            product="Apple MacBook Air",
            category="Laptop",
            quantity=5,
            price=1499.0,
        ),
        Order(
            order_id=4,
            date=datetime.date(2026, 6, 8),
            customer="Emma van der Meer",
            product="Samsung Galaxy Watch 6",
            category="Smartwatch",
            quantity=8,
            price=209.99,
        ),
        Order(
            order_id=5,
            date=datetime.date(2026, 6, 8),
            customer="Willem van Dijk",
            product="Apple Watch Series 9",
            category="Smartwatch",
            quantity=2,
            price=419.5,
        ),
        Order(
            order_id=6,
            date=datetime.date(2026, 6, 8),
            customer="Pieter van der Berg",
            product="Samsung Galaxy Tab S9",
            category="Tablet",
            quantity=10,
            price=364.34,
        ),
        Order(
            order_id=7,
            date=datetime.date(2026, 6, 8),
            customer="Jan de Jong",
            product="Dell XPS 15",
            category="Laptop",
            quantity=3,
            price=1099.95,
        ),
        Order(
            order_id=8,
            date=datetime.date(2026, 6, 8),
            customer="Emma van der Meer",
            product="Samsung Galaxy S24",
            category="Smartphone",
            quantity=1,
            price=275.0,
        ),
        Order(
            order_id=9,
            date=datetime.date(2026, 6, 8),
            customer="Sanne de Vries",
            product="Amazon Kindle Paperwhite",
            category="E-Reader",
            quantity=16,
            price=179.99,
        ),
        Order(
            order_id=10,
            date=datetime.date(2026, 6, 8),
            customer="Sanne de Vries",
            product="Samsung Galaxy S24",
            category="Smartphone",
            quantity=7,
            price=699.8,
        ),
    ]


@pytest.fixture
def invalid_file_format() -> str:
    return "pdf"


@pytest.fixture
def valid_report_results() -> ReportResult:
    return ReportResult(
        total_orders=10,
        total_revenue=27370.41,
        top_products=[
            ("Apple MacBook Air", 7495.0),
            ("Samsung Galaxy S24", 6414.4),
            ("Samsung Galaxy Tab S9", 3643.4),
            ("Dell XPS 15", 3299.85),
            ("Amazon Kindle Paperwhite", 2879.84),
        ],
        top_customers=[
            ("Sanne de Vries", 15273.44),
            ("Jan de Jong", 4540.65),
            ("Pieter van der Berg", 3643.4),
            ("Willem van Dijk", 1958.0),
            ("Emma van der Meer", 1954.92),
        ],
        revenue_by_category=[
            ("Laptop", 10794.85),
            ("Smartphone", 6414.4),
            ("Tablet", 4762.4),
            ("E-Reader", 2879.84),
            ("Smartwatch", 2518.92),
        ],
    )


@pytest.fixture
def valid_json_report() -> dict[str, int | float | list[list[str | float]]]:
    return {
        "total_orders": 10,
        "total_revenue": 27370.41,
        "top_products": [
            ["Apple MacBook Air", 7495.0],
            ["Samsung Galaxy S24", 6414.4],
            ["Samsung Galaxy Tab S9", 3643.4],
            ["Dell XPS 15", 3299.85],
            ["Amazon Kindle Paperwhite", 2879.84],
        ],
        "top_customers": [
            ["Sanne de Vries", 15273.44],
            ["Jan de Jong", 4540.65],
            ["Pieter van der Berg", 3643.4],
            ["Willem van Dijk", 1958.0],
            ["Emma van der Meer", 1954.92],
        ],
        "revenue_by_category": [
            ["Laptop", 10794.85],
            ["Smartphone", 6414.4],
            ["Tablet", 4762.4],
            ["E-Reader", 2879.84],
            ["Smartwatch", 2518.92],
        ],
    }


@pytest.fixture
def valid_report_markdown() -> str:
    file_path = "tests/data/valid_report.md"
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    return content
