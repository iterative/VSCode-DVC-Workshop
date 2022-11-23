from sklearn.ensemble import RandomForestRegressor
import yaml

with open('params.yaml') as config_file:
    config = yaml.safe_load(config_file)

def RandomForestModel(n_estimators,max_depth,min_samples_split,min_impurity_decrease ):
    """Fits the classifier"""
    regressor = RandomForestRegressor( bootstrap=True,
        max_samples= max_samples,
        n_estimators = n_estimators,
        max_depth=max_depth,
        min_samples_split=min_samples_split,
        min_impurity_decrease=min_impurity_decrease)

    return regressor
