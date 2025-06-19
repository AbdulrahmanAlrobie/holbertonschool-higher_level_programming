#!/usr/bin/env python3
"""Module for XML serialization and deserialization of Python dictionaries."""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dict to XML and save it to filename."""
    root = ET.Element('data')
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    with open(filename, 'w', encoding='utf-8') as xmlfile:
        tree.write(xmlfile, encoding='unicode')


def deserialize_from_xml(filename):
    """Read XML from filename and return a Python dict."""
    tree = ET.parse(filename)
    root = tree.getroot()
    result = {}
    for child in root:
        result[child.tag] = child.text
    return result
