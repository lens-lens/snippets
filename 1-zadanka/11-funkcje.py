def calculate_sum(a, b, c=10):
    return a+b+c

result = calculate_sum(2,2,2)
print ('Wynikiem funkcji jest', result)


#AKTUALIZACJA-DODATEK:
#Z YT CORY'EGO:
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Math', 'Art', name='Lena', age=27)

# to samo mozna zapisać w ten sposób:
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Math', 'Art']
info = {'name': 'Lena', 'age': 27}

student_info(*courses, **info)