# изчислява броя работни места в една зала

length = float(input())
width = float(input())

a = length // 120
b = (width - 100) // 70

sum = (a * b) - 3
print(sum)
