# złożone z dwóch składowych: keys, values

author = {
    'first_name' : 'Stephen',
    'last_name' : 'King'
}

print(author['first_name'])
print(author['last_name'])

# przejście po pętli (klucze i wartości)
for key in author:
    print(key, author[key])

# author.items() - tuple, author.keys() - klucze, author.values() - wartości
# przejście po pętli jako tuple
for item in author.items():
    print(item)

# wypisanie pętli w kolejności
for first_name, last_name in author.items():
    print(first_name, last_name)

# WYJĄTKI 
try:
    print(first_name['Stefan'])
except KeyError:
    print('Błędne imię')
