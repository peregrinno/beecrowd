a, b = input().split(" ")
a, b = int(a), int(b)
if a < 0:
    e = b
    if b < 0: e = b * -1
    for r in range(e):
        f = a - r
        if f%b == 0: break
    q = f / b
else:
    q = a / b
    r = a % b        
if r == -2:
    r = 1
elif q == -0:
    q = 0

print(f'{q:.0f} {r}')