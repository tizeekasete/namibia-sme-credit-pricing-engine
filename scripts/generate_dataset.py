import pandas as pd
import random

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

    records.append([
        i,
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
        collateral_value
    ])

df = pd.DataFrame(records, columns=[
    "business_id",
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
    "collateral_value"
])

df.to_csv(
    "data/sme_loans.csv",
    index=False
)
print("Dataset generated successfully.")