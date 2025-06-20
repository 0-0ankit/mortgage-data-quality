import pandas as pd
import os

# Paths
input_path = "data/mortgage_loans_raw.csv"
output_path = "data/mortgage_loans_cleaned.csv"

# Load dataset
df = pd.read_csv(input_path)

# Remove duplicate Loan_IDs (keep first)
df = df.drop_duplicates(subset='Loan_ID', keep='first')

# Drop rows with missing Interest Rate or Credit Score
df = df.dropna(subset=['Interest_Rate', 'Credit_Score'])

# Ensure Interest Rate is float
df['Interest_Rate'] = pd.to_numeric(df['Interest_Rate'], errors='coerce')

# Add High Risk Flag (Credit Score < 650 or Loan Amount > ₹15L)
df['High_Risk_Flag'] = df.apply(
    lambda row: 'Yes' if row['Credit_Score'] < 650 or row['Loan_Amount'] > 1500000 else 'No',
    axis=1
)

# Save cleaned data
df.to_csv(output_path, index=False)
print("✅ Cleaned dataset saved to:", output_path)
