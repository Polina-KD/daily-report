class InvalidCsvError(Exception):
    """
    Raised when the CSV contains invalid data.
    """
class InvalidPriceFormat(Exception):
    """
    Raised when the price format is invalid.
    """

class MissingHeaderError(Exception):
    """
    Raised when the CSV contains missing headers.
    """

class MissingColumnError(Exception):
    """
    Raised when a required CSV column is missing.
    """
