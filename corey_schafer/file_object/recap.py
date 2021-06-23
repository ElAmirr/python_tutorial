print("first methode to reade file")
with open('test.txt', 'r') as rf:
    f_contents = rf.read()
    print(f_contents)

print("second methode to reade file")
with open('test.txt', 'r') as rf:
    size_to_read = 10
    f_contents = rf.read(size_to_read)
    while len(f_contents) > 0:
        print(f_contents)
        f_contents = rf.read(size_to_read)

print("third methode to reade file")
with open('test.txt', 'r') as rf:
    for line in rf:
        print(line)

print("fourth methode to reade file")
with open('test.txt', 'r') as rf:
    f_contents = rf.readline()
    while len(f_contents) > 0:
        print(f_contents)
        f_contents = rf.readline()


print("first method to copy past a text")
with open('test.txt', 'r') as rf:
    with open('copy.txt', 'w') as wf:
        size_to_read = 10
        f_contents = rf.read(size_to_read)
        while len(f_contents) > 0:
            wf.write(f_contents)
            f_contents = rf.read(size_to_read)

print("second methode to copy past a text")
with open('test.txt', 'r') as rf:
    with open('copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

# to copy past an image just add rb and wb b:binary
