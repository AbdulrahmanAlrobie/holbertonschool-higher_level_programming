#!/usr/bin/python3
"""Module defining the Student class with JSON serialization and
reloading capabilities."""


class Student:
    """Represents a student with basic attributes and supports
    serialization/deserialization."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dict of the Student instance.

        If attrs is a list of strings, only include those.
        Otherwise, return the full __dict__ copy.
        """
        if isinstance(attrs, list) and all(
                isinstance(a, str) for a in attrs):
            return {k: v for k, v in self.__dict__.items()
                    if k in attrs}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """Replace attributes of the Student instance using json dict."""
        for key, value in json.items():
            setattr(self, key, value)
