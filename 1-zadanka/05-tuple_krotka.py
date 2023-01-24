# niemutowalne, nie można zmieniać i dodawać elementów

names=('Lena', 'Zuzu', 'Klau') 
print(names)
print(names[1])
# zamiana na liczby
print(tuple(range(0,10)))

# przypisanie liczb do zmiennej i wyświetlanie liczb co 2
a=tuple(range(0,10,2))
print(a)
print(a[1])
print(a[-2])

for name in names:
    print(name)