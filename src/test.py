import unittest
import model
import keras
import model_api


class test_model_is_loaded():
  model = tf.keras.models.load_model('/content/bad_buzz_detection/model.pkl')

  assert(type(model),'keras.src.engine.functional.Functional')


class test_model_is_working():
 def test_create_user(client):
    text = 'this girl is beautiful'
    
    response = client.post( "/predict/",data={'text': {text}})
    assert response.status_code == 200 
    




unittest.main()    
 