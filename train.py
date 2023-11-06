#import libraries
import os
# import opendatasets as od
import pandas as pd
import numpy as np
import pickle
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
# from sklearn.tree import export_text
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mutual_info_score
# from sklearn.metrics import roc_auc_score

import matplotlib.pyplot as plt
import seaborn as sns

def load_data():
    file_path  = './data/used-cars-prices-in-uk/used_cars_UK.csv'
    if os.path.exists(file_path):
        print(f"The file {file_path} exists.")
    else:
        # Get the link to the Kaggle dataset
        dataset_url = 'https://www.kaggle.com/datasets/muhammadawaistayyab/used-cars-prices-in-uk'
        # Download the dataset
        od.download(dataset_url, './data')

    # read data into dataframe
    df = pd.read_csv(file_path)
    
    return df

def clean_data(df):
    # remove first column of dataframe (unnammed)
    df = df.iloc[:, 1:]
    df.head()

    # remove second column of dataframe (title)
    df = df.iloc[:, 1:]
    df.head()

    # make all column headings lower case
    df.columns = df.columns.str.lower()
    df.head()

    # replace all ' ' (blanks) and '(' (open breackets#) with '_' (underscore) in all column headings
    # remove any ')' (close brackets)
    df.columns = df.columns.str.replace(' ', '_')
    df.columns = df.columns.str.replace('(', '_')
    df.columns = df.columns.str.replace(')', '')

    # replace service_history null values with 'unk'
    df['service_history'].fillna('unk', inplace=True)

    # reeplace previous_owners null values with '0'
    df['previous_owners'].fillna(0.0, inplace=True)

    # remove rows where engine, gearbox, doors, seats or emission_class are null
    df = df[~(df['engine'].isna() | df['gearbox'].isna() | df['doors'].isna() | df['seats'].isna() | df['emission_class'].isna())]
    df.shape

    # remove cars with mileage >300,000 as these are probably data issues
    df = df[df.mileage_miles < 300000]

    # find all columns that have strings
    categorical = list(df.dtypes[df.dtypes == 'object'].index)

    # find all columns that huve numbers
    numerical = list(df.dtypes[df.dtypes != 'object'].index)
    numerical.remove('price')

    # replace blanks with '_' in columns that have strings
    for col in categorical:
        df[col] = df[col].str.lower().str.replace(' ', '_')

    # add vehicle age and remove registration_year
    df['age'] = 2023 - df['registration_year']
    df = df.drop(columns=['registration_year'])
    numerical.remove('registration_year')
    numerical.append('age')

    # move price column to end of dataframe
    df = df[[col for col in df if col != 'price'] + ['price']]

    return df

def split_data(df):
    # split data into train/validation/test split with 60%/20%/20% distribution
    df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)
    df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=1)

    # reset indeces
    df_train = df_train.reset_index(drop=True)
    df_val = df_val.reset_index(drop=True)
    df_test = df_test.reset_index(drop=True)

    # set target value
    y_train = df_train.price
    y_val = df_val.price
    y_test = df_test.price

    del df_train['price']
    del df_val['price']
    del df_test['price']

    return df_train, df_val, df_test, y_train, y_val, y_test

# train model
def train(df_train, y_train):
    # set-up input for model
    train_dict = df_train.to_dict(orient='records')
    dv = DictVectorizer(sparse=False)
    X_train = dv.fit_transform(train_dict)

    # create a LinearRegression model
    model = LinearRegression(fit_intercept=True, copy_X=True, n_jobs=-1)

    # fit the training data
    model.fit(X_train, y_train)

    return dv, model

if __name__ == "__main__":
    df = load_data()
    df = clean_data(df)
    df_train, df_val, df_test, y_train, y_val, y_test = split_data(df)

    dv, model = train(df_train, y_train)
    # y_pred = predict(df_val, dv, model)

    # save linear regression model to pickle file
    output_file = f'model_reg.bin'
    with open(output_file, 'wb') as f_out: 
        pickle.dump((dv, model), f_out)

    print(f"The model {output_file} created.")