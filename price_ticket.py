#  цена на билети

budget = float(input())
category = input()
number_of_fans = int(input())

transport_charges = 0.00
money_for_ticket = 0.00
money_difference = 0.00

if number_of_fans <= 4:
    transport_charges = 0.75 * budget
elif number_of_fans <= 9:
    transport_charges = 0.6 * budget
elif number_of_fans <= 24:
    transport_charges = 0.5 * budget
elif number_of_fans <= 49:
    transport_charges = 0.4 * budget
else:
    transport_charges = 0.25 * budget


if category == "Normal":
    money_for_ticket = number_of_fans * 249.99
else:
    money_for_ticket = number_of_fans * 499.99


money_difference = budget - transport_charges - money_for_ticket

result = f"Yes! You have {money_difference:.2f} leva left"

if money_difference < 0:
    result = "Not enough money!" + f" You need {abs(money_difference):.2f} leva"


print(result)
