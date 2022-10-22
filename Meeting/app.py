from urllib import response
import streamlit as st
import random
import requests
import json
import datetime
import pandas as pd


page = st.sidebar.selectbox('Choose your age',['users','rooms','bookings'])

if page == 'users':
    st.title('ユーザー登録画面')

    #### https://docs.streamlit.io/library/api-reference/control-flow/st.form

    with st.form(key = 'user'):
        # DB連番 # user_id: int = random.randint(0, 100)
        username: str = st.text_input('ユーザー名', max_chars=20)
        data = {
            # 'user_id': user_id,
            'username': username
        }
        submit_button = st.form_submit_button(label='ユーザー登録')
        
    ## Submitボタンを送信したら
    if submit_button:
        st.write('### 送信データの確認(このラインはDebug用)↓')
        # st.json(data)
        st.write('## レスポンス結果(このラインはDebug用)')
        url = 'http://127.0.0.1:8000/users'
        res = requests.post(
            url,
            data=json.dumps(data)
        )
        if res.status_code == 200:
            st.success('ユーザー登録完了しました')
        st.write(res.status_code) ## Debug:レスポンスコード確認様
        st.json(res.json())   ## Debug:レスポンス確認様 

elif page == 'rooms':
    st.title('会議室登録画面')

    #### https://docs.streamlit.io/library/api-reference/control-flow/st.form

    with st.form(key = 'room'):
        # room_id: int = random.randint(0, 100)
        room_name: str = st.text_input('会議室名', max_chars=20)
        capacity: int = st.number_input('定員', step=1)
        data = {
            # 'room_id': room_id,
            'room_name': room_name,
            'capacity': capacity
        }
        submit_button = st.form_submit_button(label='会議室登録')
        
    ## Submitボタンを送信したら
    if submit_button:
        st.write('## 送信データ')
        # st.json(data) ### このラインはDebug用
        st.write('## レスポンス結果')
        url = 'http://127.0.0.1:8000/rooms'
        res = requests.post(
            url,
            data=json.dumps(data)
        )
        if res.status_code == 200:
            st.success('会議室登録完了')
        st.write(res.status_code) ## Debug:レスポンスコード確認様
        st.json(res.json()) ## Debug:レスポンスコード確認様
    

elif page == 'bookings':
    st.title('会議室予約画面')

    # https://docs.streamlit.io/library/api-reference/control-flow/st.form
    
    #### ユーザー一覧の取得 (usersエンドポイントを実行)
    url_users = 'http://127.0.0.1:8000/users'
    res = requests.get(url_users)
    users = res.json()
    # st.json(users) #確認用
    
    # 辞書型：KEY：ユーザー名、VALUE:ユーザーID
    users_name = {}
    for user in users:
        users_name[user['username']] = user['user_id']
    # st.write(users_name) #Debug用
    

    #### 会議室一覧の取得
    url_rooms = 'http://127.0.0.1:8000/rooms'
    res = requests.get(url_rooms)
    rooms = res.json()
    rooms_name = {}
    for room in rooms: # roomsのJSONデータから以下の辞書データをforで取得
        rooms_name[room['room_name']] = {
            'room_id': room['room_id'],
            'capacity': room['capacity']
        }
    # st.write(rooms_name) #Debug用

    st.write('### 会議室一覧')
    df_rooms = pd.DataFrame(rooms)
    df_rooms.columns = ['会議室名', '定員', '会議室ID']
    st.table(df_rooms)

    ## 予約一覧
    url_bookings = 'http://127.0.0.1:8000/bookings'
    res = requests.get(url_bookings)
    bookings = res.json()
    df_bookings = pd.DataFrame(bookings)
    
    ### UserIDを名前を取得
    users_id = {}
    for user in users:
        users_id[user['user_id']] = user['username']
    
    ### RoomIDからルーム名を取得
    rooms_id = {}
    for room in rooms:
        rooms_id[room['room_id']] = {
            'room_name': room['room_name'],
            'capacity': room['capacity'],
        }
    
    # IDを各値に変更(例：「ユーザーIDを名前に変換する。)
    to_username = lambda x: users_id[x]  #user idから名前に変換
    to_room_name = lambda x: rooms_id[x]['room_name'] #room id からルーム名に変換
    to_datetime = lambda x: datetime.datetime.fromisoformat(x).strftime('%Y/%m/%d %H:%M') #日付フォーマット変換
    
    # 特定の列に上記で取得した値を適用。(user_id, room_id, date等をmappingする。)
    df_bookings['user_id'] = df_bookings['user_id'].map(to_username) 
    df_bookings['room_id'] = df_bookings['room_id'].map(to_room_name)
    df_bookings['start_datetime'] = df_bookings['start_datetime'].map(to_datetime)
    df_bookings['end_datetime'] = df_bookings['end_datetime'].map(to_datetime)

    # カラム名を列名から日本語に変換して表示内容を加工
    df_bookings = df_bookings.rename(columns={
        'user_id': '予約者名',
        'room_id': '会議室名',
        'booked_num': '予約人数',
        'start_datetime': '開始時刻',
        'end_datetime': '終了時刻',
        'booking_id': '予約番号'
    })
    st.write('### 予約一覧')
    st.table(df_bookings)



    with st.form(key = 'booking'):
        # booking_id: int = random.randint(0, 100)
        username: str = st.selectbox('予約者名', users_name.keys()) #上記で取得した値から取得
        room_name: str = st.selectbox('会議室名', rooms_name.keys()) #上記で取得した値から取得
        booked_num: int = st.number_input('予約人数', step=1, min_value=1)
        date = st.date_input('日付を入力', min_value=datetime.date.today())
        start_time = st.time_input('開始時刻: ', value=datetime.time(hour=9, minute=0))
        end_time = st.time_input('終了時刻: ', value=datetime.time(hour=20, minute=0))
        submit_button = st.form_submit_button(label='予約登録')
        
    ## Submitボタンを送信したら
    if submit_button:
        user_id: int = users_name[username]              # random.randint(0, 100)
        room_id: int = rooms_name[room_name]['room_id']  # random.randint(0, 100)
        capacity: int = rooms_name[room_name]['capacity'] 
        
        data = {
            #'booking_id': booking_id,
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
        
        ## 定員以上の予約人数の場合
        if booked_num > capacity:
            st.error(f'{room_name}の定員は、{capacity}名です。{capacity}名以下の予約人数で予約して下さい')
            # st.json(data)  ### このラインはDebug用
        ## 予約時間のバリデーション
        elif start_time >= end_time:
            st.error('開始時刻が終了時刻を超えています。')
        elif start_time < datetime.time(hour=9, minute=0, second=0) or end_time > datetime.time(hour=20, minute=0, second=0):
            st.error('利用時間は9:00~20:00になります。')
        else:
            ## 上記バリデーションに問題無ければ会議室予約成功!!
            url = 'http://127.0.0.1:8000/bookings'
            res = requests.post(
            url,
            data=json.dumps(data)
            )
            if res.status_code == 200:
                st.success('予約が完了しました')
                # st.write(res.status_code)
                # st.json(res.json())
            elif res.status_code == 404 and res.json()['detail'] == 'Already booked' :
                st.error('指定の時間にはすでに予約が入っています。')
                st.json(res.json())