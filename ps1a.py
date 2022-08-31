def getMonth():
    def askQuestions():
        q1_res = float(input("Please declare your annual salary (in thousands, USD): ")) * 1000
        q2_res = float(input("How much would you like to save each month (please represent your response as a percentage without the ampersand sign? ")) / 100
        q3_res = float(input("What is the price of your dream house (in millions, USD)? ")) * 1000000
        return q1_res, q2_res, q3_res

    def computeNum(semi_annual_raise = 0.0):
        annual_salary = q1_res 
        portion_saved = q2_res
        total_cost = q3_res 
        portion_down_payment = 0.25
        current_savings = [0]
        month = 0
        r = 0.04

        # of working months required 

        while sum(list(current_savings)) < (total_cost * portion_down_payment): 
            if month % 6 == 0 and month > 0:
                annual_salary *= (1.0 + semi_annual_raise) 

            month += 1

            inv_returns = (sum(list(current_savings))) * (r/12) 
            current_savings.append(inv_returns + annual_salary/12 * portion_saved)

            if (((total_cost) * (portion_down_payment)) - (sum(list(current_savings)))) <= 0: 
                print(f"It would take {month} months to save enough for a down payment.")

        # for month in range(0,1000):  
        #     if ((month) % 6 == int(0)) and month > 0:
        #         annual_salary *= (1.0 + semi_annual_raise) 
                    
        #     inv_returns = (sum(list(current_savings))) * (r / 12)
        #     current_savings.append(annual_salary/12 * portion_saved + inv_returns)  

        #     if (((total_cost) * (portion_down_payment)) / (sum(list(current_savings)))) <= 1:
        #         month += 1
        #         print(f"It will take {month} months to save enough for a down payment.")
        #         break   

        return annual_salary, portion_saved, total_cost, portion_down_payment, current_savings
        
    return askQuestions, computeNum 

askQuestions, computeNum = getMonth()

q1_res, q2_res, q3_res = askQuestions()

print("\nWithout any increase in salary: ")
computeNum()

