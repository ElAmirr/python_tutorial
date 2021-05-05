# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces


# Create function
def sayHello(name): # name is a parametre
    print(f'Hello {name}')


sayHello('Amir') # calling sayHello function

# Return value
def getSum(num1, num2):
    total = num1 + num2
    return total

sum = getSum(3, 4)
print(sum)

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum = lambda num1, num2 : num1 + num2 # return num1 +num2 and assignet to getSum

print(getSum(10, 2))
