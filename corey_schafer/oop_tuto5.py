
class Employee:

    num_of_emp = 0
    raise_amount = 1.04

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.email = first_name + '' + last_name + '@gmail.com'
        self.pay = pay

        Employee.num_of_emp += 1

    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return "employee('{}', '{}', {})".format(self.first_name, self.last_name, self.pay)

    def __str__(self):
        return "{} - {}".format(self.full_name(), self.email)

    # this is how telling them how to add these employees together
    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.full_name())


emp1 = Employee("amir", "othmani", 5000)
emp2 = Employee("rami", "gonzales", 100)

print(emp1)

print(repr(emp1))
print(len(emp1))

print(emp1.__repr__())
print(emp2.__str__())
print(emp1.__len__())

# special method with 2 attribut
print(emp1 + emp2)
