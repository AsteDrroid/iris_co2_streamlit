
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns
import streamlit as st



st.title("Data Visualization web ap")

st.text('1 Iris dataset')

df = px.data.iris()


st.dataframe(df)
' 2 Iris dataset'


df = px.data.iris()

st.dataframe(df)
st.text('3 Iris dataset')

fig = px.scatter(df, x='sepal_width',
y='sepal_length',
color='species',
size='petal_length',
hover_data=['petal_width'],
marginal_x='box')

st.plotly_chart(fig)

fig = px.scatter(df, x="sepal_width", y="sepal_length")
fig.show()