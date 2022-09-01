import math
try:
    finalValue = input("Enter final account value: ")
    annualRate = input("Enter annual interest rate in percent: ")
    years = input("Enter number of years: ")
    months = years/12
    monthlyRate = annualRate/12
    initial = str(round(finalValue/(math.pow(1+monthlyRate,months)),2))
    print("Initial deposit amount is " + initial)
except ValueError:
    print("You did not enter a number")
