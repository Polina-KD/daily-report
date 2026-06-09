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

