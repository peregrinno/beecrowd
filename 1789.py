maiores = []
while True:
    try:
        x = int(input())
        lesmas = input().split()
        maior = 0
        for i in range(len(lesmas)):
            if int(lesmas[i]) > maior:
                maior = int(lesmas[i])
        maiores.append(maior)
    except:
        break

for i in range(len(maiores)):
    if maiores[i] >= 20:
        print('3')
    elif 10 < maiores[i] < 20:
        print('2')
    else:
        print('1')