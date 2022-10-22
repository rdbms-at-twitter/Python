from urllib import response
import streamlit as st
import random
import requests
import json
import datetime


page = st.sidebar.selectbox('Choose your age',['users','rooms','bookings'])

if page == 'users':
    st.title('APテスト画面(ユーザー) ')

    #### https://docs.streamlit.io/library/api-reference/control-flow/st.form

    with st.form(key = 'user'):
        user_id: int = random.randint(0, 100)
        username: str = st.text_input('ユーザー名', max_chars=20)
        data = {
            'user_id': user_id,
            'username': username
        }
        submit_button = st.form_submit_button(label='リクエスト送信')
        
    ## Submitボタンを送信したら
    if submit_button:
        st.write('## 送信データ')
        st.json(data)
        st.write('## レスポンス結果')
        url = 'http://127.0.0.1:8000/users'
        res = requests.post(
            url,
            data=json.dumps(data)
        )
        # st.write(res.status_code)
        st.json(res.json())    

elif page == 'rooms':
    st.title('APテスト画面(会議室) ')

    #### https://docs.streamlit.io/library/api-reference/control-flow/st.form

    with st.form(key = 'room'):
        room_id: int = random.randint(0, 100)
        room_name: str = st.text_input('会議室名', max_chars=20)
        capacity: int = st.number_input('定員', step=1)
        data = {
            'room_id': room_id,
            'room_name': room_name,
            'capacity': capacity
        }
        submit_button = st.form_submit_button(label='リクエスト送信')
        
    ## Submitボタンを送信したら
    if submit_button:
        st.write('## 送信データ')
        st.json(data)
        st.write('## レスポンス結果')
        url = 'http://127.0.0.1:8000/rooms'
        res = requests.post(
            url,
            data=json.dumps(data)
        )
        # st.write(res.status_code)
        st.json(res.json())  
    

elif page == 'bookings':
    st.title('APテスト画面(予約) ')

    #### https://docs.streamlit.io/library/api-reference/control-flow/st.form

    with st.form(key = 'booking'):
        booking_id: int = random.randint(0, 100)
        user_id: int = random.randint(0, 100)
        room_id: int = random.randint(0, 100)
        booked_num: int = st.number_input('予約人数', step=1)
        date = st.date_input('日付を入力', min_value=datetime.date.today())
        start_time = st.time_input('開始時刻: ', value=datetime.time(hour=9, minute=0))
        end_time = st.time_input('終了時刻: ', value=datetime.time(hour=20, minute=0))
        data = {
            'booking_id': booking_id,
            'user_id': user_id,
            'room_id': room_id,
            'booked_num': booked_num,
            'start_datetime': datetime.datetime(
                year=date.year,
                month=date.month,
                day=date.day,
                hour=start_time.hour,
                minute=start_time.minute
            ).isoformat(),
            'end_datetime': datetime.datetime(
                year=date.year,
                month=date.month,
                day=date.day,
                hour=start_time.hour,
                minute=start_time.minute
            ).isoformat()   ### Need to be str: https://fastapi.tiangolo.com/tutorial/extra-data-types/  
        }
        submit_button = st.form_submit_button(label='リクエスト送信')
        
    ## Submitボタンを送信したら
    if submit_button:
        st.write('## 送信データ')
        st.json(data)
        st.write('## レスポンス結果')
        url = 'http://127.0.0.1:8000/bookings'
        res = requests.post(
            url,
            data=json.dumps(data)
        )
        # st.write(res.status_code)
        st.json(res.json())      