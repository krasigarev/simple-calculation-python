# лице на триъгълник в равнината


x1 = int(input())  # num1
y1 = int(input())  # num2
x2 = int(input())  # num3
y2 = int(input())  # num4  y2 = y3
x3 = int(input())  # num5
y3 = int(input())  # num6  y2 = y3


def triangle(num1, num2, num3, num4, num5, num6):
    a = abs(x2 - x3)
    h = abs(y2 - y1)
    s = a*h/2
    print(s)


print('\n----------\n ')

triangle(x1, y1, x2, y2, x3, y3)

print('\n----------\n ')

triangle(x1, y1, x2, y2, x3, y3)

print('\n----------\n ')

triangle(x1, y1, x2, y2, x3, y3)
