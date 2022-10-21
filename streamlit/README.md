### Install streamlit

https://docs.streamlit.io/library/get-started

```
shinya@DESKTOP-8BDL7KA:~/win/github/Python$ pip3 install streamlit
Collecting streamlit
  Downloading streamlit-1.13.0-py2.py3-none-any.whl (9.2 MB)
     |████████████████████████████████| 9.2 MB 6.0 MB/s
Requirement already satisfied: importlib-metadata>=1.4 in /usr/lib/python3/dist-packages (from streamlit) (1.5.0)
Collecting altair>=3.2.0
```

細かい依存関係の差異はエラーログを見ながら適宜修正。


### API

https://docs.streamlit.io/library/api-reference
<BR>
https://docs.streamlit.io/library/api-reference

```
shinya@DESKTOP-8BDL7KA:~/win/github/Python/streamlit$ streamlit run app.py 

Collecting usage statistics. To deactivate, set browser.gatherUsageStats to False.


  You can now view your Streamlit app in your browser.

  Network URL: http://172.27.74.154:8501
  External URL: http://222.224.154.237:8501
```