# Classe 6 - Web Scrapping + Spotify API 
> 19/03/2024

En aquest codi s'automatitza la recopilació i organització de dades sobre el Festival de la Cançó d'Eurovisió des de la Viquipèdia i les guarda en un format convenient per a un posterior anàlisi o visualització. (.xlsx en aquest cas) 

<hr>
La llibreria utilitzada per l'extracció de dades ha estat Beautuful Soup.

```
import requests
from bs4 import BeautifulSoup
```

**Exercici 1 (main.py)**
- Utilitza web scraping per extreure dades de la pàgina de la Viquipèdia sobre el Festival de la Cançó d'Eurovisió per a cada any des del 2000 fins al 2023.
  ```
  for anyo in range(2000,2024):
    resposta = requests.get(f'https://es.wikipedia.org/wiki/Festival_de_la_Canci%C3%B3n_de_Eurovisi%C3%B3n_{anyo}')
    try:
        codi_web = resposta.text
        soup = BeautifulSoup(codi_web, 'html.parser')

        final = soup.find('span', id='Final')
        tabla = final.find_next("table")
  ```
- Després de recopilar les dades, les emmagatzema en un arxiu Excel separat per a cada any amb el format "datasetEurovision-{anyo}.xlsx".
  ```
  df = pd.read_html(str(tabla))[0]
  print(df)
  print(f'Todo bien en {anyo}')
  df.to_excel(f'datasetEurovision-{anyo}.xlsx', index=False)
  time.sleep(1)
  ```
- Seguidament, llegeix els arxius Excel creats i els combina en un únic dataframe.
  ```
  files = glob.glob("*.xlsx")
  list_dfs = []
  
  for f in files :
      df = pd.read_excel(f)
      any = f.split('-')[1].split('.')[0]
      list_dfs.append(df)
  ```
- Modifica els noms de les columnes i afegeix una nova columna amb l'any de cada conjunt de dades.
  ```
  df['año'] = any
  df.columns.values[2] = "Cantante(s)"
  df.columns.values[5] = "Puntos"
  df.columns.values[0] = "N."
  ```

- Finalment, guarda el dataframe combinat en un nou arxiu Excel anomenat "final.xlsx".
  ```
  final_df = pd.concat(list_dfs)
  final_df.to_excel("final.xlsx", index=False)
  ```
  
_Exemple dataset 2002_:
  > ![image](https://github.com/albertarrebola08/bigdataUABopt4/assets/104431726/faaf885a-b0b6-4b36-b224-965f97779b6b)

**Exercici 2 (main2.py)**
- Llegeix el dataframe obtingut al exercici anterior del fitxer "final.xlsx".
  ```
  df = pd.read_excel('final.xlsx')
  ```
- Per a cada fila del dataframe, realitza una cerca a través de l'API de Spotify utilitzant informació com el cantant, la cançó i l'any del Festival d'Eurovisió. Els resultats de la cerca s'emmagatzemen en un fitxer JSON anomenat "search.json".
  ![image](https://github.com/albertarrebola08/bigdataUABopt4/assets/104431726/ccb20c7b-f1f8-4a26-8aef-1b29f1c05840)
  ```
  for index,row in df.iterrows():
    artist = row["Cantante(s)"]
    song = row["Canción"]
    year = row["año"]

    q = f'{song} {artist} {year} Eurovision'

    result = spotify.search(q, limit=10, offset=0, type='track', market=None)
    result['query'] = q
    with open(f"search.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4)
  ```
- Es pausa l'execució durant 15 segons després de cada cerca per evitar superar els límits d'ús de l'API de Spotify. (poden ser menys segons, els 15 son per fer comprovacions del primer resultat amb tranquilitat).
  ```
  time.sleep(15)
  ````
### Tecnologies i llibreries noves que hem utilitzat: 

|               | Tecnologia/Llibreria | Definició i ús                             |
|-----------------------|-----------------------|----------------------------------------|
| <img src="https://miro.medium.com/v2/resize:fit:772/0*oN9jA-Ad3mRlPAYy.png" width="200px"> | Beautiful Soup                 | Beautiful Soup és un paquet Python per analitzar documents HTML i XML, inclosos els que tenen un marcatge incorrecte. Crea un arbre d'anàlisi per a documents que es poden utilitzar per extreure dades d'HTML, la qual cosa és útil per al raspat web. |
