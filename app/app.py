from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    result = None

    if request.method == "POST":

        business_name = request.form["business_name"]

        annual_revenue = float(request.form["annual_revenue"])

        existing_debt = float(request.form["existing_debt"])

        credit_score = int(request.form["credit_score"])

        missed_payments = int(request.form["missed_payments"])

        loan_amount = float(request.form["loan_amount"])

        repayment_years = int(request.form["repayment_years"])

        debt_ratio = existing_debt / annual_revenue

        risk_score = (
            (credit_score / 850) * 60
            - (missed_payments * 10)
            - (debt_ratio * 30)
        )

        reasons = []

        if credit_score >= 750:
            reasons.append("Strong credit score supports approval.")
        elif credit_score >= 600:
            reasons.append("Credit score is acceptable but not strong.")
        else:
            reasons.append("Low credit score increases lending risk.")

        if missed_payments == 0:
            reasons.append("No missed payments improves borrower reliability.")
        elif missed_payments <= 2:
            reasons.append("Recent missed payments require closer review.")
        else:
            reasons.append("Multiple missed payments significantly reduce approval strength.")

        if debt_ratio <= 0.20:
            reasons.append("Debt is low compared to annual revenue.")
        elif debt_ratio <= 0.50:
            reasons.append("Debt level is moderate compared to annual revenue.")
        else:
            reasons.append("Debt is high compared to annual revenue.")

        if risk_score >= 50:
            decision = "APPROVE"
            interest_rate = 8
            decision_class = "approve"
            recommendation = "This borrower appears strong enough for approval based on the current credit score, payment history, and debt position."

        elif risk_score >= 30:
            decision = "REVIEW"
            interest_rate = 15
            decision_class = "review"
            recommendation = "This borrower should be reviewed manually. Approval may be possible if the business reduces debt, improves payment history, or provides stronger supporting documents."

        else:
            decision = "REJECT"
            interest_rate = 0
            decision_class = "reject"
            recommendation = "This borrower does not currently meet the approval threshold. The strongest path to approval would be lowering debt, improving credit score, and avoiding missed payments."

        if interest_rate > 0:

            monthly_interest = (interest_rate / 100) / 12

            total_payments = repayment_years * 12

            monthly_payment = (
                loan_amount *
                (
                    monthly_interest *
                    (1 + monthly_interest) ** total_payments
                ) /
                (
                    (1 + monthly_interest) ** total_payments - 1
                )
            )

            monthly_payment = round(monthly_payment, 2)

            total_repayment = monthly_payment * total_payments

            total_interest_income = total_repayment - loan_amount

        else:

            monthly_payment = "N/A"

            total_interest_income = "N/A"

        result = {
            "business_name": business_name,
            "annual_revenue": f"N${annual_revenue:,.0f}",
            "existing_debt": f"N${existing_debt:,.0f}",
            "loan_amount": f"N${loan_amount:,.0f}",
            "repayment_years": repayment_years,
            "risk_score": round(risk_score, 2),
            "decision": decision,
            "interest_rate": f"{interest_rate}%" if interest_rate > 0 else "N/A",
            "monthly_payment": f"N${monthly_payment:,.2f}" if monthly_payment != "N/A" else "N/A",
            "total_interest_income": f"N${total_interest_income:,.2f}" if total_interest_income != "N/A" else "N/A",
            "decision_class": decision_class,
            "reasons": reasons,
            "recommendation": recommendation
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)