s, d = 1, 2

for n in range(3, 39, 2):   
    s += n/d
    n += 2
    d *= 2
    
print("{:.2f}".format(s))