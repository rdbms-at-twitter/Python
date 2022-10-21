from random import sample
import streamlit as st 
import pandas as pd

## St Tile
st.title("This is sample Title")

## Basic write
st.write('Demo app Streamlit')

## Magic
"Hello World with double quotation"

## markdown
st.markdown("## Sample Markdown")


## st.markdown
st.markdown(
   """
   # doc1
   ## doc2
   ### doc3
   
   - test lint1
   """ 
)

st.code('a = 12345', language='python')

st.code("""
        
        import numpy as np
        import pandas as pd
        a = 123
        pd.DataFrame()
        
        """)

### Dataframe
### https://docs.streamlit.io/library/api-reference/data/st.dataframe


df = pd.DataFrame({
    'Row1': [1,2,3,4,5],
    'Row2': [-1,-2,-3,-4,-5],
})


st.dataframe(df)

### 列で大きいデータをハイライト
st.dataframe(df.style.highlight_max(axis=0))



## JSON

st.json({
    'data':{
        'name': 'abc',
        'age' : 123
        
    }
})