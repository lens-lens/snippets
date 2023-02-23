# CLASS VARIABLES - raise_amount
# INSTANCE VARIABLES - self.nazwa=

class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Michael', 'Scott', 5000)
emp_2 = Employee('Holly', 'Flax', 6000)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

#TODO nadpisać wartość raise_amount:
Employee.raise_amount = 1.05

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)