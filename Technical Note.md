# Technical Note — Brightstone Logistics Report Generator

## 🧱 Architecture

The application is split into the following modules:

- **cli.py** — command-line interface, argument parsing, error handling
- **reader.py** — CSV reading and validation
- **report.py** — business logic and calculations
- **writer.py** — output generation (JSON and Markdown)
- **models.py** — data structures (`Order`, `ReportResult`)
- **exceptions.py** — custom exception classes for error handling

This separation follows a simple layered architecture:
input → processing → output.

---

## 📊 Data model

The core entity is the `Order` object.

Each order contains:
- order_id
- date
- customer
- product
- category
- quantity
- price

The report is represented by the `ReportResult` class, which aggregates:
- report date
- total orders
- total revenue
- top customers
- top products
- revenue by category

---

## 🔄 Data flow

1. The CLI orchestrates the application flow and parses command-line arguments using argparse
2. The CSV file is read and validated, and raw data is converted into `Order` objects
3. Business logic processes the list of orders
4. A `ReportResult` object is created containing aggregated metrics (totals, top customers/products, revenue per category)
5. The output is written in the selected format (JSON or Markdown)

---

## ⚠️ Error handling

The application uses custom exceptions:

- `InvalidCsvError` — invalid data format
- `MissingColumnError` — required column is missing
- `UnsupportedFileFormat` — unsupported output format

All errors are:
- logged using the `logging` module
- handled in the CLI layer
- mapped to exit codes:
  - 0 → success
  - 1 → input/data error
  - 2 → system/configuration error

---

## 🧠 Design decisions

- Separated CLI from business logic to improve testability
- Used dataclasses (`Order`, `ReportResult`) for clean data handling
- Centralized calculations in `report.py` to avoid duplication
- Supported two output formats using a shared reporting layer

---

## ⚖️ Trade-offs

- Combined multiple aggregations (top-N and revenue per category) into a single function to reduce complexity
- Used standard library only to keep the project lightweight and portable
- Used a simple CLI implementation based on argparse to keep the project lightweight and easy to maintain.

---

## 📌 Summary

The project is designed to be simple, testable, and easy to extend.
Each module has a clear responsibility, and the system can be extended with new output formats or data sources without changing core logic.