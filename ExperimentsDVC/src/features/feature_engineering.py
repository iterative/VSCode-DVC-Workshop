import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import yaml

with open('params.yaml') as config_file:
    config = yaml.safe_load(config_file)


def feature_selection(data,list_column_x, list_column_y):
    """Select features for training and target features"""
    X = data[list_column_x]
    y = data[list_column_y]
    print('----FEATURES SELECTED----')
    return X , y


def transform_to_datetime(data, column):
    """Applies a standard classifier"""
    data[column] = pd.to_datetime(data[column]) 


def split_data(X,y, size, state):
    """splits data into training and test set"""
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=size,
         random_state=state)
    print('----DATA SPLITTED----')
    return X_train, X_test, y_train, y_test


def standard_scaler(data):
    """Applies a standard classifier"""
    scaler = StandardScaler().fit(data)
    data_transform = scaler.transform(data)
    print('----DATA SCALED----')
    return data_transform


def delta_time(data, column):
    """Create Delta columns for daytime"""
    data['Day'] = data[column].apply(lambda time: time.day)
    data['Hour'] = data[column].apply(lambda time: time.hour)
    data['Minute'] = data[column].apply(lambda time: time.minute)



def drop_column(data, column):
    """Drop a column from the dataset"""
    data.drop(['column'], axis=1)