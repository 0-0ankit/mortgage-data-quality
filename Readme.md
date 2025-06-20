# Mortgage Lending Data Quality System

A full-stack Python + SQL + Tableau pipeline to simulate mortgage data, clean it via ETL, reconcile it, and visualize risk & approval patterns.

## Structure
- `scripts/`: All ETL and SQL logic
- `data/`: Input/output datasets
- `tableau/`: Tableau dashboards

## Technologies
Python, Pandas, MySQL, Tableau

## To Run
1. Generate raw data:
   ```bash
   python scripts/generate_loans.py
