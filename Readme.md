# 🏦 Mortgage Lending Data Quality System

A complete data analytics pipeline that simulates and analyzes mortgage loan data using Python, MySQL, and Tableau. This project mimics real-world data quality validation and reconciliation workflows used in financial institutions.

---

## 🚀 Features

✅ Simulate mortgage data with issues (missing values, duplicates, inconsistencies)  
✅ Clean and validate data using a Python ETL pipeline  
✅ Load data into MySQL tables for structured processing  
✅ Reconcile internal and external datasets using SQL queries  
✅ Optional: Visualize risk and approval insights in a Tableau dashboard  

---

### 🗃️ Project Structure

```
Mortgage_Lending_Quality_System/
├── data/                      # Raw and cleaned datasets (CSV)
├── scripts/                   # All Python scripts
│   ├── generate_loans.py
│   ├── etl_pipeline.py
│   ├── mysql_loader.py
│   ├── generate_external_loans.py
│   ├── load_external_loans.py
│   └── sql_reconciliation_queries.sql
├── tableau/                   # Tableau workbook (dashboard)
└── README.md
```



---

## 📊 Tableau Dashboard

📈 *Coming soon*  
(*Link will go here once dashboard is published to Tableau Public*)

---

## 🧰 Tech Stack

- **Python** (Pandas)
- **MySQL** (`mysql-connector-python`)
- **SQL** (Reconciliation queries)
- **Tableau Public** (Dashboard Visualization)
- Git & GitHub (Version control & publishing)

---

## 🧠 Concepts Applied

- Data Cleaning (ETL)
- Risk Scoring
- Relational Databases (RDBMS)
- SQL Joins and Data Reconciliation
- Data Visualization
- Business Rule Validation (Credit Score + Loan Amount logic)

---

## 📌 How to Run Locally

🧾 1. Clone the Repository
```
   git clone https://github.com/0-0ankit/mortgage-data-quality.git
   cd mortgage-data-quality

```

⚙️ 2. Run Scripts in Order

```
   python scripts/generate_loans.py
   python scripts/etl_pipeline.py
   python scripts/mysql_loader.py
   python scripts/generate_external_loans.py
   python scripts/load_external_loans.py

```

🧮 3. Run Reconciliation Queries in MySQL

Use this script inside your MySQL client:
```
   scripts/sql_reconciliation_queries.sql
```
## ✨ Author

**Ankit Yadav**  
📍 Bengaluru, India  
🔗 [LinkedIn Profile](https://www.linkedin.com/in/ankitcodes247/)  
💻 [GitHub Profile](https://github.com/0-0ankit)











