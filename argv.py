# import module argv from libary/package systeme
from sys import argv

if len(argv) == 2:
    print(f"hello, {argv[1]}")
else:
    print("hello, world")
# print alll arguments
for arg in argv:
    print(arg, end=' ')
