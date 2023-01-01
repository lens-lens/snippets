class TheOffice:
    def __init__(self, first_name, last_name): 
        self.first_name = first_name
        self.last_name = last_name

    def hello(self):
        return self.first_name, self.last_name #return jest do zapisu w bazie danych

michael = TheOffice(first_name='Michael', last_name='Scott')
print(michael.first_name, michael.last_name)

holly = TheOffice(first_name='Holly', last_name='Flax')
print(holly.first_name, holly.last_name)
