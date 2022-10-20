from fastapi import FastAPI

## Fast APIのインスタンス化
app = FastAPI()

## Root Access then return following response. (Get Method at this time)
@app.get("/")
## def index():
async def index():
    return {"message": "Hello World!!"}
