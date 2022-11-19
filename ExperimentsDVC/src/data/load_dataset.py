# Functions that load the datasets
import pandas as pd
import yaml



with open('params.yaml') as config_file:
    config = yaml.safe_load(config_file)

def read_data():
    """Reads the data"""
    data_path_var = config_file['load']['data_path']
    data = pd.read_csv(data_path_var)
    print('----DATASET LOADED----')
    return data
