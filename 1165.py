t = int(input())

for i in range(t):
    x = int(input())
    n_p = 0
    p = 0
 
    for j in range(1,x+1):
        if x % j == 0:
            p += 1
        else:
            n_p += 1
        if p > 2:
            break
            
    if p > 2:
        print(f'{x} nao eh primo')
    else:
        print(f'{x} eh primo')