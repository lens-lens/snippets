number = 1

while number < 6:
    print(number)
    number += 2

# to samo można zapisać w ten sposób:
for number in range(1,6,2):
    print(number)

# jeśli chcemy przerwać pętle np po liczbie 5:
for number in range(1,10):
    if number == 5:
        break
    print(number)

# jeśli chcemy nie pokazywać liczby np 5, ale nie kończyć pętli:
for number in range(1,10):
    if number == 5:
        continue
    print(number)
