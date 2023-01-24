# mutowalne, można zmieniać i dodawać elementy

names = ['Lena', 'Zuzu', 'Klau']
print(names)

# zamiana ostatniego imienia
names[-1] = 'Ol'
print(names)
# dodanie imienia
names.append('Klau')
print(names)
# sortowanie listy
names.sort()
print(f'sortowanie: {names}')
# sortowanie listy od tyłu
names.sort(reverse=True)
print(names)

# sprawdzanie ile razy dane imię pojawiło się w liście
print(names.count('Lena'))

#wypisanie imion jedno pod drugim (przejście po pętli)
for name in names:
    print(name)

# usuwanie imienia
# names.remove('Zuzu')
# print(names)

# usuwanie całej listy
# names.clear()
# print(names)

# pytanie o ulubione owoce w kolejności
# fruits = []
# for i in range(0,5):
#     fruit = input(f'Jaki jest Twój {i} ulubiony owoc?')