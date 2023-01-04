#ZAD. Przygot. funkcję, która będzie sortowała otrzymywaną listę imion:
#w kolejności alfabetycznej pierszej litery, 
#w kolejności alfabetycznej ostatniej litery, 
#według długości imienia.
import pytest 

def sort_by(names, first_letter=False, last_letter=False, length=False):
    if first_letter:
        names.sort()
    if last_letter:
        names.sort(key=lambda name: name[::-1])
    if length:
        names.sort(key=len)
    return names

class TestSort:
    @pytest.fixture
    def names(self):
        return ['Lena', 'Jacek', 'Zu', 'Klau']

    def test_sort(self, names): #dodajemy names po przecinku z funkcji pod dekoratorem @pytest.fixture, zamiast given
        #given
        # names = ['Lena', 'Jacek', 'Zu', 'Klau']
        #when
        sorted_names = sort_by(names, first_letter=True)
        #then
        assert sorted_names == ['Jacek', 'Klau', 'Lena', 'Zu']
        
    def test_reverse_sort(self, names): #dodajemy names po przecinku z funkcji pod dekoratorem @pytest.fixture, zamiast given
        #given
        # names = ['Lena', 'Jacek', 'Zu', 'Klau']
        #when
        sorted_names = sort_by(names, last_letter=True)
        #then
        assert sorted_names == ['Lena', 'Jacek', 'Zu', 'Klau']

    def test_by_length(self, names):
        #when
        sorted_names = sort_by(names, length=True)
        #then
        assert sorted_names == ['Zu', 'Lena', 'Klau','Jacek']

#żeby sprawdzić czy testy przeszły - terminal: pytest .\test_sort.py (będąc w odpow. folderze)
#żeby sprawdzić które testy przeszły - terminal: pytest .\test_sort.py -vvv