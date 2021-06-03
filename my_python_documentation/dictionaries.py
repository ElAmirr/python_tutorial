# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# Create dict
person = {
    'first_name': 'Amir',
    'last_name': 'Othmani',
    'age': 23,
    'list': [1,2,3,4,5]
}

# Use constructor
person2 = dict(first_name='skandar', last_name='othmani', )

# Get value
print(person['first_name'])
print(person.get('last_name')) # get method
print(person.get('list'))
print(person.get('list')[1])

# Add key/value
person['phone'] = '92104649'

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())

#copy a dict 
person3 = person.copy()
person3['city'] = 'Boston'

print(person3)

# Remove item
del(person['age'])
person.pop('phone')

# Clear 
person.clear() # empty dict {} 

# Get length
print(len(person3))

# List of dict
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'salah', 'age': 27}
]

print(people)
print(people[0]['name']) #give the dict '0' with specefic field 'name'

print(person, type(person))
