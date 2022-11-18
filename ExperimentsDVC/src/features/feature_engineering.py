import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def feature_selection(data, list_column_x, list_column_y):
    """Select features for training and target features"""
    X = data[list_column_x]
    Y = data[list_column_y]
    return X , Y


def transform_to_datetime(data, column):
    """Applies a standard classifier"""
    data[column] = pd.to_datetime(data[column]) 


def split_data(X,y, size, state):
    """splits data into training and test set"""
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=size, random_state=state)
    return X_train, X_test, y_train, y_test


def standard_scaler(data):
    """Applies a standard classifier"""
    scaler = StandardScaler().fit(data)
    data_transform = scaler.transform(data)
    return data_transform


