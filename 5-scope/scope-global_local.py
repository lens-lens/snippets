#LEGB - Local, Enclosing, Global, Built-in
#GLOBAL SCOPES: nazwy zdefiniowane w tym zakresie są dostępne dla całego kodu
#LOCAL SCOPES: nazwy zdefiniowane w tym zakresie są dostępne tylko dla kodu w zakresie

#TODO 1: print local y:
# x = 'global x'
# def test():
#     y = 'local y'
#     print(y)
# test()

#TODO 2: print global x:
# x = 'global x'
# def test():
#     y = 'local y'
#     print(x)
# test()

# print(y) --> NameError: name 'y' is not defined
# print(x) --> global x

#TODO 3: print inside local x & outside global x:
# x = 'global x'
# def test():
#     x = 'local x'
#     print(x)
# test()
# print(x)

#TODO 4: print inside & outside local x:
# def test():
#     global x
#     x = 'local x'
#     print(x)
# test()
# print(x)

#TODO 5: print local z:
def test(z):
    x = 'local x'
    print(z)
test('local_z')

# print(z) --> NameError: name 'z' is not defined