
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns
import streamlit as st



st.title("Data Visualization web ap")

st.text('Iris dataset')

df = px.data.iris()

st.dataframe(df)
'Iris dataset'


df = px.data.iris()

st.dataframe(df)
st.text('Iris dataset')

fig = px.scatter(df, x='sepal_width',
y='sepal_length',
color='species',
size='petal_length',
hover_data=['petal_width'],
marginal_x='box')

st.plotly_chart(fig)