# search for prime number from 2 to 9
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, "equals", x, "*", n//x)
            break
    else:
        print(n, " is a prime")

for num in range(2, 10):
    if num % 2 == 0:
        print('found an even number', num)
# go directly to the next number in for loop
        continue
    print('found a number', num)
