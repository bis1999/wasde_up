import pandas as pd 
import streamlit


import pandas as pd 
import streamlit as st 
import pickle
import calendar

import plotly.graph_objects as go
from plotly.subplots import make_subplots



df = pd.read_csv("WASDE.csv")
stations = st.sidebar.radio('Stations',(['Corn']))
st.title("WASDE Report")

project  = pd.read_csv("Projections.csv")

year_start, year_end = st.slider('Select year range', min_value=2001, max_value=2022, value=(2018, 2022))


filtered_df = df[(df['marketYear'] >= year_start) & (df['marketYear'] <= year_end)]
filtered_df  = filtered_df.set_index("marketYear").T
st.subheader(stations + "Report")

st.dataframe((filtered_df).round(2),width = 700,height = 550)


st.subheader("Projections for 2024")
st.dataframe((project),width = 700,height = 550)

