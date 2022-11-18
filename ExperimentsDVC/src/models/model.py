from sklearn.ensemble import RandomForestRegressor

def RandomForestModel(X,Y):
    """Fits the classifier"""
    regressor = RandomForestRegressor(n_estimators = 100)
    regressor.fit(X_data_transformed, y_train)
    return regressor



model = RandomForestModel(X_data_transformed,y_train)