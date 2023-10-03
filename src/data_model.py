from pydantic import BaseModel
#from string import string
class Tweet(BaseModel):
    text: str

class Item(BaseModel):
    sentiment: str

