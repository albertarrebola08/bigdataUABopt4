# clase 6

# Llibreries a instal·lar

import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import json
api_client_id = ""
api_client_secret = ""

# Configurar el cliente de Spotify
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(api_client_id, api_client_secret))


import pandas as pd
import time
import glob

#scrapping
def extract_wiki():
    for anyo in range(2000,2024):
        resposta = requests.get(f'https://es.wikipedia.org/wiki/Festival_de_la_Canci%C3%B3n_de_Eurovisi%C3%B3n_{anyo}')
        try:
            codi_web = resposta.text
            soup = BeautifulSoup(codi_web, 'html.parser')

            final = soup.find('span', id='Final')
            print(final)
            tabla = final.find_next("table")
            df = pd.read_html(str(tabla))[0]
            print(df)
            print(f'Todo bien en {anyo}')
            df.to_excel(f'datasetEurovision-{anyo}.xlsx', index=False)
            time.sleep(1)
        except(AttributeError):
            print(f"Problema en {anyo}")

#extract_wiki()


def unir_excel():
    files = glob.glob("*.xlsx")
    list_dfs = []

    for f in files :
        df = pd.read_excel(f)
        any = f.split('-')[1].split('.')[0]
        list_dfs.append(df)
        df['año'] = any
        df.columns.values[2] = "Cantante(s)"
        df.columns.values[5] = "Puntos"
        df.columns.values[0] = "N."
    final_df = pd.concat(list_dfs)
    final_df.to_excel("final.xlsx", index=False)
    print(final_df)
# unir_excel()

df = pd.read_excel('final.xlsx')
print(df)

for index,row in df.iterrows():
    artist = row["Cantante(s)"]
    song = row["Canción"]
    year = row["año"]

    q = f'{song} {artist} {year} Eurovision'



    result = spotify.search(q, limit=10, offset=0, type='track', market=None)
    result['query'] = q
    with open(f"search.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4)
    time.sleep(15)
