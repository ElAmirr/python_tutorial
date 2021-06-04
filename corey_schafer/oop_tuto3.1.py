import datetime


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

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp1 = Employee("amir", "othmani", 5000)
emp2 = Employee("rami", "gonzales", 100)

my_date = datetime.date(2016, 7, 19)
print(Employee.is_workday(my_date))
