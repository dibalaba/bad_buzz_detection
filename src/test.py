import unittest
import data_model as dm
import keras
import model_api
import tensorflow as tf
import tensorflow_text as t
import requests as r


# test to make sure model is loaded
class test_model_is_loaded(unittest.TestCase):
   
   def test_model(self):
    model = tf.keras.models.load_model('model.pkl')
    
    assert(type(model),'keras.src.engine.functional.Functional')

# test to make sure API is working

class test_model_is_working(unittest.TestCase):
 def test_sentiment_returned(self):
    text = 'this girl is beautiful'
    
    response = r.post( "https://dowta-be-web-app.azurewebsites.net/predict/",data={'text': {text}})
    assert(response.status_code, 200) 
    




if __name__ == '__main__':
    unittest.main() 




 