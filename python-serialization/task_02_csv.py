#!/usr/bin/python3

import csv
import json


def convert_csv_to_json(filename_csv):
    try:
        with open(filename_csv, "r", encoding="utf-8") as fcsv:
            data_list = list(csv.DictReader(fcsv))
        with open("data.json", "w", encoding="utf-8") as fjson:
            json.dump(data_list, fjson)
        return True
    except (OSError, csv.Error, json.JSONDecodeError):
        return False
