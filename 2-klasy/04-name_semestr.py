from math import ceil #ceil to funkcja, która zaokrągla wszystko w górę

class TheOffice:
    def __init__(self, first_name, last_name): 
        self.first_name = first_name
        self.last_name = last_name
        self.semestr = 1

    def hello(self):
        return self.first_name, self.last_name

    #jeśli chcemy założyć, że może być na wyższym lub niższym roku:
    def go_higher(self):
        self.semestr += 1
    
    def go_down(self):
        self.semestr -= 1

    def get_year(self):
        return ceil(self.semestr/2)

michael = TheOffice(first_name='Michael', last_name='Scott')
print('Semestr', michael.semestr)

#jesli chcę, żey był rok wyżej + podać rok:
michael.go_higher()
print('Semestr', michael.semestr)
print('Rok', michael.get_year())