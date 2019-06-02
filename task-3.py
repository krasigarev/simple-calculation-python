n = float(input())   # страна на квадрат
w = float(input())   # едната страна на плочка
l = float(input())   # другата страна на плочка
m = float(input())   # широчина на пейката
o = float(input())   # дължина на пейката

lice_square = n**2
lice_peika = m * o
area_with_tiles = lice_square-lice_peika
area_tiles = w*l
area_count = area_with_tiles/area_tiles
time = area_count*0.2

print(area_count)
print(time)
