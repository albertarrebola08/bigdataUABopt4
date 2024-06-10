# This is a sample Python script

import glob

import pandas as pd

lista = []

files = glob.glob("querys/*.csv")
for f in files:
    df = pd.read_csv(f)
    df.rename(columns={df.columns[1]: "volum"}, inplace=True)

    lista.append(df)

final = pd.concat(lista)
final.to_csv("dataset-final-final.csv", index=False)
"""
import glob
import pandas as pd

extensio = 'querys/*.csv'

df1 = pd.read_csv("querys/ahorro.csv")
df2 = pd.read_csv("querys/ahorrar.csv")
df3 = pd.read_csv("querys/precio_luz.csv")
df4 = pd.read_csv("querys/precio_gasolina.csv")
df5 = pd.read_csv("querys/como_ganar_dinero.csv")

# Merge the dataframes one by one
final = df1.merge(df2, how="left", on='date')
final = final.merge(df3, how="left", on='date')
final = final.merge(df4, how="left", on='date')
final = final.merge(df5, how="left", on='date')

# Save the merged dataframe to a new CSV file
final.to_csv("merged_data.csv", index=False)


"""
