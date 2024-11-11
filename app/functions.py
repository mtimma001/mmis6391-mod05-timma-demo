# Function to calculate the letter grade based on the average of the grades
def calculate_grades(grade):
    # avg = sum(grades) / len(grades)
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'


# Function to calculate the loan amortization details
def loan_amortization(loan_amount, interest_rate, loan_term_years):

    loan_term_months = loan_term_years * 12
    monthly_interest_rate = interest_rate / 12 / 100

    if monthly_interest_rate > 0:
        monthly_payment = loan_amount * (monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -loan_term_months))
    else:
        monthly_payment = loan_amount / loan_term_months

    loan_amortization_list = []

    for i in range(1, loan_term_months, 1):
        interest_paid = loan_amount * monthly_interest_rate
        principal_paid = monthly_payment - interest_paid
        remaining_balance = loan_amount - principal_paid

        loan_amortization_list.append({
            'month': i,
            'starting_balance': loan_amount,
            'interest_paid': interest_paid,
            'principal_paid': principal_paid,
            'monthly_payment': monthly_payment,
            'remaining_balance': remaining_balance
        })

        loan_amount = remaining_balance

    return loan_amortization_list

# Remove the usage part since we call this functions elsewhere
# # Test the calculate_grades function
# grades_list = [85, 92, 78, 90, 88]
# print("Grades:", grades_list)
# print("Letter Grade:", calculate_grades(grades_list))
#

# # Test the loan_amortization function
# loan_amt = 10000  # Loan amount
# interest_rt = 5  # Annual interest rate (in percentage)
# loan_term_yrs = 2  # Loan term in years
#
# print(f"\nLoan: ${loan_amt}, Interest Rate: {interest_rt}%, Term: {loan_term_yrs} years")
# amortization_schedule = loan_amortization(loan_amt, interest_rt, loan_term_yrs)
#
# # Print the amortization schedule for the first few months
# print("\nAmortization Schedule (First 5 Months):")
# for month_info in amortization_schedule[:5]:  # Display only the first 5 months
#     print(f"Month {month_info['month']}:")
#     print(f"  Starting Balance: ${month_info['starting_balance']:.2f}")
#     print(f"  Interest Paid: ${month_info['interest_paid']:.2f}")
#     print(f"  Principal Paid: ${month_info['principal_paid']:.2f}")
#     print(f"  Monthly Payment: ${month_info['monthly_payment']:.2f}")
#     print(f"  Remaining Balance: ${month_info['remaining_balance']:.2f}")