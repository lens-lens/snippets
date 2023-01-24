from math import ceil 

class TheOffice:
    def __init__(self, first_name, last_name): 
        self.first_name = first_name
        self.last_name = last_name
        self.semestr = 1

    def hello(self):
        return self.first_name, self.last_name

    def go_higher(self):
        self.semestr += 1
    
    #jeśli istnieje ryzyko błędu w działaniu kodu, poprzez dodanie przez użytkownika nieprawidłowej zmiennej,
    #wtedy najlepiej zapisać wcześniej możliwe WYJĄTKI, aby nie pojawił się Error!
    def go_down(self):
        if self.semestr <= 1:
            raise Exception('Nie możesz tego wpisać')

    @property
    def year(self): 
        return ceil(self.semestr/2)

#a potem całość do wywołania umieścić w try:
try:
    michael = TheOffice(first_name='Michael', last_name='Scott')
    michael.go_down()
except Exception as message:
    print(message)