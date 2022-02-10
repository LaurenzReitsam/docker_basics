from dataclasses import dataclass
from typing import Optional

import requests

FieldType = Optional[float]


@dataclass
class Payload:
    per_capita_crime_rate: FieldType = None
    prop_residential_land_zoned_for_lots: FieldType = None
    prop_non_retail_business_acres: FieldType = None
    dummy: FieldType = None
    nitric_oxides_concentration: FieldType = None
    avg_nr_rooms_per_dwelling: FieldType = None
    prop_build_prior_1940: FieldType = None
    distance_to_boston: FieldType = None
    ind_access_radial_highways: FieldType = None
    tax_rate: FieldType = None
    teacher_ratio: FieldType = None
    ratio_black_people: FieldType = None
    ratio_lower_status_population: FieldType = None


def send_request(pl: Payload):
    resp = requests.post("http://127.0.0.1:5000/", json=pl.__dict__)
    resp.raise_for_status()
    print(resp.json())


if __name__ == "__main__":
    pl = Payload()
    send_request(pl)
