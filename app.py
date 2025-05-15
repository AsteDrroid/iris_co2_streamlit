
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns
import streamlit as st
import plotly.express as px

st.title("Data Visualization web app")

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

"""
fig = px.scatter(df, x="sepal_width", y="sepal_length")
fig.show()
"""
px.scatter(df, x="sepal_width", y="sepal_length").show()

"""   
==============================================================

"""
df = px.data.iris()
df.head

co2 = pd.read_csv('CO2_per_capita.csv', sep=";")

co2 = co2.sort_values('Year')

# TODO: Visualize your data on a World map 
fig = px.scatter_geo(co2, locations="Country Code",
# color="continent", # which column to use to set the color of markers
hover_name="Country Name", # column added to hover information
#size="C02 Per Capita (metric tons)", # size of markers
animation_frame = "Year",
projection="natural earth")

fig.show()

""" 
mkdir my_streamlit_app
 git init -b main                                                                       [🐍 3.10.12]
git add --all
git commit -m "Streamlit first commit"

pipreqs  #pip install pipreqs  # pour requirements.txt

Then, create a repository on GitHub : https://github.com/new and copy the ssh link of the repository.

git remote add origin git@github.com:AUTHENTIKRIDDIM/iris_co2_streamlit.git
git branch --set-upstream-to=origin/main main
git pull --rebase
git push origin main
 """

"""
                                                                      [🐍 3.10.12]
git add --all
git commit -m "Streamlit 2nd commit"
git push origin main
"""