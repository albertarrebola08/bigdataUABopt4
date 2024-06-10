# Classe 3 - API Spotify + Gephy Visualization
> 27/02/2024
> 
L'objectiu principal de la sessió és obtenir les relacions dels generes entre els artistes relacionats obtinguts a la classe anterior. S'emmagatzema les dades en un CSV i mitjançant pandas en un dataframe amb "source" i "target" que son els que Gephi interpretarà per mostrar l'esquema graph i podrem veure les relacions entre aquests generes en base als artistes.
**Fases del codi**
- Inicialització: Recopila informació d'artistes inicials i els afegeix a llista_de_relacionats.
- Ampliació: Per a cada artista inicial, obté artistes relacionats i els afegeix a llista_definitiva.
- Creació de tuples: Converteix els elements de llista_definitiva en tuples (source, target) i els afegeix a llista_tuples.
- Exportació: Crea un DataFrame a partir de llista_tuples i l'exporta a un fitxer CSV.
**Explicació del codi (main.py)**
Un cop fetes les connexions amb Spotipy i l'importació de llibreries necessaries (explicat a la classe anterior), realitzem un primer bloc que recorre la llista d'artistes dins de result['artists']. Per a cada artista, crea un diccionari artista amb informació com l'origen ("segismuno toxicomano"), el nom de l'artista ("desti"), els gèneres, i l'ID. Afegeix aquest diccionari a la llista llista_de_relacionats.
```for artist in result['artists']:
    artista = {}
    artista['origen'] = "segismuno toxicomano"
    artista["desti"] = artist["name"]
    artista["generes"] = artist["genres"]
    artista["id"] = artist["id"]

    llista_de_relacionats.append(artista)
```
A continuació inicialitza llista_definitiva i afegeix a aquesta llista cada element de llista_de_relacionats. Per a cada element, obté artistes relacionats utilitzant la funció get_related(id). Per a cada artista relacionat, crea un nou diccionari artista amb informació com l'origen (que és el nom de l'artista en el element original), el nom de l'artista ("desti"), els gèneres, i l'ID. Afegeix aquest nou diccionari a llista_definitiva.
```
llista_definitiva = []

for element in llista_de_relacionats:
    llista_definitiva.append(element)
    id = element['id']
    result = get_related(id)
    for artist in result['artists']:
        artista = {}
        artista['origen'] = element["desti"]
        artista["desti"] = artist["name"]
        artista["generes"] = artist["genres"]
        artista["id"] = artist["id"]

        llista_definitiva.append(artista)
```
El següent bloc crea una llista de tuples llista_tuples. Per a cada element a llista_definitiva, extreu l'origen ("origen") i la destinació ("desti"), i crea una tupla (source, target). Aquesta tupla s'afegeix a llista_tuples.
```
llista_tuples = []
for i in llista_definitiva:
    source = i["origen"]
    target = i["desti"]
    tupla = (source, target)

    llista_tuples.append(tupla)
```
Finalment es crea un DataFrame de Pandas (df) a partir de llista_tuples, amb les columnes "source" i "target". Es mostra el DataFrame a la consola amb print(df) i es guarda com un fitxer CSV anomenat graf.csv utilitzant <code>to_csv()</code> de Pandas.

**Graph resultant:** 

_main.py_
![image](https://github.com/albertarrebola08/bigdataUABopt4/assets/104431726/c940e094-72a7-494a-8f9a-1df1198473ab)

### Tasques 
#### 1) Incloure gèneres musicals al dataset i visualitzar les relacions mitjançant un Graph > _tasca1.py_
```
llista_tuples = []
for i in llista_definitiva:
    source= i["origen"]
    target = i["desti"]
    tupla = (source,target)
    llista_tuples.append(tupla)

for i in llista_definitiva:
    for g in i["generes"]:
        source = i["origen"]
        target = g
        tupla = (source,target)
        llista_tuples.append(tupla)

df = pd.DataFrame(llista_tuples, columns = ["source", "target"])

print(df)
df.to_csv("graf_generes.csv", sep=",", index=False)
```
**Graph resultant:**
![image](https://github.com/albertarrebola08/bigdataUABopt4/assets/104431726/a978f106-1207-4993-b0f4-b76519c97a18)

<img src="https://cdn-icons-png.freepik.com/512/10748/10748293.png" width="40px">

#### 2) Fer el mateix procés d'obtenció pero a partir d'una playlist. > _tasca2.py_

El procés consistia en "alimentar" la funció treballada fins ara: _artist_related_artist(artist_id)_ passant com a argument l'artist_id obtingut dinàmicament desde un bucle for mitjançant una altra funció de l'API anomenada: _playlist_items(playlist_id)_.


```result_playlist = spotify.playlist_items('37i9dQZF1DX7fvgalTu2lg')```

El funcionament és molt similar pero el punt de partida surt de la iteració d'un bucle que agafa cada artista a partir de la playlist
```
for e in result_playlist['items']:
    for artist_data in e['track']['artists']:
        artist_id = artist_data['id']
        artist_name = artist_data['name']
```

Finalment després de tenir totes les dades recopilades al dataframe creem el .csv:
```
df.to_csv("graf_playlist.csv", sep=",", index=False)
```

S'ha utilitzat la playlist "!Arriba los ánimos!", generada pel propi Spotify formada per 80 cançons. <br><br> M'ha semblat interessant estudiar quins artistes i gèneres considera Spotify que pujaran el nostre estat anímic. En aquest cas hi ha 3 que destaquen: 
- Pop / Dance Pop
- Soul
- Rock / Soft Rock
- Reggueton / Urbano (tenen una agrupació modular molt separada a la resta pero amb un tamany a considerar)
  
<img src="https://github.com/albertarrebola08/bigdataUABopt4/assets/104431726/e2c03681-a282-402a-82c8-bcf45531b578" width="500px"> <br>

#### 3) Generar el graph
![image](https://github.com/albertarrebola08/bigdataUABopt4/assets/104431726/2f015f05-fef0-43f5-b6f8-862a33235bce)

<hr>

#### 4) Crear JSON's de playlist utilitzant l'offset i processar-los després de recopilar-los (Veure a la següent sessió)
- import json
- import glob

### Tecnologies i llibreries noves que hem utilitzat: 

|               | Tecnologia/Llibreria | Definició i ús                             |
|-----------------------|-----------------------|----------------------------------------|
| <img src="https://gephi.org/gephi-lite/gephi-logo.svg" width="200px"> | Gephi                 | Eina de visualització de xarxes i gràfics, utilitzada per analitzar, explorar i visualitzar dades de xarxes complexes. Ampla aplicació en ciència de les xarxes, visualització de dades i investigació social. En el nostre cas com es vee a les captures, l'hem fet servir per fer visualitzacions interactives i veure les relacions entre artistes i gèneres mitjançant nodes |
| GLOB LIBRARY | glob                 | Llibreria que permet obtenir informació dels fitxers de la carpeta i emmagatzar en un array filtrant amb instruccions com en el nostre cas que hem obtingut només els .json (`*:json`) |




