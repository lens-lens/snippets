#ZAD. Przygot. klasę bank. Klasa powinna mieć możliwość wpłacania i wypłacania.
#W chwili inicjalizacji bank powinien mieć puste saldo.

class Bank:
    def __init__(self):
        self.amount = 0
    
    def add_money(self, money: int):
        self.amount += money

    def remove_money(self, money: int):
        self.amount -= money

        return money

class TestBank:
    def test_create_bank(self): #sprawdza, czy udało się poprawnie stworzyć klasę bank
        bank = Bank()
        assert bank.amount == 0 #sprawdza, czy bank ma puste saldo
        assert isinstance(bank, Bank) #sprawdza, czy dany obiekt należy do danej klasy
        #pierwszy arg: nazwa obiektu, drugi arg: klasa obiektu

    def test_add_money(self): #wpłacanie pieniędzy
        #given
        bank = Bank()
        #when
        bank.add_money(100)
        #then
        assert bank.amount == 100

    def test_remove_money(self): #wypłacanie pieniędzy
        #given
        bank = Bank()
        bank.add_money(100)
        #when
        money = bank.remove_money(30)
        #then
        assert money == 30
        assert bank.amount == 70

#żeby sprawdzić czy testy przeszły - terminal: pytest .\test_bank.py (będąc w odpow. folderze)
#żeby sprawdzić które testy przeszły - terminal: pytest .\test_bank.py -vvv