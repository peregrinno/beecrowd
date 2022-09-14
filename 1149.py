entrada = []
entrada = input().split(" ")
a = int(entrada[0])

for i in range(1,len(entrada)):
    n = int(entrada[i])
    if int(entrada[i]) > 0:
        break
       
a, n = int(a), int(n)
i, x = 0, 0

while i <= n - 1:
    x += a + i
    i += 1

print (x)


