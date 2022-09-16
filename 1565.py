MAXIDITON = []
c = 0
while True:
    try:
        x = int(input())
        MAXIDITON.append(x)
        c = c + 1
    except:
        break

for i in MAXIDITON[0:c]:
    if i == 0:
        print('vai ter copa!')
    if i != 0:
        print('vai ter duas!')