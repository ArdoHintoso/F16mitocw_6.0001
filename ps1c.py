# initialize variables for bisection search

low = 0
high = 10000
portion_saved = ((low+high)/2)/10000
epsilon = 100
steps = 0

# initialize other variables

initial_salary = float(input("Enter the starting salary: "))
semi_annual_raise = 0.07
r = 0.04
portion_down_payment = 0.25
total_cost = 1000000.0
max_months = 36
current_savings = []

# function for calculating savings

def getSavings(portion_saved):
    # reinitialize
    current_savings = []
    annual_salary = initial_salary 

    for month in range(0,max_months):  
        if ((month) % 6 == int(0)) and month > 0:
            annual_salary *= (1.0 + semi_annual_raise) 
                
        inv_returns = (sum(list(current_savings))) * (r / 12)
        current_savings.append(annual_salary/12 * portion_saved + inv_returns)  

    return current_savings

# include case when impossible to save in 36 months
      
if sum(list(getSavings(1))) < (total_cost * portion_down_payment):
    print("It is not possible to pay the down payment in three years")
else:
    # bisection search
    
    while abs(sum(list(current_savings)) - (total_cost * portion_down_payment)) >= epsilon:
        current_savings = getSavings(portion_saved)
        
        if sum(list(current_savings)) > (total_cost * portion_down_payment):
            high = portion_saved * 10000
        else: 
            low = portion_saved * 10000

        portion_saved = ((low+high)/2)/10000
        steps += 1

    # print results 

    print(f"Best savings rate: {round(portion_saved,6)}")
    print(f"Steps in bisection search: {round(steps,6)}")  

