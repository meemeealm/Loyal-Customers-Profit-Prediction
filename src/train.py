#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestRegressor

from sklearn.pipeline import make_pipeline
import pickle


def load_data():
    sales_df = pd.read_csv('Supermart Grocery Sales - Retail Analytics Dataset.csv')
    sales_df['Profit'] = sales_df['Profit'].astype('int')
    sales_df['Discount'] = sales_df['Discount'].astype('int')
    return sales_df

rf = RandomForestRegressor(n_estimators=30,      # fewer trees
                            max_depth=10,  
                            max_features="sqrt",
                            random_state=42)



# rf.fit(X_train, y_train)
#prediction=rf.predict(X_test)

def train_model(sales_df):
    categorical = ["Customer Name","Sub Category","City"]
    numerical = ["Sales","Discount"]

    train_dict = sales_df[categorical + numerical].to_dict(orient="records")
    y= np.log1p(sales_df['Profit'].values)
   

    pipeline = make_pipeline(
        DictVectorizer(),
        RandomForestRegressor()
    )
    pipeline.fit(train_dict, y)

    return pipeline


def save_model(pipeline, output_file):
    with open('model.bin', 'wb') as f_out:
        pickle.dump(pipeline, f_out) 

    print ("model save to model.bin")

sales_df = load_data()
pipeline = train_model(sales_df)
save_model(pipeline,'model.bin')







