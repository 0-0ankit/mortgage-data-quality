import pandas as pd
import random
import numpy as np
import os

# Set seed
random.seed(42)
np.random.seed(42)

names = ['Rahul Sharma', 'Meera Gupta', 'Amit Singh', 'Priya Das', 'Ravi Mehta',
         'Sneha Jain', 'Arjun Verma', 'Nikita Roy', 'Karan Joshi', 'Divya Nair']

def generate_loan_data(n=200):
    data = []
    for i in range(1, n + 1):
        loan_id = f"L{i:04d}"
        name = random.choice(names)
        amount = random.randint(100000, 2000000)
        interest_rate = round(random.uniform(7.0, 12.5), 2)
        term = random.choice([10, 15, 20, 25, 30])
        credit_score = random.randint(550, 800)
        status = 'Approved' if credit_score >= 700 and amount <= 1000000 else 'Rejected'
        bank_flag = random.choice(['Internal', 'External'])

        if random.random() < 0.05:
            interest_rate = None
        if random.random() < 0.05:
            credit_score = None
        if random.random() < 0.03:
            loan_id = f"L{random.randint(1, n):04d}"

        data.append([loan_id, name, amount, interest_rate, term, credit_score, status, bank_flag])
    
    df = pd.DataFrame(data, columns=[
        'Loan_ID', 'Customer_Name', 'Loan_Amount', 'Interest_Rate',
        'Term_Years', 'Credit_Score', 'Loan_Status', 'Bank_Flag'
    ])
    return df

if __name__ == "__main__":
    df = generate_loan_data()
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/mortgage_loans_raw.csv", index=False)
    print("✅ Generated: mortgage_loans_raw.csv")
