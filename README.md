# Satellites  kinematic predictions Data Science Workshop

The following repository contains the material for 
[PyDay BCN Workshop](https://pybcn.org/events/pyday_bcn/pyday_bcn_2022/#agenda_section).
It presents the machine learning prediction challenge of
kinematic trajectory predictions for Satellites for avoiding
collisions and Kessler Syndrome.


The following repository presents an iteration coming from the cookie cutter
template and includes the key building blocks for making experiments for DVC
VSCode extension. 
Some of the cookie cutter template features have been dropped out for simplicity.


### The Challenge

Satellite position and Speed
The number of RSOs - artificial objects that are in orbit around earth has nearly doubled during the last 2 decades, from around 11K to 20K in 2019. This number is expected to rise due to satellite technology improvements and lower costs of production.

The challenge is to predict a more accurate orbit trajectory and satellite positions in order to avoid collisions and avoid the space debris. An uncontrolled chain of collisions and a huge amount of space debris cause what is called the Kessler Syndrome

Kessler Syndrome is a phenomenon in which the amount of junk in orbit around Earth reacehs a point where it just creates more and more space Debris, causing substantial problems for satellites, astronauts and mission planners. Some of the day to day problems might include internet connections and mobile communications interruptions. In order to avoid cascade effects, we need to predict position and velocity for satellites.


### Target variables & Machine Learning Challenge

Taking into account the challenge and dataset, coming from an already known simulated trajectories (position and velocity) we want to predict real kinematic trajectories position and velocity. Therefore, we have multiple target variables and continuous variables. We will use a Random Forest Regressor.

We use an ensemble method , in which we use multiple learning algorithms to obtain better predictive performance. For that we fit multiple target variable regression trees and average results. A random forest is a meta estimator that fits a number of classifying decision trees on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting. The sub-sample size is controlled with the max_samples parameter if bootstrap=True (default), otherwise the whole dataset is used to build each tree. A random forest is a meta estimator that fits a number of classifying decision trees on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting.

In a nutshell, we could say that this strategy consists of fitting one regressor per target and then to an average ensemble method. If in in a single target scenario we fit one tree, here we have a forest.


https://user-images.githubusercontent.com/24204714/221022813-70fea91e-e740-41d9-a52f-430a2560c0e3.mp4




### DVC Experiments
------------

Managing machine learning experiments can be challenging. The ultimate goal
of the open-source [DVC](https://github.com/iterative/vscode-dvc) extension for VSCode is to make analysis, collaboration and reproducibility easier.

With the extension, we are able to visualize experiments in the table and plots,
analyze them and persist them.
There are two main manners experiments can be conducted with the material
presented in the repository: through fast experiment tracking with a jupyter
notebook and thanks to dvc pipelines

#### Fast experiment tracking with DVCLive

You can follow the blogpost to know more about DVCLive release . 
If you want to conduct experiments directly from your notebook, please follow
 the instructions above:

```
git clone https://github.com/iterative/VSCode-DVC-Workshop
git checkout dvcLiveexp
```
Activate the virtual environment and configure your Python correctly. Then go to
`notebooks > Statistical Distribution Datasets.ipynb` and run all cells.

Go then to the extension and select Show experiments

#### Experiment tracking with DVC Pipelines

For defining [stages](https://dvc.org/doc/user-guide/pipelines/defining-pipelines#defining-pipelines), we can use CLI or `dvc.yaml` file. Please refer [here](https://github.com/SoyGema/VSCode-DVC-Experiments-Template) 
for a template of how to build your own pipeline with DVC and [here]() to customize your parameters. 
Visit [our community gem](https://iterative.ai/blog/august-22-community-gems#im-constructing-a-pipeline-with-several-stages-inside-the-dvcyaml-file) 
as a common FAQ that might take place when executing your pipeline.

For defining [metrics](https://dvc.org/doc/start/experiment-management/experiments#get-started-experiments) we use [DVCLive](https://github.com/SoyGema/VSCode-DVC-Experiments-Template) python library. As a starting point we will be using [log_metric()](https://dvc.org/doc/dvclive/api-reference/live/log_metric#livelog_metric) and [sklearn_plot()](https://dvc.org/doc/dvclive/api-reference/live/log_sklearn_plot#livelog_sklearn_plot) methods to set up experiments.

For [experiments](https://dvc.org/doc/start/experiment-management/experiments#get-started-experiments), they can be executed from the CLI or the UI coming from the table. The main CLI command will be using will [`dvc exp run`](https://dvc.org/doc/dvclive/api-reference/live/log_sklearn_plot)
 and [`dvc repro`](https://dvc.org/doc/command-reference/repro#repro) for CLI. 


### Setup instructions

1. Clone the repository 

```
git clone https://github.com/iterative/VSCode-DVC-Workshop
```

2. Download the data. Inside the project folder ExperimentsDVC/dataset. This action will create a
   folder inside the project called satellite-data containing the dataset.

```
dvc get https://github.com/iterative/dataset-registry \
          workshop/satellite-data/
```

2. Create a virtual environment. Once created, a pop-up window might show up to select the environment for the workspace. Click yes.


```
pip install virtualenv
cd VSCode-DVC-Workshop/
virtualenv venv
```

If the pop-up window doesn't show, use `source venv/bin/activate` to activate the virtualenv.

3. Install requirements

```
pip install -r requirements.txt
```

4. Install the [DVC VSCode extension from the marketplace](https://marketplace.visualstudio.com/items?itemName=Iterative.dvc). 
For that, inside your IDE, go to Extensions and search for DVC and click install

(image)

5. Open the Command Palette (F1 or ⇧⌃P on Windows/Linux or ⇧⌘P on macOS) and type
DVC: Setup The Workspace. 
Select
* Auto. Use the virtual environment detected automatically by the Python version OR
* Manual. Let me select the virtual environment manually. 


6. Have a look at the [Notebook](https://github.com/iterative/VSCode-DVC-Workshop/blob/main/ExperimentsDVC/notebooks/Satellites_orbit_trajectory.ipynb) and learn more about the challenge we will track

6. Read the [DVC documentation](https://dvc.org/doc) and customize the `dvc.yaml` , `params.yaml` files.

7. Set python path.

```
export PYTHONPATH="$path/VSCode-DVC-Workshop/"
```


### The resulting directory structure
------------

The directory structure of your new project looks like this: 

```
├── LICENSE
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scripts to download or generate data
│   │   └── make_dataset.py
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling
│   │   └── build_features.py
│   │
│   ├── models         <- Scripts to train models and then use trained models to make
│   │   │                 predictions
│   │   ├── predict_model.py
│   │   └── train_model.py
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
│
├── dvc.yaml           <- includes pipeline stages definition. Linked to params.yaml file 
└── params.yaml        <- define the hyperparameters we want to iterate from that will be useful for the table

```

## Contributing

We welcome contributions! [See the docs for guidelines](https://drivendata.github.io/cookiecutter-data-science/#contributing).

### Installing development requirements
------------

    pip install -r requirements.txt

### Running the tests
------------

    py.test tests




