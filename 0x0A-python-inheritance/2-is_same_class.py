#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """checks if the type of the object is equal to the specified class. 
    If they are equal, it returns True, otherwise it returns False."""
    if type(obj) == a_class:
        return True
    return False
