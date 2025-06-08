"""
Data analisys for Boca Project
June 2025 / Andy Negut
"""

import pandas as pd
import plotly.express as px

# load data
df = pd.read_csv("boca_locations.csv")

# compute sum for each row, numeric only, find the most popular/non-popular products
dff = df.sum(axis=1, numeric_only=True).to_frame("sum")
print(dff)
fig = px.bar(dff, y="sum")
fig.show()

# product availability
dff = df.sum(numeric_only=True)
print(dff)
fig = px.bar(dff)
fig.show()
