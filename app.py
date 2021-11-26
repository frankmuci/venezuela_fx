import streamlit as st
import requests
import pandas as pd
import numpy as np



st.markdown("How far into the future do you want to predict the FX rate?")


@st.cache
def get_select_box_data():

    future_ranges = ['1 day','7 days', '30 days']

    return pd.DataFrame({
        'first column': future_ranges,

    })


df = get_select_box_data()

option = st.selectbox('Select a line to filter', df['first column'])

filtered_df = df[df['first column'] == option]

#st.write(filtered_df)
