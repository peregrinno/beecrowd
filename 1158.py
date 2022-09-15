n = int(input())
soma = 0
cases = []
for i in range(n):
    x, y = input().split(" ")
    x, y = int(x), int(y)
    if x % 2 == 0:
        z = x+1
    else:
        z = x
    for j in range(y):
        soma += z
        z += 2
    cases.append(soma)
    soma = 0

for i in range(n):
    print(cases[i])