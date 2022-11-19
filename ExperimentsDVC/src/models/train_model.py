from sklearn.ensemble import RandomForestRegressor
from src.data.load_dataset import read_data
from src.features.feature_engineering import feature_selection , split_data, standard_scaler
from src.models.model import  RandomForestModel
### Defines all the pipeline structure
import yaml


# One Stage pipeline. This script will be executed with 'dvc exp run' or 'dvc repro'


with open('params.yaml') as config_file:
    config = yaml.safe_load(config_file)


train = read_data(config['load']['data_path_train'])
#test = read_data(path=)

X , y = feature_selection

X_train , X_test, y_train, y_test = split_data(X,y, 
config['splitdata']['size'], 
config['splitdata']['state'])
(X_data_transformed) = standard_scaler(X_train)


model = RandomForestModel(X_data_transformed,y_train)


X_data_transformed_test = standard_scaler(X_test)
model.score(X_data_transformed_test, y_test)



