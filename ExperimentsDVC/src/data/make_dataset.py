# Functions that load the datasets
import pandas as pd

def read_data(path):
    """Reads the data"""
    data = pd.read_csv(path)
    print('----DATASET LOADED----')
    return data
