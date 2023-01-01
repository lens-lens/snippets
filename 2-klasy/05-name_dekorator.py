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
    
    def go_down(self):
        self.semestr -= 1

    #jeśi chcę móc zawsze łatwo odnieść się do tej funkcji (metody) muszę zastosować DEKORATOR
    @property
    def year(self): #get_year zamieniam wtedy na year
        return ceil(self.semestr/2)

michael = TheOffice(first_name='Michael', last_name='Scott')
print('Semestr', michael.semestr)

michael.go_higher()
print('Semestr', michael.semestr)
print('Rok', michael.year) #tutaj też zmieniam i usuwam ()