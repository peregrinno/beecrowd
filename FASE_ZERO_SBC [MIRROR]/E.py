entrada = input().split()
estudantes = int(entrada[0])
litros = int(entrada[1])
consumo = int(entrada[2])
poder_producao = litros

consumo_t = (estudantes * consumo) / 1000
while consumo_t > litros:
    litros += poder_producao

print (f'{litros:.0f}')
