import sys
import timeit

listee = [1, 2, 'a', 'b', "amir", "skandar"]
tuplee = (1, 2, 'a', 'b', "amir", "skandar")

size_list = sys.getsizeof(listee)
size_tuple = sys.getsizeof(tuplee)

print(f"the size of list {size_list}")
print(f"the size of tuple {size_tuple}")

time_list = timeit.timeit(
    stmt="[1, 2, 'a', 'b', 'amir', 'skandar']", number=100000000)
time_tuple = timeit.timeit(
    stmt="(1, 2, 'a', 'b', 'amir', 'skandar')", number=100000000)

print(f"the time to build list = {time_list}s")
print(f"the time to build tuple = {time_tuple}s")
