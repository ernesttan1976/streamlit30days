import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
from datetime import datetime
import altair as alt

# df = pd.read_csv('Aggregated_Metrics_By_Video.csv').iloc[1:,:]

# st.write(df)

# st.title("This is a title", anchor="Title")
# st.header("This is a header", anchor="Header")
# st.subheader("This is a subheader", anchor="Subheader")

# st.markdown(r"""
#             # My Streamlit App :tada:
            
#             **Hello** _there_ `how are you`?
            
#             > Quickly build Data Web Apps
            
#             - This
#             - is 
#             - Markdown :smile:
            
#             ---
            
#             $$
#             \sum_{k=0}^{n-1} ar^k = 
#             a \left(\frac{1-r^{n}}{1-r}\right)
#             $$
            
#             """)

# DAY 5

st.header('st.write')
st.write('Hello, *world*! :sunglasses:')
st.write(1234)

df = pd.DataFrame({
    'first_column': [1,2,3,4],
    'second_column': [10,20,30,40]
})
st.write(df)

df2 = pd.DataFrame(np.random.randn(200,3), columns=['a','b','c'])
c = alt.Chart(df2).mark_circle().encode(x='a', y='b',size='c',color='c', tooltip=['a','b','c'])
st.write(c)