import csv
import json

def csv_vers_json(eleves_valides_csv, eleves_valides_json):

    data = []

    with open(eleves_valides_csv, "r") as csv_file:

        lecteur = csv.DictReader(csv_file)

        for ligne in lecteur:
            data.append(ligne)

    with open(eleves_valides_json, "w") as json_file:

        json.dump(data, json_file, indent=4)

