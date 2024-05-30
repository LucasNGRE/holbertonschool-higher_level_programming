#!/usr/bin/env python3
import csv
import json


def convert_csv_to_json(csv_filename, json_filename='data.json'):
    try:
        data = []
        with open(csv_filename, 'r') as csvf:
            csvReader = csv.DictReader(csvf)
            for row in csvReader:
                data.append(row)

        with open(json_filename, 'w') as jsonf:
            json.dump(data, jsonf)
        return True
    except FileNotFoundError:
        print(f"Erreur : le fichier {csv_filename} n'a pas été trouvé.")
        return False
    except Exception as e:
        print(f"Erreur lors de la conversion : {e}")
        return False
