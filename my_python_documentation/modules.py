# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# Core modules

# import all method from the module datime
import datetime 
today = datetime.date.today()
print(today)

# or only import the method date from datetime module
from datetime import date 
today = date.today()
print(today)

# import all method from time
import time
timestamp = time.time()
print(timestamp)

# or import only time methode from time module
from time import time
timestamp = time()
print(timestamp)

'''
install module with pip3 globaly:
pip3 install camelcase 
to see what i install type:
pipe freeze

'''
# Pip modules
from camelcase import CamelCase
c = CamelCase()
print(c.hump('hello world'))

# Import custom module
import validator
from validator import validate_email
email = 'test@test.com'
if validate_email(email):
    print('Eamil is valid')
else:
    ('Eamil is bad')