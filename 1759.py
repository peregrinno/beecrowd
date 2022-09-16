n = int(input())
ho = ""
for i in range(n):
    if i == n-1:
        ho += "Ho"
    else:
        ho += "Ho "
        
ho += "!"

print(ho)