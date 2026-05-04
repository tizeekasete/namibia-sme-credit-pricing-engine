DROP TABLE IF EXISTS sme_loans;

CREATE TABLE sme_loans (
    business_id INTEGER,
    business_name TEXT,
    sector TEXT,
    annual_revenue REAL,
    years_in_business INTEGER,
    loan_amount REAL,
    existing_debt REAL,
    credit_score INTEGER,
    missed_payments INTEGER,
    collateral_value REAL,
    loan_term_months INTEGER
);

-- Debt ratio
SELECT 
    business_name,
    annual_revenue,
    existing_debt,
    ROUND(existing_debt * 1.0 / annual_revenue, 3) AS debt_ratio
FROM sme_loans;

-- Multi-factor risk model
SELECT 
    business_name,
    credit_score,
    missed_payments,
    ROUND(existing_debt * 1.0 / annual_revenue, 3) AS debt_ratio,
    CASE
        WHEN credit_score < 600 OR missed_payments >= 3 OR (existing_debt * 1.0 / annual_revenue) > 0.5 THEN 'High Risk'
        WHEN credit_score < 680 OR missed_payments >= 1 OR (existing_debt * 1.0 / annual_revenue) > 0.3 THEN 'Medium Risk'
        ELSE 'Low Risk'
    END AS risk_category
FROM sme_loans;

-- Scoring model
SELECT 
    business_name,
    ROUND(
        (credit_score / 850.0) * 60
        - (missed_payments * 10)
        - ((existing_debt * 1.0 / annual_revenue) * 30)
    , 2) AS risk_score
FROM sme_loans;

-- Final decision model
SELECT 
    business_name,
    ROUND(
        (credit_score / 850.0) * 60
        - (missed_payments * 10)
        - ((existing_debt * 1.0 / annual_revenue) * 30)
    , 2) AS risk_score,
    CASE
        WHEN (
            (credit_score / 850.0) * 60
            - (missed_payments * 10)
            - ((existing_debt * 1.0 / annual_revenue) * 30)
        ) >= 50 THEN 'APPROVE'
        WHEN (
            (credit_score / 850.0) * 60
            - (missed_payments * 10)
            - ((existing_debt * 1.0 / annual_revenue) * 30)
        ) >= 30 THEN 'REVIEW'
        ELSE 'REJECT'
    END AS decision
FROM sme_loans;
-- =========================
-- LOAN DECISION VIEW
-- =========================
CREATE VIEW loan_decisions AS
SELECT
    business_name,
    credit_score,
    missed_payments,
    ROUND(existing_debt * 1.0 / annual_revenue, 3) AS debt_ratio,

    ROUND(
        (credit_score / 850.0) * 60
        - (missed_payments * 10)
        - ((existing_debt * 1.0 / annual_revenue) * 30),
    2) AS risk_score,

    CASE
        WHEN (
            (credit_score / 850.0) * 60
            - (missed_payments * 10)
            - ((existing_debt * 1.0 / annual_revenue) * 30)
        ) >= 40 THEN 'Approve'

        WHEN (
            (credit_score / 850.0) * 60
            - (missed_payments * 10)
            - ((existing_debt * 1.0 / annual_revenue) * 30)
        ) >= 25 THEN 'Review'

        ELSE 'Reject'
    END AS decision

FROM sme_loans;