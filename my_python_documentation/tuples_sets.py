# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')
fruits2 = tuple(('Apples', 'Oranges', 'Grapes')) # usless

print(fruits, fruits2)

# Single value needs trailing comma
fruits3 = ('Apple')
fruits4 = ('Apple',)

print(fruits3, type(fruits3))
print(fruits4, type(fruits4))

# Get value
print(fruits[1]) # same as lists

# Can't change value
fruits[0] = 'Pears' # tuple objects can't support item assignment

# Delete tuple 
del fruits2 # name fruits2 is not defined it's no  longer defined 

# Get length
print(len(fruits))

# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set = {'Apples', 'Oranges', 'Grapes'}

# Check if in set
print('Apple' in fruits_set)

# Add to set
fruits_set.add('Grape')

#Remove from set
fruits_set.remove('Grape')

# Add duplicate
fruits_set('Apples') # didn't add apple twise (no duplicate members)

# Cleare set
fruits_set.cleare()

print(fruits_set) # empty set nothing in it

# Delete set
del fruits_set # name fruits_set is not defined
