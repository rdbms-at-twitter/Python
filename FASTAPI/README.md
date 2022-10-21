## This repo is testing Fast API.


### Basic Test

```
shinya@DESKTOP-8BDL7KA:~/win/github/Python/FASTAPI$ python3 type_hints.py 
110円
shinya@DESKTOP-8BDL7KA:~/win/github/Python/FASTAPI$ python3 type_hints2.py 
110円
shinya@DESKTOP-8BDL7KA:~/win/github/Python/FASTAPI$ 
```

### Install Fast API

- Prepare

```
sudo apt-get update
sudo apt install python3-pip
```

- FastAPI

```
shinya@DESKTOP-8BDL7KA:~/win/github/Python$ pip3 install fastapi
Collecting fastapi
  Downloading fastapi-0.85.1-py3-none-any.whl (55 kB)
     |████████████████████████████████| 55 kB 1.4 MB/s
Collecting starlette==0.20.4
  Downloading starlette-0.20.4-py3-none-any.whl (63 kB)
     |████████████████████████████████| 63 kB 2.1 MB/s
Collecting pydantic!=1.7,!=1.7.1,!=1.7.2,!=1.7.3,!=1.8,!=1.8.1,<2.0.0,>=1.6.2
  Downloading pydantic-1.10.2-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (13.6 MB)
     |████████████████████████████████| 13.6 MB 5.3 MB/s
Collecting anyio<5,>=3.4.0
  Downloading anyio-3.6.2-py3-none-any.whl (80 kB)
     |████████████████████████████████| 80 kB 7.4 MB/s
Collecting typing-extensions>=3.10.0; python_version < "3.10"
  Downloading typing_extensions-4.4.0-py3-none-any.whl (26 kB)
Collecting sniffio>=1.1
  Downloading sniffio-1.3.0-py3-none-any.whl (10 kB)
Requirement already satisfied: idna>=2.8 in /usr/lib/python3/dist-packages (from anyio<5,>=3.4.0->starlette==0.20.4->fastapi) (2.8)
Installing collected packages: sniffio, anyio, typing-extensions, starlette, pydantic, fastapi
Successfully installed anyio-3.6.2 fastapi-0.85.1 pydantic-1.10.2 sniffio-1.3.0 starlette-0.20.4 typing-extensions-4.4.0
shinya@DESKTOP-8BDL7KA:~/win/github/Python$
```

- Server

```
shinya@DESKTOP-8BDL7KA:~/win/github/Python$ pip3 install uvicorn
Collecting uvicorn
  Downloading uvicorn-0.19.0-py3-none-any.whl (56 kB)
     |████████████████████████████████| 56 kB 2.5 MB/s
Requirement already satisfied: click>=7.0 in /usr/lib/python3/dist-packages (from uvicorn) (7.0)
Collecting h11>=0.8
  Downloading h11-0.14.0-py3-none-any.whl (58 kB)
     |████████████████████████████████| 58 kB 5.9 MB/s
Installing collected packages: h11, uvicorn
  WARNING: The script uvicorn is installed in '/home/shinya/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed h11-0.14.0 uvicorn-0.19.0
shinya@DESKTOP-8BDL7KA:~/win/github/Python$
```


### MEMO:

- FastAPI は巨人の肩の上に立っています。
  Web の部分はStarlette
  データの部分はPydantic

https://fastapi.tiangolo.com/ja/



### Start Server

- main.py

```
shinya@DESKTOP-8BDL7KA:~/win/github/Python/FASTAPI$ uvicorn main:app --reload
INFO:     Will watch for changes in these directories: ['/mnt/c/WLS/github/Python/FASTAPI']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [4263] using StatReload
INFO:     Started server process [4265]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     127.0.0.1:60442 - "GET / HTTP/1.1" 200 OK
```

- sample.py

http://127.0.0.1:8000/items/5?q=some

```
shinya@DESKTOP-8BDL7KA:~/win/github/Python/FASTAPI$ uvicorn sample:app --reload
INFO:     Will watch for changes in these directories: ['/mnt/c/WLS/github/Python/FASTAPI']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [4405] using StatReload
INFO:     Started server process [4407]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     127.0.0.1:60452 - "GET /items/5?q=somequery HTTP/1.1" 200 OK
```



### API Document

- Automatically created !!!!!!

Swagger format Document is auto generated.
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc

Refer:
https://swagger.io/tools/swagger-ui/


### Query Parameter (Default: Tokyo)

http://127.0.0.1:8000/prefecture/
http://127.0.0.1:8000/prefecture/?prefecture_name=kanagawa&prefecture_id=14

http://127.0.0.1:8000/prefecture/tokyo
http://127.0.0.1:8000/prefecture/kanagawa?prefecture_id=14&city_name=Chigasaki


```
hinya@DESKTOP-8BDL7KA:~/win/github/Python/FASTAPI$ uvicorn query_param:app --reload
INFO:     Will watch for changes in these directories: ['/mnt/c/WLS/github/Python/FASTAPI']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [6337] using StatReload
INFO:     Started server process [6339]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     127.0.0.1:60628 - "GET /prefecture/ HTTP/1.1" 200 OK
```


### Optional

http://127.0.0.1:8000/prefecture/?prefecture_name=test&prefecture_id=1
http://127.0.0.1:8000/prefecture/ 


```
shinya@DESKTOP-8BDL7KA:~/win/github/Python/FASTAPI$ uvicorn option:app --reload
INFO:     Will watch for changes in these directories: ['/mnt/c/WLS/github/Python/FASTAPI']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [7121] using StatReload
INFO:     Started server process [7123]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```


## Post Item

Using ``` from pydantic import BaseModel ```

Check it Out: http://127.0.0.1:8000/docs

- Curl ALL

```
shinya@DESKTOP-8BDL7KA:~$ curl -X 'POST' \
  'http://127.0.0.1:8000/item' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Humberger",
  "description": "with Chips",
  "price": 500,
  "tax": 1.1
}'
{"name":"Humberger","description":"with Chips","price":500,"tax":1.1}shinya@DESKTOP-8BDL7KA:~$
```

- Curl Modify with Fstring

```
curl -X 'POST' \
  'http://127.0.0.1:8000/item' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "ハンバーガー",
  "description": "トマト入り",
  "price": 505,
  "tax": 1.1
}'
```

- Response body

```
{
  "message": "ハンバーガーは、税込みで555円です。"
}
```



- Load Server with reload
```
shinya@DESKTOP-8BDL7KA:~/win/github/Python/FASTAPI$ uvicorn post_item:app --reload
INFO:     Will watch for changes in these directories: ['/mnt/c/WLS/github/Python/FASTAPI']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [7637] using StatReload
INFO:     Started server process [7639]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     127.0.0.1:60824 - "GET /docs HTTP/1.1" 200 OK
INFO:     127.0.0.1:60824 - "GET /openapi.json HTTP/1.1" 200 OK
INFO:     127.0.0.1:60830 - "POST /item HTTP/1.1" 200 OK
INFO:     127.0.0.1:60834 - "GET /docs HTTP/1.1" 200 OK
INFO:     127.0.0.1:60834 - "GET /openapi.json HTTP/1.1" 200 OK
INFO:     127.0.0.1:60840 - "POST /item HTTP/1.1" 200 OK
```




### Post Item Validation

- Item Length 4-12
```
Item{
name*	string
title: Name
maxLength: 12
minLength: 4
description	string
title: Description
price*	integer
title: Price
tax	Tax[...]
 
}
```

- Using Field for Validate Length
```
shinya@DESKTOP-8BDL7KA:~/win/github/Python/FASTAPI$ uvicorn shop_api:app --reload
INFO:     Will watch for changes in these directories: ['/mnt/c/WLS/github/Python/FASTAPI']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [11876] using StatReload
INFO:     Started server process [11878]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```