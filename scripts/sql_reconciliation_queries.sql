-- Use the correct database
USE mortgage_db;

-- 🔎 1. Find loan IDs present in internal but missing from external
SELECT Loan_ID 
FROM internal_loans
WHERE Loan_ID NOT IN (SELECT Loan_ID FROM external_loans);

-- 🔎 2. Find loan IDs present in external but missing from internal
SELECT Loan_ID 
FROM external_loans
WHERE Loan_ID NOT IN (SELECT Loan_ID FROM internal_loans);

-- 🔎 3. Mismatched Loan_Amount values for same Loan_ID
SELECT i.Loan_ID, i.Loan_Amount AS Internal_Amount, e.Loan_Amount AS External_Amount
FROM internal_loans i
JOIN external_loans e ON i.Loan_ID = e.Loan_ID
WHERE i.Loan_Amount != e.Loan_Amount;

-- 🔎 4. Count of total mismatches in loan amount
SELECT COUNT(*) AS Mismatch_Count
FROM internal_loans i
JOIN external_loans e ON i.Loan_ID = e.Loan_ID
WHERE i.Loan_Amount != e.Loan_Amount;

-- 🔎 5. Summary: count of missing and mismatched
SELECT 
    (SELECT COUNT(*) FROM internal_loans WHERE Loan_ID NOT IN (SELECT Loan_ID FROM external_loans)) AS Missing_in_External,
    (SELECT COUNT(*) FROM external_loans WHERE Loan_ID NOT IN (SELECT Loan_ID FROM internal_loans)) AS Missing_in_Internal,
    (SELECT COUNT(*) FROM internal_loans i
        JOIN external_loans e ON i.Loan_ID = e.Loan_ID
        WHERE i.Loan_Amount != e.Loan_Amount) AS Amount_Mismatches;
