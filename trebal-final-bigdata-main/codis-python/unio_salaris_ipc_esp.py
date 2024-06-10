import pandas as pd

def normalitza_dates(df, columna_date):
    # Intenta convertir la data al format consistent MM/YYYY, inferint el format de data
    df[columna_date] = pd.to_datetime(df[columna_date], errors='coerce').dt.strftime('%m/%Y')
    return df

df1 = pd.read_csv('espanya_salaris_nou.csv', usecols=['Any', 'Salari'])
df2 = pd.read_csv('espanya_ipc.csv', usecols=['Any', 'Index'])

df1 = normalitza_dates(df1, 'Any')
df2 = normalitza_dates(df2, 'Any')

df_combinat = pd.merge(df1, df2, on='Any', how='outer')
df_combinat.to_csv('dataset.csv', index=False)
