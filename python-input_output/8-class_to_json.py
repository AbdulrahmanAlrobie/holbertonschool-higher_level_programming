#!/usr/bin/python3
"""Module for class-to-JSON conversion of object attributes."""

def class_to_json(obj):
    """Return the dictionary description of an object for JSON serialization."""
    return obj.__dict__
