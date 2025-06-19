#!/usr/bin/env python3
"""Basic serialization module: serialize a Python dictionary to JSON and
deserialize JSON back to a Python dictionary."""

import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary to a JSON file (overwrite if exists)."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load a JSON file and deserialize it to a Python dictionary."""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
