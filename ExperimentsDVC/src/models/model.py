from sklearn.ensemble import RandomForestRegressor
import yaml

with open('params.yaml') as config_file:
    config = yaml.safe_load(config_file)



def RandomForestModel(X_data_transformed,y_train):
    """Fits the classifier"""
    regressor = RandomForestRegressor(config['trainmodel']['parameters']['n_estimators'],
    max_depth=config['trainmodel']['parameters']['max_depth'],
    min_samples_split=config['trainmodel']['parameters']['min_samples_split'],
    min_impurity_decrease=config['trainmodel']['parameters']['min_impurity_decrease'])

    regressor.fit(X_data_transformed, y_train)
    return regressor



model = RandomForestModel(X_data_transformed,y_train)