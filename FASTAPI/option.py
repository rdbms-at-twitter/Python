from fastapi import FastAPI
from typing import Optional

## Fast APIのインスタンス化
app = FastAPI()

### Sample: http://127.0.0.1:8000/prefecture/?prefecture_name=test&prefecture_id=1
### Sample: http://127.0.0.1:8000/prefecture/ 

@app.get("/prefecture/")
async def prefecture(prefecture_name: Optional[str] = None, prefecture_id: Optional[int] = None):  
    return {
        "prefecture_name": prefecture_name,
        "prefecture_id": prefecture_id
        }
