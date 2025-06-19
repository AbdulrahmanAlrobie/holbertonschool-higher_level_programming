#!/usr/bin/python3
"""Module for JSON serialization of Python objects."""

import json


def to_json_string(my_obj):
    """Return the JSON representation of a Python object (string)."""
    return json.dumps(my_obj)
