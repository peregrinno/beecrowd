n = int(input())
fib = []
saida = ""
x, i = 0,0

for i in range(n):
    if i == 0:
        fib.append(0)
        saida += str(fib[i]) + " "
    elif i == 1:
        fib.append(1)
        saida += str(fib[i])
    else:
        fib.append(fib[i-1] + fib[i-2])
        saida += " " + str(fib[i-1] + fib[i-2])

print(saida)