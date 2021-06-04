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

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def create_new_employee(cls, emp_str):
        first_name, last_name, pay = emp_str.split('-')
        return cls(first_name, last_name, pay)


emp1 = Employee("amir", "othmani", 5000)
emp2 = Employee("rami", "gonzales", 100)

emp_str_1 = 'john-doe-7000'
emp_str_2 = 'steve-smith-3000'
emp_str_3 = 'jane-doe-9000'

new_emp_1 = Employee.create_new_employee(emp_str_1)
new_emp_2 = Employee.create_new_employee(emp_str_2)

print(new_emp_1.email)
print(new_emp_1.pay)

print(new_emp_2.full_name())

Employee.set_raise_amount(1.1)
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
