# w konsoli: pip install pytest
# SPRAWDZENIE, CZY FUNKCJA NAM COŚ WYŚWIETLA:

def get_triangle_field(base: int, height: int) -> float:
    # field = 0.5 * base * height
    print(0.5 * base * height)

def test_triangle_area(capsys): #capsys - odbiera to, co zwraca nasz program + błędy
    #given
    base = 10
    height = 8
    #when - field = get_triangle_area(base, heigh)
    get_triangle_field(base, height)
    out, err = capsys.readouterr() #zwraca tuple złożoną z output i error
    #then
    assert out == '40.0\n' #ważne! znak końca wiersza

#żeby sprawdzić czy testy przeszły - terminal: pytest .\test_show.py (będąc w odpow. folderze)
#żeby sprawdzić które testy przeszły - terminal: pytest .\test_show.py -vvv