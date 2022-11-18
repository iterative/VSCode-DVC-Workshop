# Satellites  kinematic predictions Data Science Workshop

The following repository contains the material for PyDay Workshop.
It presents the machine learning prediction challenge of
kinematic trajectory predictions for Satellites for avoiding
collisions and Kessler Syndrome.


The following repository presents an iteration coming from the cookie
cutter template and includes the key building blocks for making experiments
for DVC VSCode extension. Some of the cookie cutter template features have 
been dropped out for simplicity.


### Setup instructions

1. Clone the repository 

´git clone https://github.com/iterative/VSCode-DVC-Workshop´

2. Create virtual environment. Once created, a popup window might show up
to select the environment for the workspace. Click yes

´pip install virtualenv´
´cd VSCode-DVC-Workshop/
virtualenv .venv´

OR 

activate existing virtual environment
´source .venv/bin/activate´

3. Install requirements

´pip install -r requirements.txt´

4. Install DVC VSCode extension from the marketplace. For that, Inside your
IDE, go to Extensions and search for DVC and click install

(image)

5. Open the Command Palette (F1 or ⇧⌃P on Windows/Linux or ⇧⌘P on macOS) and type
DVC: Setup The Workspace

5. Read the documentation and customize the ´dvc.yaml´ , ´params.yaml´ files.





### DVC Experiments
------------

Managing machine learning experiments can be challenging. The ultimate goal
of DVC OpenSource extension is to make analysis, collaboration and reproducibility easier.

With the extension , we are able to visualize experiments in the table and plots.

For defining [stages](https://dvc.org/doc/user-guide/pipelines/defining-pipelines#defining-pipelines)
We can use CLI or ´dvc.yaml´ file. Please refer [here]() 
for a template of how to build you own pipeline with DVC and [here]() to customize your parameters. 
Visit [our community gem](https://iterative.ai/blog/august-22-community-gems#im-constructing-a-pipeline-with-several-stages-inside-the-dvcyaml-file) 
as a common FAQ that might take place when executing you pipeline.

For defining [metrics]() we use DVCLive python library. As a starting point we 
will be using [log_metrics()]() and [sklearn_plots()]() methods to setup experiments

For [experiments](), they can be executed from the CLI or the UI coming from
the table. The main CLI command will be using  will [´dvc exp run´]()
 and [´dvc repro´]() for CLI interface. 



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




