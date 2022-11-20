# Functions that load the datasets
import pandas as pd
import yaml



with open('params.yaml') as config_file:
    config = yaml.safe_load(config_file)

def read_data(data_path_var):
    """Reads the data"""
    data = pd.read_csv(data_path_var)
    print('----DATASET LOADED----')
    return data
