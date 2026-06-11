# Brightstone Logistics Report Generator

A command-line tool that processes daily CSV exports from a legacy WMS system and generates a
structured business report.

The tool helps automate reporting so users do not need to open Excel manually.

---

## 📊 What the tool does

From a CSV file with orders, it generates:

- total number of orders
- total revenue
- top 5 products by revenue
- top 5 customers by total spend
- revenue per category

---

## 🚀 Installation

Clone the repository and install the project in editable mode:

```bash
git clone <repo-url>
cd daily-report
pip install -e .
```

---

## ▶️ How to run

```bash id="rd2"
python -m report --input orders.csv --output report.md --format markdown
```

---

## ⚙️ Arguments

- `--input`: path to input CSV file
- `--output`: path to output file
- `--format`: output format (`json` or `markdown`)

## 📦 Output formats

### Markdown

Human-readable report for sharing.

### JSON

Structured data for further processing.

Both formats use the same internal report logic.

---

## 🧪 Running tests

```bash
pytest --cov=report
```