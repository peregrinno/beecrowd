dia1, dia2, dia3 = input().split()

dia1, dia2, dia3 = int(dia1), int(dia2), int(dia3)
if dia1 == 0 and dia2 == 0 and dia3 == 0:
    pass
else:
    if dia1 > dia2 and dia2 <= dia3:
        print(':)')
    
    elif dia1 < dia2 and dia2 >= dia3:
        print(':(')
    
    elif (dia1 < dia2 and dia2 < dia3) and dia2 - dia1 > dia3 - dia2:
        print(':(')
    
    elif (dia1 < dia2 and dia2 < dia3) and dia2 - dia1 <= dia3 - dia2:
        print(':)')
    
    elif (dia1 > dia2 and dia2 > dia3) and dia1 - dia2 > dia2 - dia3:
        print(':)')
    
    elif (dia1 > dia2 and dia2 > dia3) and dia1 - dia2 <= dia2 - dia3:
        print(':(')
     
    elif dia1 == dia2 and dia2 < dia3:
        print(':)')
    elif dia1 == dia2 and dia2 > dia3:
        print(':(')