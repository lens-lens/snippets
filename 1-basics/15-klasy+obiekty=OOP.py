class Human:
    # init to konstruktor klasy, uruchamiany w pierszej kolejności
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # można też napisać tak:
        # print(self.whatsyourname())

    # żeby odnieść się do klasy trzeba podać w nawiasie (self), a następnie argumenty, które chcemy aby się wywoływały 
    def whatsyourname(self, powitanie = 'Hello'):
        return powitanie + ' my name is ' + self.name + ' mam ' + self.age + ' lat' 

object = Human('Lena', '27')
print(object.name)
print(object.whatsyourname('Elo')) # można zmienić np przedstawienie się, podając inne w tym nawiasie

# można stworzyć object2 w tej samej klasie, tylko trzeba mu nadać osobne imię
object2 = Human('Jacek', '28')
print(object2.whatsyourname())