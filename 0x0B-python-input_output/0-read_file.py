#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    """A function that prints the contents of a UTF-8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
