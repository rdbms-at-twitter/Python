import requests ### Send Request
import json     ### JSONでリクエストをPOSTする。

def main():
    url = 'http://127.0.0.1:8000/item'
    body = {
    "name": "smile",
    "description": "price less",
    "price": 1000,
    "tax": 1.1
    }
    
    res = requests.post(url, json.dumps(body)) ### 上記辞書型のbodyをJSON形式にして送信する必要あり。
    print(res.json())
    
if __name__ == "__main__":
    main()

