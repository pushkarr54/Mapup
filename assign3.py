# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 11:26:53 2023

@author: Shashank
"""

import pandas as pd
import numpy as np

def get_bus_indexes(dataset):
    
    df = pd.read_csv('dataset-1.csv')

    
    bus_mean = df['bus'].mean()

    # Find indices where 'bus' values are greater than twice the mean
    bus_indexes = df[df['bus'] > 2 * bus_mean].index.tolist()
    bus_indexes.sort()  # Sort in ascending order

    return bus_indexes


result_indexes = get_bus_indexes('dataset-1.csv')
print(result_indexes)
