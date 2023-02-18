# OPCJA 1: zapisując kod w ten sposób trzeba zamknąć go poprzez CLOSE
# f = open('1-zadanka/tasks.txt', 'r')
# print(f.name) #printuje ściezkę
# print(f.mode) #printuje tryb (r-read)
# f.close() 

# OPCJA 2:
with open('1-zadanka/tasks.txt', 'r') as f:
#wyświetli jedno pod drugim:
    # f_contents =  f.read() 
    # print(f_contents)

#wyświetli w liście:
    # f_contents =  f.readlines() 
    # print(f_contents)

#wyświetli pierwszą linijkę ściezki:
    # f_contents =  f.readline() 
    # print(f_contents, end='')

#wyświetli wszysttkie jedno pod drugim:
    # for line in f: 
    #     print(line, end='')

    size_to_read = 10
    f_contents = f.read(size_to_read) #miejsce w znakach
    print(f.tell()) #miejsce w bajtach (polski znak = 2B)

    while len(f_contents) > 0:
        print(f_contents, end='*')
        # print(f_contents, end='f{f.tell}') #mozna wyprintować z nr miejsca
        f_contents = f.read(size_to_read)

# print(f.closed) #nie potrzeba CLOSE, bo jest zamknięty automatycznie
