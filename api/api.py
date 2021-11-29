from fastapi import FastAPI
import requests
import joblib

app = FastAPI()


@app.get("/")
def index():
    return {'This is the test API': True}

def predict(days_ahead):
    #This will represent our initial API.
    return {'Future FX Rate': 'fx_rate' + days_ahead}


params1 = {
    'How many days out?' : 'X'
}

url = 'http://localhost:8000/predict'
response = requests.get(url, params1).json()
print(response)


@app.get("/predict")
def prediction():

    pipeline = joblib.load('model.joblib')
    prediction = pipeline.predict()
    #Still need to think about what this will look like for us. Is the user putting in
    #how many days ahead they want to predict? Does this mean making different models for
    #each length of prediction?
    return {
        'Future FX Rate': float(prediction[0])
    }
