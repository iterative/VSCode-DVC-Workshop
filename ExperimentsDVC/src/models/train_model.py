from sklearn.ensemble import RandomForestRegressor
from src.data.load_dataset import read_data
from src.features.feature_engineering import feature_selection ,split_data, standard_scaler , delta_time , transform_to_datetime
from src.models.model import  RandomForestModel
### Defines all the pipeline structure
import yaml
from dvclive import Live 

# One Stage pipeline. This script will be executed with 'dvc exp run' or 'dvc repro'

with open('params.yaml') as config_file:
    config = yaml.safe_load(config_file)


train_data = read_data(config['load']['data_path_train'])


#Datetime Transformations
transform_to_datetime(train_data, 'epoch')
delta_time(train_data,'epoch') 


X , y = feature_selection(train_data,config['featureselection']['features'],config['featureselection']['labels'])


X_train , X_test, y_train, y_test = split_data(X,y, 
config['splitdata']['size'], 
config['splitdata']['state'])

X_data_transformed = standard_scaler(X_train)
X_data_transformed_test = standard_scaler(X_test)

### Train setup 
live = Live()
model = RandomForestModel(
    n_estimators = config['train']['n_estimators'],
    max_depth=config['train']['max_depth'],
    min_samples_split=config['train']['min_samples_split'],
    min_impurity_decrease=config['train']['min_impurity_decrease'])



#with Live() as live:
print('----TRAINING----')
model.fit(X_data_transformed, y_train)
print('----TRAINING DONE----')
live.log_metric("Acc train",model.score(X_data_transformed, y_train))
live.log_metric("Acc test", model.score(X_data_transformed_test, y_test))
live.end()

### Predictions 
print('----PREDICTIONS----')
validation_data = read_data(config['load']['data_path_test'])
transform_to_datetime(validation_data, 'epoch')
delta_time(validation_data,'epoch')

validation_data = validation_data.convert_objects(convert_numeric=True)

X_validation_transformed = standard_scaler(validation_data)

print(model.predict(X_validation_transformed[0]))









