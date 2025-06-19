#!/usr/bin/env python3
"""Module to convert CSV data to JSON format."""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Read a CSV file and write its contents as JSON to data.json.

    Returns True on success, False on failure (e.g., file not found).
    """
    try:
        with open(csv_filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            rows = [row for row in reader]
        with open('data.json', 'w', encoding='utf-8') as jsonfile:
            json.dump(rows, jsonfile)
        return True
    except Exception:
        return False
