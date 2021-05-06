for i in range(5):
    print(i)
print("")

for i in range(5, 10):
    print(i)
print("")

for i in range(-1, -10, -1):
    print(i)
print("")

# To iterate over the indices of a sequence, you can combine range() and len() as follows:
a = ['amir', 'oumaima', 'skandar', 'habib', 'moufida']
for i in range(len(a)):
    print(i, a[i])
print("")

# object
print(range(10))
print("")

# list
print(list(range(2, 2)))
print("")
