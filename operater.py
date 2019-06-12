n1 = int(input())
n2 = int(input())

operater = input()

result = 0


if operater == "+":
    result = n1 + n2
elif operater == "-":
    result = n1 - n2
elif operater == "*":
    result = n1 * n2
elif operater == "/":
    result = n1 / n2
elif operater == "%":
    result = n1 % n2
else:
    print(f"Cannot divide {n1} by zero")

if result % 2 == 0:
    result2 = "even"
else:
    result2 = "odd"


print(f"{n1} {operater} {n2}"
      f" == {result} - {result2}")
