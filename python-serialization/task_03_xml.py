#!/usr/bin/python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    # 1. Créer la racine
    root = ET.Element("data")

    # 2. Ajouter les éléments enfants
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    # 3. Écrire le XML dans le fichier
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}
    for child in root:
        result[child.tag] = child.text
    return result
