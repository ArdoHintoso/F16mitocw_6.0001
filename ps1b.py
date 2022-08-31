from ps1a import getMonth
import numpy as np

# ask previous and new questions

askQuestion, computeNum = getMonth()

semi_annual_raise = float(input("\nEnter the semi-annual raise, as a decimal: "))

annual_salary, portion_saved, total_cost, portion_down_payment, current_savings = computeNum(semi_annual_raise)

a = (total_cost * portion_down_payment)
b = (sum(list(current_savings)))

print(a)
print(b)
print(b >= a) 

# print("\nLet's see.. If your boss was more generous and doubled your raise: ")
# annual_salary, portion_saved, total_cost, portion_down_payment, current_savings = computeNum(2*semi_annual_raise)

# print(sum(list(current_savings))+annual_salary/12*portion_saved)


# Others solution 

# print("\nLet's check our answer with collaborators:\n")

# salary_annual = float(input("Enter your annual salary:"))
# saved_portion = float(input("Enter the percent of your salary to save, as a decimal:"))
# cost_total = float(input("Enter the cost of your dream home:"))
# annual_raise_semi = float(input("Enter your semi-annual raise, as a decimal"))

# down_payment_portion = 0.25
# savings_current = 0
# r = 0.04

# salary_monthly = salary_annual / 12 
# months = 0 

# while savings_current < cost_total * down_payment_portion: 
#     savings_current += (savings_current * r / 12)
#     savings_current += (salary_monthly * saved_portion)

#     if months % 6 == 0 and months > 0:
#         salary_monthly += salary_monthly*annual_raise_semi
#     months += 1

# print("Number of months: ", months)
# print(current_savings)
# print(f"my savings = {sum(list(current_savings))} vs theirs = {savings_current}. Difference? {sum(list(current_savings)) - savings_current}")



