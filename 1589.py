t = int(input())

for i in range(t):
    entrada = []
    entrada = input().split()
    r1, r2 = int(entrada[0]), int(entrada[1])
    print(f'{r1+r2}')