import mysql.connector
import pandas as pd

# Update these with your MySQL credentials
MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "#Flyingsoul123"
DATABASE_NAME = "mortgage_db"
TABLE_NAME = "internal_loans"

# Load CSV
df = pd.read_csv("data/mortgage_loans_cleaned.csv")

# Connect to MySQL
conn = mysql.connector.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD
)
cursor = conn.cursor()

# Create database if not exists
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE_NAME}")
cursor.execute(f"USE {DATABASE_NAME}")

# Drop table if exists
cursor.execute(f"DROP TABLE IF EXISTS {TABLE_NAME}")

# Create table
cursor.execute(f"""
    CREATE TABLE {TABLE_NAME} (
        Loan_ID VARCHAR(10),
        Customer_Name VARCHAR(100),
        Loan_Amount INT,
        Interest_Rate FLOAT,
        Term_Years INT,
        Credit_Score INT,
        Loan_Status VARCHAR(20),
        Bank_Flag VARCHAR(20),
        High_Risk_Flag VARCHAR(10)
    )
""")

# Insert data
for _, row in df.iterrows():
    cursor.execute(f"""
        INSERT INTO {TABLE_NAME} VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s, %s
        )
    """, tuple(row))

conn.commit()
cursor.close()
conn.close()

print("✅ Data loaded into MySQL table:", TABLE_NAME)
