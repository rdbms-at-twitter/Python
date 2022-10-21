import imp
from symbol import flow_stmt
from fastapi import FastAPI
from pydantic import BaseModel

class Data(BaseModel):
    x: float  ## intでもOK
    y: float  ## intでもOK


app = FastAPI()

@app.get('/')
def index():
    return {'message': 'Hello Deta Cloud. Thank you!!'}

@app.post('/')
def calc(data: Data):
    z = data.x*data.y
    return {'result': z}