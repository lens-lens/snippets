# w+ (WRITE):
file = open('countries_and_capitals.txt', 'w+')

countries_and_capitals = {'Poland': 'Warsaw', 'Spain': 'Madryt', 'Paris': 'France'}

for country, capital in countries_and_capitals.items():
    file.write(country + '-' + capital + '\n')

file.close()

# r (READ):
file = open('countries_and_capitals.txt')

for line in file.readlines():
    print(line.strip())

#!!! jeśli chcę WYWOŁAĆ funkcję to muszę na końcu printa dać ()
# to samo mogę zrobić w ten sposób:
# for line in file.readlines():
#     a = line.strip
#     print(a())