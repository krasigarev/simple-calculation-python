n = float(input())   # страна на квадрат
w = float(input())   # едната страна на плочка
l = float(input())   # другата страна на плочка
m = float(input())   # широчина на пейката
o = float(input())   # дължина на пейката

lice_square = n**2
lice_peika = m * o
sum_plo6a = lice_square-lice_peika
lice_plochki = w*l
broi_plochki = sum_plo6a/lice_plochki
time = broi_plochki*0.2

print(broi_plochki)
print(time)
