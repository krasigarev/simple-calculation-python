budget = int(input())
season = input()

sum_of_vacation = 0

if budget <= 100:
    if season == "summer":
        sum_of_vacation = budget*0.3
        destination = "Bulgaria"
        type_season = "Camp"
    else:
        sum_of_vacation = budget*0.7
        destination = "Bulgaria"
        type_season = "Hotel"
elif budget <= 1000:
    if season == "summer":
        sum_of_vacation = budget*0.4
        destination = "Balkans"
        type_season = "Camp"
    else:
        sum_of_vacation = budget*0.8
        destination = "Balkans"
        type_season = "Hotel"
else:
    sum_of_vacation = budget*0.9
    destination = "Europe"
    type_season = "Hotel"


print(f"Somewhere in {destination}!\n"
      f"{type_season} - {sum_of_vacation:.2f}")
