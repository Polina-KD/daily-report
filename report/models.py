from dataclasses import dataclass
import datetime


@dataclass
class Order:
    """
    Represents a single order from WMS export CSV file.

    Attributes:
        order_id: Unique order ID.
        date: Date when the order was placed.
        customer: Customer full name.
        product: Name of the product ordered.
        category: Product category.
        quantity: Numbers of items ordered.
        price: Price per single product.
    """

    order_id: int
    date: datetime.date
    customer: str
    product: str
    category: str
    quantity: int
    price: float


@dataclass
class ReportResult:
    """
    Represents a result from WMS export CSV file.

    Attributes:
        report_date: Date string for the report.
        total_orders: Total number of orders.
        total_revenue: Total revenue of orders.
        top_products: Top 5 products by revenue.
        top_customers: Top 5 customers by total spend.
        revenue_by_category: Revenue per category sorted from high to low.
    """

    report_date: str
    total_orders: int
    total_revenue: float
    top_products: list[tuple[str, float]]
    top_customers: list[tuple[str, float]]
    revenue_by_category: list[tuple[str, float]]
