t = int(input())

for i in range(t):
    x = int(input())
    n = 0
    for j in range(1,x):
        if x % j == 0:
            n += j
    
    if n == x:
        print(f'{x} eh perfeito')
    else:
        print(f'{x} nao eh perfeito')