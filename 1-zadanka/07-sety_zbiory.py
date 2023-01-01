# niemutowalne, nie przyjmują kolejności, nie pokazują duplikatów

team_a = {'Michael', 'Stanley', 'Kelly', 'Michael'}
team_b = {'Kevin', 'Michael','Pam', 'Kelly'}

# operacje na zbiorach (setach)
print('SUMA', team_a | team_b)
print('CZĘŚĆ WSPÓLNA', team_a & team_b)
print('RÓŻNICA SYMETRYCZNA', team_a ^ team_b)
print('A-B', team_a - team_b)
print('B-A', team_a - team_b)

# dodawanie setu do listy
list_a = ['Dwight', 'Jim']
list_a.extend(team_a)
print(list_a)