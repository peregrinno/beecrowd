cases, soma = [],[]
n = int(input())

while n != 0:
    if n == 0:
        pass
    else:
        if n % 2 != 0:
            n = n+1
        for i in range(5):
            soma.append(n)
            n += 2
        cases.append(sum(soma))
    n = int(input())
    soma = []

for i in range(len(cases)):
    print(cases[i])
                