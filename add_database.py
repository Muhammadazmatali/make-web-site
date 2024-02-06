import streamlit as st
import pandas as pd
database = pd.read_csv("Python.xlsx")
st.dataframe("database")