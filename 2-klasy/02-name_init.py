class TheOffice:
    def __init__(self, first_name, last_name): #first_name i last_name to zmienne obiektu
        self.first_name = first_name
        self.last_name = last_name
        #self - specjalna zmienna, która wskazuje na ten obiekt, w którym się znajdujemy

michael = TheOffice(first_name='Michael', last_name='Scott')
print('First name: ', michael.first_name)
print('Last name: ', michael.last_name)

holly = TheOffice(first_name='Holly', last_name='Flax')
print('First name: ', holly.first_name)
print('Last name: ', holly.last_name)