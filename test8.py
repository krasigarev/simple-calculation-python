n = int(input())
result = ''
a = 1

for a in range(1, n+1):
    for b in range(1, n+1):
        for c in range(1, n+1):
            for d in range(1, n+1):
                for e in range(1, n+1):
                    for f in range(1, n+1):
                        if a*b*c*d*e*f == n:
                            result += f"{a} * {b} * {c} * {d} * {e} * {f} \n"

print(result)

