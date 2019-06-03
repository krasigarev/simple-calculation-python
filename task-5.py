working_day = int(input())
salary_dally = float(input())
rate = float(input())


day = working_day * salary_dally
profit = (((day * 12) + (day * 2.5))* 0.75)*rate / 365

print(profit)




