import requests

class Employee:
    """a simple employee class"""

    raise_amount = 1.1

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay

    @property
    def email(self):
        return '{}{}@gmail.com'.format(self.first_name, self.last_name)

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def monthly_scheduele(self, month):
        response = requests.get(f'http://company.com/{self.last_name}/{mont}')
        if response.ok:
            return response.txt
        else:
            return 'bad response!'
 