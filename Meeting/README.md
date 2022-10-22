### ORM

https://www.sqlalchemy.org/

```
shinya@DESKTOP-8BDL7KA:~/win/github/Python$ pip3 install sqlalchemy
Collecting sqlalchemy
  Downloading SQLAlchemy-1.4.42-cp38-cp38-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.6 MB)
     |████████████████████████████████| 1.6 MB 5.1 MB/s
Collecting greenlet!=0.4.17; python_version >= "3" and (platform_machine == "aarch64" or (platform_machine == "ppc64le" or (platform_machine == "x86_64" or (platform_machine == "amd64" or (platform_machine == "AMD64" or (platform_machine == "win32" or platform_machine == "WIN32"))))))
  Downloading greenlet-1.1.3.post0-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (157 kB)
     |████████████████████████████████| 157 kB 9.7 MB/s
Installing collected packages: greenlet, sqlalchemy
Successfully installed greenlet-1.1.3.post0 sqlalchemy-1.4.42
shinya@DESKTOP-8BDL7KA:~/win/github/Python$
```


### sqlite3

```
shinya@DESKTOP-8BDL7KA:~$ sudo apt install -y sqlite3
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following packages were automatically installed and are no longer required:
  bridge-utils dns-root-data dnsmasq-base libfwupdplugin1 ubuntu-fan
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  libsqlite3-0
Suggested packages:
  sqlite3-doc
The following NEW packages will be installed:
  sqlite3
The following packages will be upgraded:
  libsqlite3-0
1 upgraded, 1 newly installed, 0 to remove and 162 not upgraded.
Need to get 1409 kB of archives.
After this operation, 2803 kB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 libsqlite3-0 amd64 3.31.1-4ubuntu0.4 [549 kB]
Get:2 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 sqlite3 amd64 3.31.1-4ubuntu0.4 [860 kB]
Fetched 1409 kB in 2s (809 kB/s)
(Reading database ... 65840 files and directories currently installed.)
Preparing to unpack .../libsqlite3-0_3.31.1-4ubuntu0.4_amd64.deb ...
Unpacking libsqlite3-0:amd64 (3.31.1-4ubuntu0.4) over (3.31.1-4ubuntu0.2) ...
Selecting previously unselected package sqlite3.
Preparing to unpack .../sqlite3_3.31.1-4ubuntu0.4_amd64.deb ...
Unpacking sqlite3 (3.31.1-4ubuntu0.4) ...
Setting up libsqlite3-0:amd64 (3.31.1-4ubuntu0.4) ...
Setting up sqlite3 (3.31.1-4ubuntu0.4) ...
Processing triggers for man-db (2.9.1-1) ...
Processing triggers for libc-bin (2.31-0ubuntu9.7) ...
shinya@DESKTOP-8BDL7KA:~$ sqlite3 --version
3.31.1 2020-01-27 19:55:54 3bfa9cc97da10598521b342961df8f5f68c7388fa117345eeb516eaa837balt1
shinya@DESKTOP-8BDL7KA:~$
```






#### Start APP

http://127.0.0.1:8501/

- 1
```
shinya@DESKTOP-8BDL7KA:~/win/github/Python/Meeting$ streamlit run app.py 

Collecting usage statistics. To deactivate, set browser.gatherUsageStats to False.


  You can now view your Streamlit app in your browser.

  Network URL: http://172.27.74.154:8501
  External URL: http://222.224.154.237:8501

```

- 2
```
shinya@DESKTOP-8BDL7KA:~/win/github/Python/Meeting$ uvicorn sql_app.main:app --reload
INFO:     Will watch for changes in these directories: ['/mnt/c/WLS/github/Python/Meeting']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [27798] using StatReload
INFO:     Started server process [27800]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```
