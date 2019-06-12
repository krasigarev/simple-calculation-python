#  цена на хотелска стая

month = input()
night = int(input())

overnight = 0
overnight1 = 0

if month == "may" or month == "october":
    if night <= 14:
        price = 50
        overnight = (night * price) * 0.95
    elif night > 14:
        price = 50
        overnight = (night * price) * 0.7
    else:
        price = 50
        overnight = night * price
elif month == "june" or month == "september":
    if night <= 14:
        price = 75.20
        overnight = night * price
    elif night > 14:
        price = 75.20
        overnight = (night * price) * 0.8

elif month == "july" or month == "august":
    if night <= 14:
        price = 76
        overnight = night * price
    elif night > 14:
        price = 76
        overnight = night * price
else:
    if month == "may" or month == "october":
        if night <= 14:
            price = 65
            overnight1 = night * price
        elif night > 14:
            price = 65
            overnight1 = (night * price) * 0.90

    elif month == "june" or month == "september":
        if night < 14:
            price = 68.20
            overnight1 = night * price
        elif night > 14:
            price = 68.20
            overnight1 = (night * price) * 0.90
    elif month == "july" or month == "august":
        if night <= 14:
            price = 77
            overnight1 = night * price
        elif night > 14:
            price = 77
            overnight1 = (night * price) * 0.90


print(f"Apartment {overnight1:.2f} leva")
print(f"Studio {overnight:.2f} leva")
