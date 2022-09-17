while True:
    try:
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
        
        if t == 5:
            tab_uns = 0
        else:
            tab_uns = (t // 3)
            
        for i in range(t):
            for j in range(t):
                if i < meio and j == i or i > meio and j == i:
                    mat[i][j] = 2
                if j == sub:
                    mat[i][j] = 3
                    sub -= 1
                if tab_uns == 0:
                    if i > tab_uns and j > tab_uns and i < t-1 and j < t-1:
                        mat[i][j] = 1
                else:
                    if i > tab_uns-1 and j > tab_uns-1 and i < t-tab_uns and j < t-tab_uns:
                        mat[i][j] = 1
                if i == meio and j == meio:
                    mat[i][j] = 4
                print(mat[i][j], end="")
            print()
        print()
    except:
        break
