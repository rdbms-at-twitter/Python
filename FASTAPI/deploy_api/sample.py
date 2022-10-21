import requests
import json


def main():
    # url = 'http://127.0.0.1:8000'
    url = 'https://a4lw81.deta.dev/'  ### Using Deta Cloud
    data = {
        'x': 500,
        'y': 100
    }
    
    res = requests.post(url, json.dumps(data))
    print(res.json())
    
if __name__ == '__main__':
    main()