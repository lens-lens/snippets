#LEGB - Local, Enclosing, Global, Built-in
#ENCLOSING:
#inner - funkcja lokalna, dostępna tylko wewnątrz outer

#TODO: print inner & outer x:
def outer():
    x = 'outer x'

    def inner():
        x = 'inner x'
        print(x)

    inner()
    print(x)

outer()