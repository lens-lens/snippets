# żeby funkcja mogła podebrać dowolną ilość argumentów pozycyjnych, gdy np
# 1000 = pensja pracownika
# 0.1 = dodatek stażowy
# 0.25 = sprzedaż
# 0.3 = stanowisko

def calculate_salary(*args, base:float) -> float:
    salary = base
    for arg in args:
        salary = salary + (salary * arg)
    return salary

print(calculate_salary(0.1, 0.25, 0.3, base=1000))
print(calculate_salary(0.1, base=1000))