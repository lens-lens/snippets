#DZIEDZICZENIE

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal): #dziedziczenie 1 linii
    def voice(self):
        print('Woof! Woof!')

class Wolf(Dog): #dziedziczenie 2 linii
    def hello(self):
        print('Jestem wilkiem!')
        super().voice() #to jest po to, aby voice z psa też się wliczał

class Cat(Animal): #dziedziczenie 1 linii
    def voice2(self):
        print('Meow, meow!')

dog = Dog('Luka', 5)
print(dog.name, dog.age)
dog.voice()

cat = Cat('Spajka', 10)
print(cat.name, cat.age)
cat.voice2()

wolf = Wolf('Michael', 9)
print(wolf.name, wolf.age)
wolf.hello()
