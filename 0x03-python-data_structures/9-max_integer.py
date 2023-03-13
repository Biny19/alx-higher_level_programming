#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    l = my_list[0]
    for num in range(len(my_list)):
        if my_list[i] > l:
            l = my_list[num]
    return (l)
