# CAPITALIZE - zamienia piewszą literę na dużą
name = 'Jacek'
print(name.capitalize())
# UPPER - zamienia wszystkie litery na duże
print(name.upper())
# LOWER - zamienia wszystkie litery na małe
print(name.upper())
# STARTSWITH - sprawdza, czy string zaczyna się podaną literą
print(name.startswith('J'))
# L i R STRIP - usuwa literę z lewej lub prawej strony, sam STRIP usuwa zbędne spacje, jeśli są
print(name.lstrip('J'))
print(name.rstrip('k'))


# SPLIT - rozdziela zdanie na pojedyńcze słowa
channel = 'Jak nauczyć się programowania'
print(channel.split(' '))
# JOIN - łączy pojedyńcze słowa w zdanie
channel_2 = ' '
print(channel_2.join(['Jak', 'nauczyć', 'się', 'programowania']))


# Jeśli chcemy wyświetlić: pierwszą literę:
print(name[0])
# piersze dwie:
print(name[0:2])
# od trzeciej do końca:
print(name[2:])
