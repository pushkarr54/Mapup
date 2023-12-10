# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 09:53:01 2023

@author: Shashank
"""

import pandas as pd
import numpy as np

def get_type_count(dataset):

    df = pd.read_csv('dataset-1.csv')
     
    
    df['car_type'] = pd.cut(df['car'], bins=[-float('inf'), 15, 25, float('inf')], labels=['low', 'medium', 'high'])

    
    type_counts = df['car_type'].value_counts().to_dict()

    # Sort the dictionary alphabetically based on keys
    sorted_type_counts = dict(sorted(type_counts.items()))

    return sorted_type_counts


result_counts = get_type_count('dataset-1.csv')
print(result_counts)