import pandas as pd
import random
from datetime import datetime, timedelta

regions = [
    "Khomas",
    "Erongo",
    "Otjozondjupa",
    "Oshana",
    "Oshikoto",
    "Kavango East",
    "Kavango West",
    "Hardap",
    "Karas"
]

industries = [
    "Retail",
    "Logistics",
    "Construction",
    "Agriculture",
    "Technology",
    "Tourism",
    "Manufacturing",
    "Mining Services",
    "Transport",
    "Food Services"
]

loan_purposes = [
    "Working Capital",
    "Expansion",
    "Equipment Purchase",
    "Inventory",
    "Vehicle Purchase",
    "Payroll Support",
    "Construction",
    "Technology Upgrade"
]

collateral_types = [
    "Property",
    "Vehicle",
    "Equipment",
    "Inventory",
    "Livestock",
    "Savings"
]

business_prefixes = [
    "Oshana",
    "Erongo",
    "Walvis",
    "Windhoek",
    "Etosha",
    "Kunene",
    "Swakop",
    "Otji",
    "Kalahari",
    "Caprivi",
    "Namib",
    "Okavango",
    "Luderitz",
    "Gobabis",
    "Katima"
]

business_suffixes = [
    "Trading",
    "Logistics",
    "Construction",
    "Retail",
    "Fishing",
    "Supplies",
    "Technologies",
    "Farming",
    "Manufacturing",
    "Food Services",
    "Tours",
    "Transport"
]

records = []

record_count = random.randint(1000, 1500)

start_date = datetime(2025, 1, 1)

for i in range(1, record_count + 1):

    business_name = (
        random.choice(business_prefixes)
        + " "
        + random.choice(business_suffixes)
    )

    industry = random.choice(industries)

    region = random.choice(regions)

    years_in_business = random.randint(1, 25)

    employees = random.randint(2, 250)

    loan_amount = random.randint(50000, 2500000)

    loan_purpose = random.choice(loan_purposes)

    loan_term = random.choice([12, 24, 36, 48, 60])

    annual_revenue = random.randint(300000, 15000000)

    monthly_expenses = random.randint(20000, 800000)

    cash_balance = random.randint(10000, 3000000)

    existing_debt = random.randint(0, 4000000)

    monthly_debt_payments = random.randint(0, 120000)

    credit_score = random.randint(450, 850)

    missed_payments = random.randint(0, 8)

    prior_defaults = random.choice([0, 0, 0, 1])

    collateral_type = random.choice(collateral_types)

    collateral_value = random.randint(50000, 5000000)

    application_date = start_date + timedelta(
        days=random.randint(0, 365)
    )

    debt_to_revenue_ratio = round(
        existing_debt / annual_revenue,
        2
    )

    loan_to_collateral_ratio = round(
        loan_amount / collateral_value,
        2
    )

    if monthly_debt_payments == 0:

        debt_service_coverage_ratio = 99

    else:

        debt_service_coverage_ratio = round(
            (
                (
                    annual_revenue
                    - (monthly_expenses * 12)
                ) / 12
            ) / monthly_debt_payments,
            2
        )

    risk_score = (
        ((credit_score - 300) / 10)
        + (years_in_business * 1.5)
        + (cash_balance / 50000)
        - (existing_debt / 100000)
        - (missed_payments * 8)
        - (prior_defaults * 20)
    )

    risk_score = round(risk_score, 1)

    if risk_score >= 80:

        decision = "Approved"

        risk_level = "Low Risk"

        interest_rate = 0.08

        pricing_tier = "Standard Risk-Based Rate"

    elif risk_score >= 45:

        decision = "Review"

        risk_level = "Medium Risk"

        interest_rate = 0.15

        pricing_tier = "Elevated Risk Premium"

    else:

        decision = "Rejected"

        risk_level = "High Risk"

        interest_rate = 0

        pricing_tier = "No Pricing Offer"

    if interest_rate > 0:

        monthly_rate = interest_rate / 12

        total_payments = loan_term

        monthly_payment = loan_amount * (
            monthly_rate
            * (1 + monthly_rate) ** total_payments
        ) / (
            (1 + monthly_rate) ** total_payments - 1
        )

        monthly_payment = round(
            monthly_payment,
            2
        )

        total_repayment = round(
            monthly_payment * loan_term,
            2
        )

        total_interest_income = round(
            total_repayment - loan_amount,
            2
        )

    else:

        monthly_payment = 0

        total_repayment = 0

        total_interest_income = 0

    approval_probability = max(
        min(
            round(risk_score * 1.1, 2),
            100
        ),
        0
    )

    records.append([
        i,
        application_date,
        business_name,
        industry,
        region,
        years_in_business,
        employees,
        loan_amount,
        loan_purpose,
        loan_term,
        annual_revenue,
        monthly_expenses,
        cash_balance,
        existing_debt,
        monthly_debt_payments,
        credit_score,
        missed_payments,
        prior_defaults,
        collateral_type,
        collateral_value,
        debt_to_revenue_ratio,
        debt_service_coverage_ratio,
        loan_to_collateral_ratio,
        risk_score,
        risk_level,
        decision,
        interest_rate,
        pricing_tier,
        monthly_payment,
        total_repayment,
        total_interest_income,
        approval_probability
    ])

df = pd.DataFrame(records, columns=[
    "business_id",
    "application_date",
    "business_name",
    "industry",
    "region",
    "years_in_business",
    "employees",
    "loan_amount",
    "loan_purpose",
    "loan_term",
    "annual_revenue",
    "monthly_expenses",
    "cash_balance",
    "existing_debt",
    "monthly_debt_payments",
    "credit_score",
    "missed_payments",
    "prior_defaults",
    "collateral_type",
    "collateral_value",
    "debt_to_revenue_ratio",
    "debt_service_coverage_ratio",
    "loan_to_collateral_ratio",
    "risk_score",
    "risk_level",
    "decision",
    "interest_rate",
    "pricing_tier",
    "monthly_payment",
    "total_repayment",
    "total_interest_income",
    "approval_probability"
])

df.to_csv(
    "data/powerbi_sme_lending_portfolio.csv",
    index=False
)

df.to_csv(
    "data/sme_loans.csv",
    index=False
)

print("Dataset generated successfully.")

print(f"Rows generated: {len(df)}")

print("Files created:")

print("data/sme_loans.csv")

print("data/powerbi_sme_lending_portfolio.csv")