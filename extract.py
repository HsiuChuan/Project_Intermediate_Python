"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    # TODO: Load NEO data from the given CSV file.
    neos = []
    with open(neo_csv_path, 'r') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            pdes = row['pdes']
            name = row['name'] if row['name'] else None
            pha = True if row['pha'] == 'Y' else False
            diameter = float(row['diameter']) if row['diameter'] else None
            neo = NearEarthObject(designation=pdes, name=name, diameter=diameter, hazardous=pha)
            neos.append(neo)
    return neos

    



def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """

    # TODO: Load close approach data from the given JSON file.
    approaches = list()
    with open(cad_json_path, 'r') as infile:
        contents = json.load(infile)
    for ca in contents['data']:
        des = ca[0] if ca[0] is not None else None
        cd = ca[3] if ca[3] is not None else None
        dist = float(ca[4]) if ca[4] else float(0.0)
        v_rel = float(ca[7]) if ca[7] else float(0.0)
        approach = CloseApproach(designation=des, time=cd, distance=dist, velocity=v_rel)
        approaches.append(approach)
    return approaches

