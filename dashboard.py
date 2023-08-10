# imports
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
from datetime import datetime

# define functions

# load data
df_agg = pd.read_csv('Aggregated_Metrics_By_Video.csv').iloc[1:,:]
df_agg.columns=['Video','Video title','Video pub­lish time','Com­ments ad­ded','Shares','Dis­likes','Likes','Sub­scribers lost','Sub­scribers gained','RPM (USD)','CPM (USD)','Av­er­age per­cent­age viewed (%)','Av­er­age view dur­a­tion','Views','Watch time (hours)','Sub­scribers','Your es­tim­ated rev­en­ue (USD)','Im­pres­sions','Im­pres­sions click-through rate (%)']
df_agg['Video publish time']=pd.to_datetime(df_agg['Video publish time'])
# df_agg['Average view duration']=df_agg['Average view duration'].apply(lambda x: x.secc)

st.write(df_agg)

df_agg_sub = pd.read_csv('Aggregated_Metrics_By_Country_And_Subscriber_Status.csv')

st.write(df_agg_sub)

df_comments = pd.read_csv('Aggregated_Metrics_By_Video.csv')

st.write(df_comments)

df_time=pd.read_csv('Video_Performance_Over_Time.csv')

st.write(df_time)