from fastapi import FastAPI
from typing import Optional, List     ## ItemsのListオブジェクトを取得
from pydantic import BaseModel, Field ## Field for Data Validateion


class ShopInfo(BaseModel):
    name: str
    location: str

class Item(BaseModel):
    # name: str
    name: str = Field(min_length=4, max_length=12) ### Fieldで文字数を制限
    description: Optional[str] = None
    price: int
    tax: Optional[float] = None
    
class Data(BaseModel):      ### この値が最終的に利用される。
    shop_info: Optional[ShopInfo] = None
    items: List[Item]       ### List形式でJSONオブジェクトの識別子のデータが入っている。
      
app = FastAPI()

@app.post("/")
async def index(date: Data):
    return {"data": date}
