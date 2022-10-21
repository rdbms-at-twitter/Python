from fastapi import FastAPI

## Fast APIのインスタンス化
app = FastAPI()

### Sample: 

### Sample: http://127.0.0.1:8000/countries/japan
### 2個↓の定義と被るので上位にある方が先に実行される。

@app.get("/countries/japan")
async def japan():  
    return {"message": 'This is Japan URL'}



### Sample: http://127.0.0.1:8000/countries/Japan

@app.get("/countries/{country_name}")
## async def country(country_name):   ## これでも良いけど型を把握出来る様に↓で設定。
async def country(country_name: str):  
    return {"country_name": country_name}


### Sample: http://127.0.0.1:8000/items/1

@app.get("/items/{item_id}")
async def item(item_id: int):  
    return {"item_id": item_id}


### Sample: http://127.0.0.1:8000/hello

@app.get("/hello")
async def index():
    return {"message": "Hello World!!"}
