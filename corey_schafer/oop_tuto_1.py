class Employee:
    def __init__(self, first_name, last_name, email, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.pay = pay

    def full_name(self):
        return ('full name: {} {}'.format(self.first_name, self.last_name))


emp1 = Employee("amir", "othmani", "othmaniamir@gmail.com", 5000)
emp2 = Employee("rami", "gonzales", "em12@gmail.com", 100)

print(emp1)
print(emp2)
emp1.pay = "0$"
print(emp1.pay)
print(emp2.first_name)
print(emp1.full_name())
print(Employee.full_name(emp2))
