# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class (with method)
class User:
    # Constructor
    def __init__(self, name, email, age): # property
        self.name = name
        self.email = email
        self.age = age

    def greeting(self): # create a method within(inside)the class 
        return f'My name is {self.name} and I am {self.age}' # to acess any of these properties from any method within(inside) the class we need to use that 'self' keyword

    def has_birthday(self):
        self.age += 1

# Extand class
class Customer(User): # extend User we passed as a parameter
    # Constructor
    def __init__(self, name, email, age): # property
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0
    def set_balance(self, fbalance):
        self.balance = balance
    def greeting(self): # even if we don't define greeting in 'Customer' class we still call 'greeting' because 'Customor' class extend 'User' class  
        return f'My name is {self.name} and I am {self.age} and my balanse is {self.balance}'
# Init user object
brad = User('Brad Traversy', 'amirothmani41@gmail.com', 23) #brad is a user object
# Init customer object
janet = Customer('janet jonson', 'janet@yahoo.com', 23)
janet.set_balance(500)

brad.has_birthday() # add +1 to age property
print(brad.age) # acess any property age = self.age
print(brad.greeting()) # run a method