print("You are %s %s, a %d-years old person from %s." % ("Krasi", "Garev", 20, "pleven"))

first_name = "Krasi"  # input()
last_name = "Garev"  # input()     f-strings
age = 20  # int()
town = "Pleven"  # input()
print(f"You are {first_name} {last_name}, a {age}-years old person from {town}")


# конкатенация --- тя се извършва с знака за +

first_name = "Krasi"   # input()
last_name = "Garev"    # input()     f-strings
age = 20               # int()
town = "Pleven"        # input()
str = first_name + " " + last_name + " is " + str(age) + " years old."
print(str)
