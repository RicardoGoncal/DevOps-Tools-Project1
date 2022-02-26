import pandas as pd
import os
import json

def avg_single_car_make(car_make):
    
    param = car_make

    target = os.getcwd() + '/files/dataset.csv'

    df = pd.read_csv(target)

    groupby_avg = df.groupby(['car_make']).median()

    avg_value_car_make = groupby_avg['car_value']

    print(avg_value_car_make)
    print(avg_value_car_make[param])

    result = 'The Avarage of car_make: ' + str(param) + ', is: ' + str(avg_value_car_make[param])

    response = result

    return response