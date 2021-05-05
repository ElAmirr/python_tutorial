# If/ Else conditions are used to decide to do something based on something being true or false

x = 10
y = 5

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values
# if/elif/else

if x > y:
    print(f'{x} is greater than {y}')
elif x == y:
    print(f'{x} is equal to {y}')
else:
    print(f'{y} is greater than {x}')

# nested if 
if x > 2:
    if x < 10:
        print(f'{x} is greater than 2 and less than 10')

# Logical operators (and, or, not) - Used to combine conditional statements
if x > 2 and x < 10:
        print(f'{x} is greater than 2 and less than 10')




# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object
numbers = [1, 2, 4, 10]

if x in numbers:
    print(x in numbers) # return True

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

if x is not y:
    print(x is not numbers)