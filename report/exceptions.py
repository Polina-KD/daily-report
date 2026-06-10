class InvalidCsvError(Exception):
    """
    Raised when the CSV contains invalid data.
    """


class MissingColumnError(Exception):
    """
    Raised when a required CSV column is missing.
    """


class UnsupportedFileFormat(Exception):
    """
    Raised when requested file format is not supported.
    """
