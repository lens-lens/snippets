with open('1-zadanka/tasks2.txt', 'w') as f:
    f.write('Test')
    # zeby w pliku txt pojawiało się tylko to, co chcemy, wpisujemy:
    f.seek(0) 
    f.write('R')