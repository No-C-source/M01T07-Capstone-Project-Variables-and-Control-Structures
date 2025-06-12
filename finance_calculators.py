import math

#Pseudocode for the financial calculators
#Ask user to choose between an investment or a bond calculator

#Accept input regardless of capitalisation by user 
#Create error message if user input is not valid 

#Investment Calculator 
#User captures amount they want to invest 
#User inputs the value of the interest rate
#User captures the number of years they want to invest 
#User inputs the type of interest (simple or compound)
#A = P * (1 + r*t) simple interest formula
#A = P * math.pow((1+r),t) compound interest formula
#Output the total amount of money they will have at the end of the investment period

#Bond Calculator
#User captures the value of the house they want to buy
#User inputs the interest rate
#User captures the number of months they want to pay the bond
#repayment = (i * P)/(1 - (1 + i)**(-n)) bond repayment formula
#i = interest rate / 100 / 12
#Output the monthly repayment amount

#Python code for investment calculator
investment_amount = float(input("Enter the amount you want to invest: \nR"))
interest_rate = float(input("Enter the interest rate: "))
years = int(input("Enter the number of years you want to invest: "))
interest_type = input("Enter the type of interest (simple or compound): ").lower()
if interest_type == "simple":
    total_amount = investment_amount * (1 + (interest_rate / 100) * years)
elif interest_type == "compound":
    total_amount = investment_amount * math.pow((1 + interest_rate / 100), years)
else:
    total_amount = None
    print("Invalid interest type. Please enter 'simple' or 'compound'.")
if total_amount is not None:
    print(f"The total amount after {years} years is: R{total_amount:.2f}")

#Python code for the bond calculator
house_value = float(input("Enter the Rand-value of your house: \nR"))
interest_rate = float(input("Specify interest rate: "))
months = int(input("Number of months to repay home loan: "))
calculated_interest = interest_rate / 100 / 12

repayment = (calculated_interest * house_value) / (1-(1 + calculated_interest) ** (-months))

print(f"The monthly repayment amount is: R{repayment:.2f}")