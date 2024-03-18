#Per #'s add a price
from pydantic import BaseModel

class User(BaseModel):
    name:str
    email:str
    latest_usage:int
    prev_usage:int