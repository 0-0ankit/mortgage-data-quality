import pandas as pd
import random

# Load the internal cleaned dataset
df_internal = pd.read_csv("data/mortgage_loans_cleaned.csv")

# Introduce mismatches in 10 random rows
df_external = df_internal.copy()
mismatch_rows = df_external.sample(10, random_state=42).index
df_external.loc[mismatch_rows, 'Loan_Amount'] *= 1.05  # 5% inflation

# Drop 5 rows to simulate missing records
drop_rows = df_external.sample(5, random_state=99).index
df_external.drop(index=drop_rows, inplace=True)

# Save as external version
df_external.to_csv("data/mortgage_loans_external.csv", index=False)
print("✅ External dataset with mismatches created.")
