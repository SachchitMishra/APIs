from pydantic import BaseModel

class User(BaseModel):
    name:str
    dob:str
    grade:int