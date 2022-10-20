from fastapi import FastAPI

## Fast APIのインスタンス化
app = FastAPI()

### Sample: 


### Sample: http://127.0.0.1:8000/prefecture/
### Sample: http://127.0.0.1:8000/prefecture/?prefecture_name=kanagawa&prefecture_id=14
### Query Parameter

@app.get("/prefecture/")
async def prefecture(prefecture_name: str = 'Tokyo', prefecture_id: int = 13):  
    return {
        "prefecture_name": prefecture_name,
        "prefecture_id": prefecture_id
        }

### Sample: http://127.0.0.1:8000/prefecture/tokyo
### Sample: http://127.0.0.1:8000/prefecture/kanagawa?prefecture_id=14&city_name=Chigasaki

@app.get("/prefecture/{prefecture_name}")
async def prefecture(prefecture_name: str = 'Tokyo', prefecture_id: int = 13, city_name: str = 'Aoyama'):  
    return {
        "prefecture_name": prefecture_name,
        "prefecture_id": prefecture_id,
        "city_name": city_name
        }
