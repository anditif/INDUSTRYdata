"""
Data analisys for Boca Project
June 2025 / Andy Negut
"""

import pandas as pd
import plotly.express as px

df = pd.read_csv("boca.csv")

# graph with Boca / non Boca icons
# select the 2 columns non Boca and Boca, then display them
dff = df[["icons non Boca", "icons Boca"]]
print(dff)
fig = px.bar(dff)
fig.show()

# graph with religious Boca / icons Boca
dff = df[["religious Boca", "icons Boca"]]
print(dff)
fig = px.bar(dff)
fig.show()

# graph with total icons based on icons non Boca / icons Boca
total = (
    df[["icons non Boca", "icons Boca"]]
    .sum(axis=1, numeric_only=True)
    .to_frame("total icons")
)
print(total)

# select just the `religious Boca` column from the dataframe
rb = df[["religious Boca"]]

# create a 2 column dataframe
dff = pd.concat([total, rb], axis=1)
print(dff.head())
fig = px.bar(dff)
fig.show()

# select all columns starting with Boca candle
columns = df.columns.values.tolist()[7:]
print(columns)

# display repeated items per each category
for col in columns:
    # select rows with value == 1 then group by person asked and select only each column
    dff = df.loc[df[col] == 1].groupby("person asked")[col].count()
    print(dff)
    fig = px.bar(dff, title=col)
    fig.show()
