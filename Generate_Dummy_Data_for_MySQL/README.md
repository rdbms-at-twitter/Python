### Prepare


- Install Pip
```
curl -O https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py --user
```

- Confirmation
```
$ pip --version
pip 23.1 from /home/ec2-user/.local/lib/python3.7/site-packages/pip (python 3.7)

$ pip --version
pip 23.1 from /home/ec2-user/.local/lib/python3.7/site-packages/pip (python 3.7)
```


- Install Required Modules

```
pip install Faker
pip install mysql-connector-python
```


### Alternative Option

- requirements.txt

```
$ cat requirements.txt
pandas
sqlalchemy
PyMySQL
tqdm
faker
```
- Batch Install
```
pip install -r requirements.txt
```

- Confirmation
```
$ pip install -r requirements.txt
Defaulting to user installation because normal site-packages is not writeable
Collecting pandas (from -r requirements.txt (line 1))
  Downloading pandas-1.3.5-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (11.3 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.3/11.3 MB 89.6 MB/s eta 0:00:00
Collecting sqlalchemy (from -r requirements.txt (line 2))
  Downloading SQLAlchemy-2.0.10-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.7 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.7/2.7 MB 93.1 MB/s eta 0:00:00
Collecting PyMySQL (from -r requirements.txt (line 3))
  Downloading PyMySQL-1.0.3-py3-none-any.whl (43 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 43.7/43.7 kB 11.4 MB/s eta 0:00:00
Collecting tqdm (from -r requirements.txt (line 4))
  Downloading tqdm-4.65.0-py3-none-any.whl (77 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 77.1/77.1 kB 20.8 MB/s eta 0:00:00
Requirement already satisfied: faker in ./.local/lib/python3.7/site-packages (from -r requirements.txt (line 5)        ) (18.4.0)
Requirement already satisfied: python-dateutil>=2.7.3 in ./.local/lib/python3.7/site-packages (from pandas->-r         requirements.txt (line 1)) (2.8.2)
Collecting pytz>=2017.3 (from pandas->-r requirements.txt (line 1))
  Downloading pytz-2023.3-py2.py3-none-any.whl (502 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 502.3/502.3 kB 69.9 MB/s eta 0:00:00
Collecting numpy>=1.17.3 (from pandas->-r requirements.txt (line 1))
  Downloading numpy-1.21.6-cp37-cp37m-manylinux_2_12_x86_64.manylinux2010_x86_64.whl (15.7 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 15.7/15.7 MB 77.3 MB/s eta 0:00:00
Requirement already satisfied: typing-extensions>=4.2.0 in ./.local/lib/python3.7/site-packages (from sqlalchem        y->-r requirements.txt (line 2)) (4.5.0)
Collecting greenlet!=0.4.17 (from sqlalchemy->-r requirements.txt (line 2))
  Downloading greenlet-2.0.2-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (566 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 566.1/566.1 kB 69.2 MB/s eta 0:00:00
Collecting importlib-metadata (from sqlalchemy->-r requirements.txt (line 2))
  Downloading importlib_metadata-6.5.1-py3-none-any.whl (22 kB)
Requirement already satisfied: six>=1.5 in ./.local/lib/python3.7/site-packages (from python-dateutil>=2.7.3->p        andas->-r requirements.txt (line 1)) (1.16.0)
Collecting zipp>=0.5 (from importlib-metadata->sqlalchemy->-r requirements.txt (line 2))
  Downloading zipp-3.15.0-py3-none-any.whl (6.8 kB)
Installing collected packages: pytz, zipp, tqdm, PyMySQL, numpy, greenlet, pandas, importlib-metadata, sqlalche        my
Successfully installed PyMySQL-1.0.3 greenlet-2.0.2 importlib-metadata-6.5.1 numpy-1.21.6 pandas-1.3.5 pytz-202        3.3 sqlalchemy-2.0.10 tqdm-4.65.0 zipp-3.15.0
```

- If you don't install mysql-connector, you might need to install it.

```
$ pip install mysql-connector-python
Defaulting to user installation because normal site-packages is not writeable
Collecting mysql-connector-python
  Downloading mysql_connector_python-8.3.0-cp38-cp38-manylinux_2_17_x86_64.whl (21.5 MB)
     |████████████████████████████████| 21.5 MB 65 kB/s
Installing collected packages: mysql-connector-python
Successfully installed mysql-connector-python-8.3.0
$
```
