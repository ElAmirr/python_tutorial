try:
    number = int(input("enter an number\n"))
    print(f"the user enter: {number}")
    answer = 10/0
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("invalid input")
