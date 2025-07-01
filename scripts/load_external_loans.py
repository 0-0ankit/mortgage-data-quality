import mysql.connector
import pandas as pd

MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "#Flyingsoul123"  # Update with your MySQL password
DATABASE_NAME = "mortgage_db"
TABLE_NAME = "external_loans"

df = pd.read_csv("data/mortgage_loans_external.csv")

conn = mysql.connector.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    database=DATABASE_NAME
)
cursor = conn.cursor()

cursor.execute(f"DROP TABLE IF EXISTS {TABLE_NAME}")
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

for _, row in df.iterrows():
    cursor.execute(f"""
        INSERT INTO {TABLE_NAME} VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s, %s
        )
    """, tuple(row))

conn.commit()
cursor.close()
conn.close()

print("✅ External data loaded into MySQL table: external_loans")
