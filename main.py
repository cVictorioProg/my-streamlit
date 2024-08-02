import streamlit as st
import pandas as pd
import os

# Function to load data
@st.cache_data(ttl=60)
def load_data(file_path):
    df = pd.read_excel(file_path)
    return df

# Define the file path
file_path = '/workspaces/my-streamlit/ACTIVE PTP.xlsx'

# Title
st.title('ACTIVE PTP DATA')

# Refresh button
if st.button('Refresh Data'):
    st.cache_data.clear()

# Load data
df = load_data(file_path)

# Display headers
st.subheader('Column Headers:')
for col in df.columns:
    st.markdown(f"**{col}**")

# Display data table
st.dataframe(df)


