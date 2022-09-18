t = int(input())

cases = []
for i in range(t):
    s, r = input().split(" ")
    if s == 'tesoura' and r == 'papel':
        cases.append("Bazinga!")
    elif s == 'papel' and r == 'tesoura':
        cases.append("Raj trapaceou!")
    elif s == 'papel' and r == 'pedra':
        cases.append("Bazinga!")
    elif s == 'pedra' and r == 'papel':
        cases.append("Raj trapaceou!")
    elif s == 'pedra' and r == 'lagarto':
        cases.append("Bazinga!")
    elif s == 'lagarto' and r == 'pedra':
        cases.append("Raj trapaceou!")
    elif s == 'lagarto' and r == 'Spock':
        cases.append("Bazinga!")
    elif s == 'Spock' and r == 'lagarto':
        cases.append("Raj trapaceou!")
    elif s == 'Spock' and r == 'tesoura':
        cases.append("Bazinga!")
    elif s == 'tesoura' and r == 'Spock':
        cases.append("Raj trapaceou!")
    elif s == 'tesoura' and r == 'lagarto':
        cases.append("Bazinga!")
    elif s == 'lagarto' and r == 'tesoura':
        cases.append("Raj trapaceou!")
    elif s == 'lagarto' and r == 'papel':
        cases.append("Bazinga!")
    elif s == 'papel' and r == 'lagarto':
        cases.append("Raj trapaceou!")
    elif s == 'papel' and r == 'Spock':
        cases.append("Bazinga!")
    elif s == 'Spock' and r == 'papel':
        cases.append("Raj trapaceou!")
    elif s == 'Spock' and r == 'pedra':
        cases.append("Bazinga!")
    elif s == 'pedra' and r == 'Spock':
        cases.append("Raj trapaceou!")
    elif s == 'pedra' and r == 'tesoura':
        cases.append("Bazinga!")
    elif s == 'tesoura' and r == 'pedra':
        cases.append("Raj trapaceou!")
    elif s == 'pedra' and r == 'pedra':
        cases.append("De novo!")
    elif s == 'papel' and r == 'papel':
        cases.append("De novo!")
    elif s == 'tesoura' and r == 'tesoura':
        cases.append("De novo!")
    elif s == 'lagarto' and r == 'lagarto':
        cases.append("De novo!")
    elif s == 'Spock' and r == 'Spock':
        cases.append("De novo!")
    
for i in range(t):
    print(f'Caso #{i+1}: {cases[i]}')
