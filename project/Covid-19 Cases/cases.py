import pandas as pd

df = pd.read_csv("all-states-history.csv")

df = df[['date', 'state', 'positiveIncrease']]
df.rename(columns={'positiveIncrease': 'cases'}, inplace=True)

df.to_csv('cases.csv', index=False)