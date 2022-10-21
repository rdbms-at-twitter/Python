import streamlit as st 
import pandas as pd
import numpy as np


st.title('sample Input widgets')

st.image('./variable-jp.png')

"Simple Button"

st.button('Click Button with no action')

### Click with Action with if 

"Simple Button with Action"

if st.button('click button with execute'):
    st.write('Thank you for your click!!')
    

### Click with Action with if  checkbox

"Simple Check Box with Action"

if st.checkbox('click checkbox with execute'):
    st.write('Thank you for your click!!')
    
    
### Multi Select 
# https://docs.streamlit.io/library/api-reference/widgets/st.multiselect

"Multi Select"
options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])

# st.write('You selected:', options)
st.write(f'選択した色は: {options}ですね')


### Slider (add sidebar)

number = st.sidebar.slider('Pick a number',-100, 100, 0)
st.sidebar.write(f'number: {number}になっています')


### Divie Column with left and right
# https://docs.streamlit.io/library/api-reference/layout

left_col, right_col = st.columns(2)
left_col.slider('Pick a number in left',0,100)
right_col.slider('Pick a number in right',100,200)



### download image

"Download image"

with open("variable-jp.png", "rb") as file:
    btn = st.download_button(
            label="Download image",
            data=file,
            file_name="variable-jp.png",
            mime="image/png"
          )