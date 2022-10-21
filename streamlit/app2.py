import streamlit as st 
import pandas as pd
import numpy as np


st.title('sample chart app')

### Random 20行、3列のデータを作成
"data"
st.write(np.random.randn(20,3))

### define data for creating graph
## https://docs.streamlit.io/library/api-reference/charts

df = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a', 'b', 'c']
    
)

## Create Chart (put data from df)

"line chart"
st.line_chart(df)

"area chart"
st.area_chart(df)


"bar chart"
st.bar_chart(df)
