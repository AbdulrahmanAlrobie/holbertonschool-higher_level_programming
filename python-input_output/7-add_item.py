#!/usr/bin/python3
"""Script that adds all arguments to a Python list and saves it in a JSON file."""

import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """Load existing list, append CLI args, and save back to JSON file."""
    filename = "add_item.json"
    try:
        items = load_from_json_file(filename)
    except FileNotFoundError:
        items = []
    items.extend(sys.argv[1:])
    save_to_json_file(items, filename)


if __name__ == "__main__":
    main()
