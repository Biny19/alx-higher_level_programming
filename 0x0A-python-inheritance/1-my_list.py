#!/usr/bin/python3
"""This module inherits from the list class"""


class MyList(list):
    """MyList class inherits from a list class"""
    def print_sorted(self):
        """afunction that prints a sorted list"""
        print(sorted(self))
