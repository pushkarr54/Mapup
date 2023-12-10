# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 12:14:03 2023

@author: Shashank
"""

import pandas as pd


def calculate_distance_matrix(dataset):
    df = pd.read_csv(dataset)
    grouped = df.groupby(['id_start', 'id_end'])['distance'].sum().reset_index()
    distance_matrix = grouped.pivot(index='id_start', columns='id_end', values='distance').fillna(0)
    distance_matrix = distance_matrix.add(distance_matrix.T, fill_value=0)
    distance_matrix.values[[range(distance_matrix.shape[0])]*2] = 0

    return distance_matrix

result_distance_matrix = calculate_distance_matrix('dataset-3.csv')
print(result_distance_matrix)



def unroll_distance_matrix(distance_matrix):
    distance_matrix = distance_matrix.reset_index()

   
    ids = distance_matrix.iloc[:, 0].tolist()

   
    unrolled_distances = []

    
    for i in range(len(ids)):
        id_start = ids[i]
        for j in range(len(ids)):
            id_end = ids[j]
            distance = distance_matrix.iloc[i, j + 1]  
            if id_start != id_end:
                unrolled_distances.append({'id_start': id_start, 'id_end': id_end, 'distance': distance})

   
    unrolled_distances_df = pd.DataFrame(unrolled_distances)

    return unrolled_distances_df


result_unrolled_distance = unroll_distance_matrix(result_distance_matrix)
print(result_unrolled_distance)
