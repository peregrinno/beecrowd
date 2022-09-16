while True:
    t = int(input())
    mat = []
    linhas = []
    for l in range(t):
        for c in range(t):
            linhas.append(0)
        mat.append(linhas)
        linhas = []

    meio = t // 2
    sub = t - 1 
    for i in range(t):
        for j in range(t):
            if i < meio and j == i or i > meio and j == i:
                mat[i][j] = 2
            if j == sub:
                mat[i][j] = 3
                sub -= 1
            if meio == 2 and t - 1 > i > 0 :
                for k in range(meio-1,meio+2):
                    mat[i][k] = 1
            elif meio > 2 and meio // 2 > i > meio * 2:
                for k in range(meio//2,(meio//2)*2):
                    mat[i][k] = 1
                    
            if i == meio and j == meio:
                mat[i][j] = 4
                
            print(mat[i][j], end=" ")
        print()

            
