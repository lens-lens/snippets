# 2* ('1. Pokaż zadania')
user_choice = 0

# 3: ('1. Pokaż zadania') tworzymy listę zadań
tasks = []
tasks.append('Posprzątać mieszkanie')
tasks.append('Zrobić pranie')
tasks.append('Zostać programistką xd')

# 4: ('1. Pokaż zadania') tworzymy funkcję do listy zadań, żeby przypisywało indeksy numeryczne do zadań (aby użytkownik mógł wybrać liczbę zadania do usunięcia)
def show_tasks():
    task_index = 0
    for task in tasks:
        print(task + '[' + str(task_index) + ']')
        # żeby indeksy rosły o 1 liczbę, a nie wszystkie były zerem:
        task_index +=1

# 5: ('2. Dodaj zadanie') z "if user_choice == 2" robimy funkcję
def add_task():
    task = input('Wpisz treść zadania: ')
    tasks.append(task)
    print('Dodano zadanie')

#6: ('3. Usuń zadanie')
def delete_task():
    task_index = int(input('Podaj numer zadania do usunięcia: '))
    if task_index < 0 or task_index > len(tasks) - 1:
        print('Zadanie o tym numerze nie istnieje')
    else:
        tasks.pop(task_index)
        print('Usunięto zadanie')

#7: ('4. Zapisz zmiany do pliku')
def save_tasks_to_file():
    file =  open('zadanka/tasks.txt', 'w')
    for task in tasks:
        file.write(task + '\n')
    file.close()

#7: ('4. Zapisz zmiany do pliku') jeśli chcemy, żeby zadania w pliku txt były z listy to do
def load_tasks_from_file():
    file = open('zadanka/tasks.txt', "r")
    for line in file.readlines():
        tasks.append(line.strip())
    file.close()

load_tasks_from_file()

# 0:
while user_choice != 5:
    if user_choice == 1:
        show_tasks()

    if user_choice == 2:
        add_task()

    if user_choice == 3:
        delete_task()

    if user_choice == 4:
        save_tasks_to_file()


# 1: jeśli chcemy stworzyć przerwę pomiędzy liniami tekstu, musimy wpisać print()
    print()
    print('1. Pokaż zadania')
    print('2. Dodaj zadanie')
    print('3. Usuń zadanie')
    print('4. Zapisz zmiany do pliku')
    print('5. Wyjdź')

# 2: tworzymy użytkownika, który wybiera co chce zrobić po liczbie, a skoro to liczba to musimy przed nawiasem wstawić int
    user_choice = int(input('Wybierz liczbę: '))
    print()