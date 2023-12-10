# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 11:30:23 2023

@author: Shashank
"""

import pandas as pd

def filter_routes(dataset):
    
    df = pd.read_csv('dataset-1.csv')

    # Group by 'route' and calculate the average of 'truck' column
    route_avg_truck = df.groupby('route')['truck'].mean()

    # Filter routes where the average truck value is greater than 7
    filtered_routes = route_avg_truck[route_avg_truck > 7].index.tolist()
    filtered_routes.sort()  # Sort the routes in ascending order

    return filtered_routes


result_routes = filter_routes('dataset-1.csv')
print(result_routes)
