from typing import Iterable

def print_items(items: Iterable):
    for item in items:
        print(item)

# print_items([1,2,3])
# print_items({4, 5, 6})
# print_items({"A": 1, "B": 2, "C": 3})


def double_value(value):
    return print(value + value)


double_value(5)
double_value('abc')
double_value([1,2,3])