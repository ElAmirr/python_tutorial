def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


x = int(input("please enter an integer: "))
fib(x)


# It is simple to write a function that returns a list of the numbers of the Fibonacci series, instead of printing it
def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


y = int(input("please enter a second integer: "))
print(fib2(y))
