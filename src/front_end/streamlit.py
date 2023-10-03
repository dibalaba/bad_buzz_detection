import streamlit as st
import requests
import json
from PIL import Image


# Loading Image using PIL
im = Image.open('/content/App_Icon.png')
# Adding Image to web app
st.set_page_config(page_title="Sentiment Analyzer App", page_icon = im)


st.title("Sentiment analyser")

st.write('Please enter your text')
text=title = st.text_input('text',value='')

if st.button('submit comment'):
    sentiment= requests.post(url='https://f54f-35-239-83-44.ngrok-free.app/predict',json = {'text' : text})
    res= json.loads(sentiment.text)['sentiment']
    st.write(res)
    
