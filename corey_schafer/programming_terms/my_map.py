def square(x):
    return x ** 2


def my_map(func, arg_list):
    result = []
    for elm in arg_list:
        result.append(func(elm))
    return result


squares = my_map(square, [1, 2, 5, 6])
print(squares)
