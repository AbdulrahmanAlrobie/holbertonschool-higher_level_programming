#!/usr/bin/python3
"""Module for JSON deserialization of strings to Python objects."""

import json


def from_json_string(my_str):
    """Return the Python object represented by a JSON string."""
    return json.loads(my_str)
