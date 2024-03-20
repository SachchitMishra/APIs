from pydantic import BaseModel

class User(BaseModel):
    num1:int
    num2:int
    sums:str