import pandas as pd
import yaml

with open('params.yaml') as config_file:
    config = yaml.safe_load(config_file)


def feature_selection(data,list_column_x, list_column_y):
    """Select features for training and target features"""
    X = data[list_column_x]
    y = data[list_column_y]
    print('----FEATURES SELECTED----')
    return X , y



