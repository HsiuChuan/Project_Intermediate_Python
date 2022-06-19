"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""
import csv
import json
import datetime

def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output row
    corresponds to the information in a single close approach from the `results`
    stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    fieldnames = ('datetime_utc', 'distance_au', 'velocity_km_s', 'designation', 'name', 'diameter_km', 'potentially_hazardous')
    # TODO: Write the results to a CSV file, following the specification in the instructions.
    with open(filename, 'w') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in results:
            datetime_utc = row.time
            distance_au = row.distance
            velocity_km_s = row.velocity
            designation = row._designation
            name = row.neo.name
            diameter_km = row.neo.diameter if row.neo.diameter is not None else 'nan'
            potentially_hazardous = 'True' if row.neo.hazardous == 'Y' else 'False'

            data = [datetime_utc, distance_au, velocity_km_s, designation, name, diameter_km, potentially_hazardous]
            writer.writerow(dict(zip(fieldnames, data)))
        


def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output is a
    list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """

    # TODO: Write the results to a JSON file, following the specification in the instructions.
    data = []
    for row in results:
        datetime_utc = datetime.datetime.strftime(row.time, "%Y-%m-%d %H:%M")
        distance_au = row.distance
        velocity_km_s = row.velocity
        designation = row._designation
        name = row.neo.name
        diameter_km = row.neo.diameter if row.neo.diameter is not None else 'nan'
        potentially_hazardous = bool(1) if row.neo.hazardous == 'Y' else bool(0)
            
        data.append(
            {
                "datetime_utc": datetime_utc,
                "distance_au": distance_au, 
                "velocity_km_s": velocity_km_s,
                "neo":
                {
                    "designation": designation,
                    "name": name,
                    "diameter_km": diameter_km, 
                    "potentially_hazardous": potentially_hazardous
                }
            }
        )

    with open(filename, 'w') as outfile:        
        json.dump(data, outfile, indent=2)