a = float(input())  # цена на килограм зеленчуци
b = float(input())  # цена на килограм плодове
c = int(input())    # количество зеленчуци
e = int(input())    # количество плодове

result = 0
# if 0 < a < 1001 and 0 < b < 1001 and 0 < c < 1001 and 0 < e < 1001:
if 0 < a and b and c and e <1011:
    sum1 = a * c
    sum2 = b * e
    result = sum1 + sum2
    print("{0:.5f}".format(result))
else:
    print('Невалидна стойност')
