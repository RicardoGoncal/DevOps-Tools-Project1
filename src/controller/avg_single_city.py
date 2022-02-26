import pandas as pd
import os
import json

def avg_single_city(city):
    
    param = city

    target = os.getcwd() + '/files/dataset.csv'

    df = pd.read_csv(target)

    groupby_avg = df.groupby(['city']).median()

    avg_value_city = groupby_avg['car_value']

    print(avg_value_city)
    print(avg_value_city[param])

    result = 'The average value of cars of the City: ' + str(param) + ', is: ' + str(avg_value_city[param])

    response = result

    return response