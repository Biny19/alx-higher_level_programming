#!/usr/bin/python3


class MyList(list):
    """MyList class inherits from a list class"""
    def print_sorted(self):
        """afunction that prints a sorted list"""
        print(sorted(self))
