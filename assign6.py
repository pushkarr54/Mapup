# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 11:39:40 2023

@author: Shashank
"""

import pandas as pd

def calculate_distance_matrix(dataset):
    # Read the dataset as a DataFrame
    df = pd.read_csv(dataset)

    # Group data by Origin and Destination IDs and calculate cumulative distances
    grouped = df.groupby(['Origin', 'Destination'])['Distance'].sum().reset_index()

    # Create a pivot table for the distance matrix
    distance_matrix = grouped.pivot(index='Origin', columns='Destination', values='Distance').fillna(0)

    # Ensure bidirectional distances by filling NaN values in the transpose of the distance matrix
    distance_matrix = distance_matrix.add(distance_matrix.T, fill_value=0)

    # Make diagonal values 0 as per the requirement
    distance_matrix.values[[range(distance_matrix.shape[0])]*2] = 0

    return distance_matrix

result_distance_matrix = calculate_distance_matrix('dataset-3.csv')
print(result_distance_matrix)
