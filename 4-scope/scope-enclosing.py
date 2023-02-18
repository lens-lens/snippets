#LEGB - Local, Enclosing, Global, Built-in
#ENCLOSING:
#inner - funkcja lokalna, dostępna tylko wewnątrz outer

#TODO 1: print inner & outer x:
def outer():
    x = 'outer x'

    def inner():
        x = 'inner x'
        print(x)

    inner()
    print(x)

outer()

#TODO 2: print outer x:
# def outer():
#     x = 'outer x'

#     def inner():
#         nonlocal x
#         print(x)

#     inner()
#     print(x)

# outer()

#TODO 3: print inner & outer & global:
# x = 'global x'
# def outer():
#     x = 'outer x'

#     def inner():
#         x = 'inner x'
#         print(x)

#     inner()
#     print(x)

# outer()
# print(x)

#TODO 4: print global:
# x = 'global x'
# def outer():

#     def inner():
#         print(x)

#     inner()
#     print(x)

# outer()
# print(x)