#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    orlist = list(a_dictionary.keys())
    orlist.sort()
    for i in orlist:
        print("{}: {}".format(i, a_dictionary.get(i)))
