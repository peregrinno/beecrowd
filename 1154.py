cont, media = 0, 0
while True:
    x = int(input())
    if x < 0:
        break
    else:
        cont += 1
        media += x

print("{:.2f}".format(media / cont))
        