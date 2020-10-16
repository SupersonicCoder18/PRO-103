import pandas as pd
import plotly.express as ps

df = pd.read_csv("PRO103.csv")
fig = ps.scatter(df, x = "date", y = "cases", color = "country")
fig.show()