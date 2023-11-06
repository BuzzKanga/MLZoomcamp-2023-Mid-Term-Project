# MLZoomcamp 2023 Mid-term Project

Mid-term project for the 2023 MLZoomCamp Course.

## Problem Description

Knowing what is a fair price for a seconhand car is easier when an estimate calculated based on previous car sales is avalailble. To calculate the price based on previous card sale can be performed using different machine learning algorithms which can be compared to determine which one provides the most accurate estimate.

![images/whichcar.png](images/whichcar.png)

## Dataset

The Used Car Prices in UK Dataset will be used for training the machine leaning models. This is a comprehensive collection of automotive information extracted from the popular automotive marketplace website, [AutoTrader (UK)](www.autotrader.co.uk). This dataset comprises 3,685 data points, each representing a unique vehicle listing, and includes thirteen distinct features providing valuable insights into the world of automobiles.

The feature names are:

- Title

- Price : price of car in pounds

- Mileage (miles)

- Registration (year)

- Previous Owners

- Fuel Type

- Body Type

- Engine

- Gearbox

- Seats

- Doors

- Emission Class

- Service history

The dataset is available from [Kaggle](www.kaggle.com) at the following url: https://www.kaggle.com/datasets/muhammadawaistayyab/used-cars-prices-in-uk

## Project Deliverables

| Area                                 | Criteria                                                                                                                                                                                        | Reference                                                                                                                                                                                                       |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Problem Description                  | Problem is described in README with enough context, so it's clear what the problem is and how the solution will be used                                                                         | This document                                                                                                                                                                                                   |
| EDA                                  | Extensive EDA (ranges of values, missing values, analysis of target variable, feature importance analysis)                                                                                      | See [notebook](https://github.com/BuzzKanga/MLZoomcamp-2023-Mid-Term-Project/blob/main/notebook.ipynb) sections:<br>- Data preparation and data cleaning<br>\- Exploratory Data Analysis                        |
| Model Training                       | Trained multiple models and tuned their parameters.                                                                                                                                             | See [notebook](https://github.com/BuzzKanga/MLZoomcamp-2023-Mid-Term-Project/blob/main/notebook.ipynb) section Train Models:<br> 1. Linear Regression Model<br> 2. Decision Tree Model<br> 3. XGBoost Model |
| Exporting notebook to script         | The logic for training the model is exported to a separate script                                                                                                                               | See [predict.py](https://github.com/BuzzKanga/MLZoomcamp-2023-Mid-Term-Project/blob/main/predict.py)                                                                                                            |
| Reproducibility                      | it's possible to re-execute the notebook and the training script without errors. The dataset is committed in the project repository or there are clear instructions on how to download the data | See [Reporduce-Project.md](https://github.com/BuzzKanga/MLZoomcamp-2023-Mid-Term-Project/blob/main/Reproduce-Project.md)                                                                                        |
| Model Deployment                     | Model is deployed (with Flask, BentoML or a similar framework)                                                                                                                                  | See [Flask-Deployment.md](https://github.com/BuzzKanga/MLZoomcamp-2023-Mid-Term-Project/blob/main/Flask-Deployment.md)                                                                                          |
| Dependency and enviroment management | Provided a file with dependencies and used virtual environment. README says how to install the dependencies and how to activate the env                                                         | See [Dependencies.md](https://github.com/BuzzKanga/MLZoomcamp-2023-Mid-Term-Project/blob/main/Dependencies.md)                                                                                                  |
| Containerization                     | The application is containerized and the README describes how to build a contained and how to run it                                                                                            | See [Containerisation.md](https://github.com/BuzzKanga/MLZoomcamp-2023-Mid-Term-Project/blob/main/Containerisation.md)                                                                                          |
| Cloud deployment                     | There's code for deployment to cloud or kubernetes cluster (local or remote). There's a URL for testing - or video/screenshot of testing it                                                     | See [Cloud-Deployment.md](https://github.com/BuzzKanga/MLZoomcamp-2023-Mid-Term-Project/blob/main/Cloud-Deployment.md)                                                                                          |
