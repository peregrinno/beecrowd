x = int(input())
z, i = x, x
cont = 1

while z <= x:
    z = int(input())

while x <= z:
    x += i
    i += 1
    cont += 1
    
print(cont)      