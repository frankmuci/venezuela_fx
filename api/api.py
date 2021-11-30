from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import pandas as pd
import joblib
from os import getgid, pipe
from venezuela_fx.data import clean_data, get_local_data
from datetime import timedelta, datetime


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.get("/")
def index():
    return {'This is the test API': True}


@app.get("/predict")
def predict(num_days):
    # params1 = {
    #     'num_days': df.iloc[-1]['Unnamed: 0'] + timedelta(days=num_days)
    # }

    #This will represent our initial API.
    df = get_local_data()
    df = clean_data(df)
    pipeline = joblib.load('model_1.joblib')
    print(pipeline)
    prediction = pipeline.predict(df.iloc[-1]['Unnamed: 0'], df.iloc[-1]['Unnamed: 0'] + timedelta(days=num_days))
    return {'FX Rate in 30 days': prediction}





# params1 = {
#     'How many days out?' : 'X'
# }

# url = 'http://localhost:8000/predict'
# response = requests.get(url, params1).json()
# print(response)


# @app.get("/predict")
# def prediction():

#     pipeline = joblib.load('model.joblib')
#     prediction = pipeline.predict()
#     #Still need to think about what this will look like for us. Is the user putting in
#     #how many days ahead they want to predict? Does this mean making different models for
#     #each length of prediction?
#     return {
#         'Future FX Rate': float(prediction[0])
#     }
