class Employee:

    num_of_emp = 0
    raise_amount = 1.04

    def __init__(self, first_name, last_name, email, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.pay = pay

        # use Employee.num_of_emp instead of self.num_of_emp
        Employee.num_of_emp += 1

    def full_name(self):
        return ('full name: {} {}'.format(self.first_name, self.last_name))

    def apply_raise(self):
        # use self.raise_amount instead of Employee.raise_amount
        self.pay = int(self.pay * self.raise_amount)


print("number of employee before contract: {}".format(Employee.num_of_emp))
emp1 = Employee("amir", "othmani", "othmaniamir@gmail.com", 5000)
emp2 = Employee("rami", "gonzales", "em12@gmail.com", 100)

print(emp1.__dict__)
print(emp2.__dict__)
print(Employee.__dict__)

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

print("after changing the value of raise_amount in emp1")
emp1.raise_amount = 1.05

print(emp1.__dict__)

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)

print("number of emolyee: {}".format(Employee.num_of_emp))
