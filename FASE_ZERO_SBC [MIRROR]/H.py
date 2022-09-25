t = int(input())
l_t_usado = [0]
max_andar = [1]
t_usado = 0

for i in range(t):
    
    c = float(input())
    
    if max(l_t_usado) > c:
        c_rest = c
        cont_andar = 1
        q_andar = cont_andar - 1 + (cont_andar * 2)
        
        while True:
            if c_rest >= q_andar:
                cont_andar += 1
                c_rest -= q_andar
                q_andar = cont_andar - 1 + (cont_andar * 2)
                t_usado += q_andar
            else:
                l_t_usado.append(t_usado)
                max_andar.append(cont_andar)
                t_usado = 0
                print(f'{cont_andar-1}')
                break
    else:
        c_rest = c - max(l_t_usado)
        cont_andar = max(max_andar)
        q_andar = cont_andar - 1 + (cont_andar * 2)
        
        while True:
            if c_rest >= q_andar:
                cont_andar += 1
                c_rest -= q_andar
                q_andar = cont_andar - 1 + (cont_andar * 2)
                t_usado += q_andar
            else:
                l_t_usado.append(t_usado)
                max_andar.append(cont_andar)
                t_usado = 0
                print(f'{cont_andar-1}')
                break
        
            
