from audioop import avg
import pandas as pd
import os
import json

def avg_car_make():
   
    target = os.getcwd() + '/files/dataset.csv'

    df = pd.read_csv(target)
    groupby_avg = df.groupby(['car_make']).median()

    avg_value_car_make = groupby_avg['car_value']

    transform_json = avg_value_car_make.to_json(orient="table")
    parsed = json.loads(transform_json)
    transform_json = json.dumps(parsed, indent=4)

    response = transform_json

    return response