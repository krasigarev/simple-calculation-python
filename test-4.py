bitcion = int(input())
yan = float(input())
commision = float(input())

dollar = yan * 0.15  # result dollar
lev = (bitcion * 1168) + (dollar*1.76)  # result lev
euro = lev / 1.95  # result euro

var = euro * (commision / 100)

ddd = euro - var
print(ddd)


