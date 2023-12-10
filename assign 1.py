# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 09:48:14 2023

@author: Shashank
"""

import pandas as pd
import numpy as np

def generate_car_matrix(dataset):
    
    df = pd.read_csv('dataset-1.csv')

    # Pivot the DataFrame to get the desired matrix
    matrix = df.pivot(index='id_1', columns='id_2', values='car').fillna(0)

    # Replace diagonal values with 0
    for col in matrix.columns:
        matrix.loc[col, col] = 0

    return matrix


result_matrix = generate_car_matrix('dataset-1.csv')
print(result_matrix)
