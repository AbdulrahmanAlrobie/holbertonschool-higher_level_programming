#!/usr/bin/python3
"""Module containing a function to read a text file and print its content."""

def read_file(filename=""):
    """Reads a UTF-8 text file and prints its content to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")