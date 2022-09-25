n = int(input())
nomes = []
medias = []
for i in range(n):
    entrada = []
    nomes.append(input())
    entrada = input().split()
    if len(entrada) <= 2:
        if len(entrada) == 1:
            nota2 = 0
            nota1 = float(entrada[0])
            media = (nota2 + nota1) / 2
        else:
            nota1 = float(entrada[0])
            nota2 = float(entrada[1])
            media = (nota2 + nota1) / 2
    elif len(entrada) == 3:
        nota1 = float(entrada[0])
        nota2 = float(entrada[1])
        nota3 = float(entrada[2])
        media = (nota3 + nota2 + nota1) / 3
    elif len(entrada) == 4:
        entrada[0] = float(entrada[0])
        entrada[1] = float(entrada[1])
        entrada[2] = float(entrada[2])
        entrada[3] = float(entrada[3])
        if min(entrada) == entrada[3]:
            nota1 = entrada[0]
            nota2 = entrada[1]
            nota3 = entrada[2]
            media = (nota3 + nota2 + nota1) / 3
        elif min(entrada) == entrada[2]:
            nota1 = entrada[0]
            nota2 = entrada[1]
            nota3 = entrada[3]
            media = (nota3 + nota2 + nota1) / 3
        elif min(entrada) == entrada[1]:
            nota1 = entrada[0]
            nota2 = entrada[2]
            nota3 = entrada[3]
            media = (nota3 + nota2 + nota1) / 3
        elif min(entrada) == entrada[0]:
            nota1 = entrada[1]
            nota2 = entrada[2]
            nota3 = entrada[3]
            media = (nota3 + nota2 + nota1) / 3
    medias.append(media)
    
for i in range(n):
    print(f'{nomes[i]}: {medias[i]:.1f}')