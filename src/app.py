import tensorflow as tf
import fastapi
import pickle
import json
import data_model as dm
import tensorflow_text as text
from fastapi import FastAPI,Response

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel


app = FastAPI()
#app = Flask(__name__)
@app.on_event("startup")
def load_model():
    global model
    #model = pickle.load(open("/content/bad_buzz_detection/model_bert.pkl", "rb"))
    model = tf.keras.models.load_model('model.pkl',compile=False)

@app.get('/')
def index():
    return {'message': 'This is the homepage of the API '}


@app.post('/predict',response_model=dm.Item)
def analyse_sentiment(data: dm.Tweet):
    print("data received to predict api")
    received = data.dict()
    text = received['text']
    print("data preprocessed waiting for prediction now")
    pred_name = model.predict([text])

    print("prediction done results si to come")
    result = 'You\'re sentiment is positive thank you' if pred_name > 0.5 else 'Thank you anyway'
    print('lets return prediction')
    return {"sentiment" : str(result)}



