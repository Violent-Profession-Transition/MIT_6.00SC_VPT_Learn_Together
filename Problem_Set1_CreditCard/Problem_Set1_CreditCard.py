""" Paying Off Credit Card Debt
 minimum monthly payment is split to cover
 1. interest paid
 2. principal paid
"""
import time


# Problem 1 paying the minimum
# write a program to calculate the credit card balance after one year
# if the person only pays the minimal monthly payment
def summary_of_paying_minimal():
    outstanding_balance = float(input("the outstanding balance on the credit card: "))
    annual_interest_rate = float(input("annual interest rate: "))
    min_monthly_rate = float(input("minimum monthly payment rate: "))
    total_paid = 0
    for month in range(1, 13):
        print("Month: ", month)
        min_monthly_payment = outstanding_balance * min_monthly_rate
        total_paid += min_monthly_payment
        print("Minimum monthly payment: ${}".format(round(min_monthly_payment, 2)))
        interest_paid = (annual_interest_rate/12) * outstanding_balance
        principal_paid = min_monthly_payment - interest_paid
        print("Principal paid: ${}".format(round(principal_paid, 2)))
        outstanding_balance = outstanding_balance - principal_paid
        print("Remaining balance: ${}".format(round(outstanding_balance, 2)))
    print("=========RESULT:==========")
    print("Total amount paid: ${}".format(round(total_paid, 2)))
    print("Remaining balance: ${}".format(round(outstanding_balance, 2)))

# Problem 2
# a problem calculating the minimum fixed monthly payment
# needed to pay off debt in 12 month

def can_pay_off(outstanding_balance, annual_interest_rate, monthly_payment):
    can_pay_off = False
    month = 1
    print("trying out monthly_payment of: ", monthly_payment)
    while month <= 12:
        interest_paid = (annual_interest_rate/12) * outstanding_balance
        if monthly_payment < interest_paid:
            break
        principal_paid = monthly_payment - interest_paid
        outstanding_balance = outstanding_balance - principal_paid
        print("outstanding_balance is now: ", outstanding_balance)
        if abs(outstanding_balance) <= 0.05:
            can_pay_off = True
            break
        month += 1
        time.sleep(0.01)
    return {
        "can_pay_off": can_pay_off,
        "month": month,
        "outstanding_balance": outstanding_balance
    }
    

def minimal_fixed_month_payment():
    outstanding_balance = float(input("the outstanding balance on the credit card: "))
    annual_interest_rate = float(input("annual interest rate: "))
    # use bisection search
    # even if there is no interest for original balance
    # we still must pay at least 1/12 of the original balance
    # so this should be the lower bound
    lower_bound = outstanding_balance/12
    # if we pay the compounded interest for the whole balance
    # without subtracting any monthly payment
    # that is the upper bound
    upper_bound = (outstanding_balance * (1+annual_interest_rate/12)**12) / 12
    monthly_payment = (upper_bound + lower_bound) / 2
    pay_off_status = can_pay_off(
        outstanding_balance,
        annual_interest_rate,
        monthly_payment)
    while not pay_off_status["can_pay_off"]:
        print("while not pay_off_status")
        if pay_off_status["outstanding_balance"] < 0:
            print("paying too much")
            upper_bound = monthly_payment
        else:
            lower_bound = monthly_payment
        monthly_payment = (upper_bound + lower_bound) / 2
        pay_off_status = can_pay_off(
            outstanding_balance,
            annual_interest_rate,
            monthly_payment)
    print("=========RESULT:==========")
    print("monthly payment to pay off debt in 1 year: ", round(monthly_payment, 2))
    print("number of months needed: ", pay_off_status["month"])
    print("balance: ", round(pay_off_status["outstanding_balance"], 2))
