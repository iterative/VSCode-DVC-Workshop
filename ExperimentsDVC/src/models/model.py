from sklearn.ensemble import RandomForestRegressor
import yaml

with open('params.yaml') as config_file:
    config = yaml.safe_load(config_file)

def RandomForestModel():
    """Fits the classifier"""
    regressor = RandomForestRegressor(config['trainmodel']['params']['n_estimators'],
    max_depth=config['train']['params']['max_depth'],
    min_samples_split=config['train']['params']['min_samples_split'],
    min_impurity_decrease=config['train']['params']['min_impurity_decrease'])

    return regressor
