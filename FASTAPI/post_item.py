from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


## Model Define for POST

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: int
    tax: Optional[float] = None
    
## Doc
#  http://127.0.0.1:8000/docs
#   Choose "Try it out" for test post method and curl command.
#

## Fast APIのインスタンス化
app = FastAPI()

@app.post("/item")

## Item from BaseModel
async def create_item(item: Item):
    # return item　### 全ての値をJSONで返す事がCurlで確認できたのでコメントアウト
    return {"message": f"{item.name}は、税込みで{int(item.price*item.tax)}円です。"}
