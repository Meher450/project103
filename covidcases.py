import pandas as pd
import plotly.express as px

df = pd.read_csv("Covid_Data.csv")

fig = px.scatter(df, x="date", y="cases", color="country",title='Covid Data')
fig.show()
