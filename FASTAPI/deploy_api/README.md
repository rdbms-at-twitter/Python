## Simple Calculator

- Load Local API

```
shinya@DESKTOP-8BDL7KA:~/win/github/Python/FASTAPI/deploy_api$ uvicorn main:app --reload
INFO:     Will watch for changes in these directories: ['/mnt/c/WLS/github/Python/FASTAPI/deploy_api']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [12875] using StatReload
INFO:     Started server process [12877]
INFO:     Waiting for application startup.
INFO:     Application startup complete.

```

- Local Test 
```
shinya@DESKTOP-8BDL7KA:~/win/github/Python/FASTAPI/deploy_api$ python3 sample.py
{'result': 500.0}
shinya@DESKTOP-8BDL7KA:~/win/github/Python/FASTAPI/deploy_api$
```



### Deploy to Deta

https://fastapi.tiangolo.com/ja/deployment/deta/


- Create Account

- Install Client

```
shinya@DESKTOP-8BDL7KA:~/win/github$ curl -fsSL https://get.deta.dev/cli.sh | sh
######################################################################## 100.0%
Archive:  /home/shinya/.deta/bin/deta.zip
  inflating: deta
Deta was installed successfully to /home/shinya/.deta/bin/deta
Run 'deta --help' in a new shell to get started
shinya@DESKTOP-8BDL7KA:~/win/github$
```

- Deploy

```
shinya@DESKTOP-8BDL7KA:~/win/github/Python/FASTAPI/deploy_api$ deta login
Please, log in from the web page. Waiting...
Failed to open the login page, open the following link in your browser:
https://web.deta.sh/cli/33481
Logged in successfully.
shinya@DESKTOP-8BDL7KA:~/win/github/Python/FASTAPI/deploy_api$ deta new
Successfully created a new micro
{
        "name": "deploy_api",
        "id": "xxxxxxxxxxxxxxxxxxxxx",
        "project": "xxxxxx",
        "runtime": "python3.9",
        "endpoint": "xxxxxxxx",
        "region": "ap-southeast-1",
        "visor": "disabled",
        "http_auth": "disabled"
}
shinya@DESKTOP-8BDL7KA:~/win/github/Python/FASTAPI/deploy_api$ deta visor enable
Successfully enabled visor mode
```

- Update Change and Deploy
```
shinya@DESKTOP-8BDL7KA:~/win/github/Python/FASTAPI/deploy_api$ deta deploy
Deploying...
Successfully deployed changes
shinya@DESKTOP-8BDL7KA:~/win/github/Python/FASTAPI/deploy_api$ 
```



### Confirm on Deta and Docs

URL: https://a4lw81.deta.dev/
Doc: https://a4lw81.deta.dev/docs
Auth: https://docs.deta.sh/docs/micros/api_keys

