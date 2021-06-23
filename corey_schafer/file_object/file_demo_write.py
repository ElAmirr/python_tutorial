# file objects

with open('test.txt', 'r') as rf:
    with open('test_copy', 'w') as wf:
        for line in rf:
            wf.write(line)
