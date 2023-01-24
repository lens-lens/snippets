# w konsoli: pip install pytest
# SPRAWDZENIE, CZY FUNKCJA NAM COŚ ZWRACA:

def is_adult(age: int) -> bool:
    #funkcja przyjmuje wartość 'wiek', która jest liczbą całkowitą, a otrzymujemy z niej prawdę/fałsz
    return age >= 18

def test_is_adult():
    #given - opisujemy to co mamy, co będzie nam służylo do przygotowania testu
    age = 18
    #when - opisujemy to co się wydarza, co daje nam wynik
    result = is_adult(age)
    #then - sprawdzamy poprawność wyniku
    assert result
    assert is_adult(20)
    #assert - jeżeli to co jest zanim będzie prawdą to test przejdzie 

def test_isnt_adult():
    assert not is_adult(17)
    assert not is_adult(8)

#żeby sprawdzić czy testy przeszły - terminal: pytest .\test_return.py (będąc w odpow. folderze)
#żeby sprawdzić które testy przeszły - terminal: pytest .\test_return.py -vvv