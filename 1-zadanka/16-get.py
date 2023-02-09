dogs = {'Fafik':6, 'Pimpek':2}

name = input('Podaj imię psa: ')

print(dogs.get(name, f'{name} nie istnieje'))