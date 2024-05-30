#!/usr/bin/env python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")

def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

