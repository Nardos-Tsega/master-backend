# Expense Tracker CLI

A tiny command-line app to track personal expenses. Built with a clean, layered design (Model → Repository → Service → CLI) and **stdlib-only** (no external deps). Data is stored as JSON.

---

## Features

- Add an expense (description, amount)
- List all expenses
- Summarize total spend (optionally by month)
- Delete by ID
- Export all data to CSV

By default, data is saved to `~/.expense_tracker/db.json`.

---

## Quick Start

```bash
# 1) Clone
git clone <your-repo-url>
cd expense_tracker

# 2) (Optional) Create & activate a venv
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 3) Run the CLI
python3 main.py --help
```
