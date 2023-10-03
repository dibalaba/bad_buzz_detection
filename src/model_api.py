from fastapi import FastAPI,Response
import pickle
import json
import data_model as dm
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import tensorflow as tf

app = FastAPI()

@app.on_event("startup")
def load_model():
    global model
    #model = pickle.load(open("/content/bad_buzz_detection/model_bert.pkl", "rb"))
    model = tf.keras.models.load_model('/content/bad_buzz_detection/model.pkl')

@app.get('/')
def index():
    return {'message': 'This is the homepage of the API '}


@app.post('/predict',response_model=dm.Item)
def analyse_sentiment(data: dm.Tweet):
    received = data.dict()
    text = received['text']

    pred_name = model.predict([text])


    result = 'You\'re sentiment is positive thank you' if pred_name > 0.5 else 'Thank you anyway'

    return {"sentiment" : str(result)}
