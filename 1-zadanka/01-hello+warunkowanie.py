first_name = input('Jak masz na imię?')
age = int(input ('Ile masz lat?'))
# print(first_name)
print(f'Hello{first_name}!')
print(f'Mam{age}lat') 

# WARUNKI
if first_name == 'Lena':
    print('Cześć Lena!')
else:
    # print('Miło mi Cię poznać!')
    print(f'Cześć {first_name}!')
    
if age >= 18:
    print('Jesteś pełnoletni!')
else:
    print('Jeszcze musisz poczekać')
    print(f'{18-age}lat')


# inny przykład WARUNKOWANIA
light = input('Jakie jest światło? (red, green, yellow')

if light == 'red':
    print('Czekaj!')
elif light == 'yellow':
    print('Przygotuj się')
elif light == 'green':
    print('Jedź!')
else:
    print('Niewłaściwa wartość')

