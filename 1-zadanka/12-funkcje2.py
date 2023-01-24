def calculate_sum(a, b, c=10):
    return a+b+c

arguments = [1,2,3]

result = calculate_sum(arguments[0],5)
print(result)
result = calculate_sum(arguments[1],5)
print(result)
result = calculate_sum(arguments[2],5)
print(result)

# przejście po pętli

for argument in arguments:
    result = calculate_sum(argument,5)
    print(result)