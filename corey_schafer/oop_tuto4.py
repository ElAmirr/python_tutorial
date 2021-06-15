
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


class Developer(Employee):
    raise_amount = 1.05

    def __init__(self, first_name, last_name, pay, programming):
        super().__init__(first_name, last_name, pay)
        self.programming = programming


class Manager(Employee):
    def __init__(self, first_name, last_name, pay, employees=None):
        super().__init__(first_name, last_name, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        for emp in self.employees:
            print('---->', emp.full_name())


emp1 = Employee("mehrez", "msatya", 200)
dev1 = Developer("amir", "othmani", 50000, "python")
dev2 = Developer("rami", "gonzales", 100, "c++")
man1 = Manager("skandar", "othmani", 5000)
print(dev1.email)
print(dev2.email)

print(dev1.pay)
dev1.apply_raise()
print(dev1.pay)

print(dev1.programming)

# print(man1.print_employees())
man1.add_emp(dev1)
man1.add_emp(dev2)
man1.add_emp(emp1)
print(man1.print_employees())
man1.remove_emp(dev1)
print(man1.print_employees())
