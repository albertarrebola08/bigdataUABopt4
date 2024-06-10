# Classe 2 - SPOTIFY API 2024

> 21/02/2024


Hem utilitzat <a href="https://developer.spotify.com/documentation/web-api">l'API de Spotify </a> per obtenir informació d'altres artistes relacionats a partir d'un ID. La llibreria externa que ens ofereixen funcions com la del script: _artist_related_artists(artist_id)_ és <a href="https://spotipy.readthedocs.io/en/2.22.1/">Spotipy</a>.
```
from spotipy.oauth2 import SpotifyClientCredentials

api_client_id = ""
api_client_secret = ""

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(api_client_id,api_client_secret))
````
Seguidament hem desenvolupat un petit script per obtenir artistes relacionats dels relacionats. És a dir en una escala de dos passos hem aconseguit multiplicar l'informació per cadascún dels primers artistes afins.

**Explicació del codi**

Després d'haver realitzat la connexió amb Spotipy, agafem l'ID de l'artista que ens interessa i utilitzem la funció ```artist_related_artist(artist_id)``` per emmagatzemar els artistes relacionats
```
artist_id = '7ltDVBr6mKbRvohxheJ9h1'
results = spotify.artist_related_artists(artist_id)

artists = results['artists']
```
L'objectiu era guardar i mostrar tota aquesta informació en un format senzill i compatible així que hem emmagatzemat els resultats en un dataframe generat per nosaltres amb la llibreria Pandas i finalment hem volcat tota la informació en un arxiu d'excel anomenat _database.xlsx_

### Tecnologies i llibreries noves que hem utilitzat: 

| Logo | Tecnologia/Llibreria | Definició i ús |
|------|-----------------------|----------------|
| <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Pandas_logo.svg/700px-Pandas_logo.svg.png" alt="Pandas" width="300px"> | Pandas | Pandas és una llibreria de programació de codi obert per a Python que proporciona estructures de dades flexibles i eines d'anàlisi de dades. És àmpliament utilitzada en anàlisi de dades, manipulació de dades i preparació de dades per a la ciència de dades. Pandas permet treballar amb dades tabulars i etiquetades de manera eficient, oferint funcions per a la lectura, escriptura, manipulació i anàlisi de dades. Nosaltres l'hem fet servir per crear un dataframe a partir de la llista d'artistes i per passar aquesta a un arxiu excel <br>` frame = pd.DataFrame({"Nom": name,"Tipus": tipo,"Followers": followers,"Link": enlace,"Popularitat": popularity,"Referencia": href,"Generes": genres,"Imatges": images_list,}, index=[0])` |
| <img src="https://statusneo.com/wp-content/uploads/2023/04/Excel_Python1.png?" alt="Openpyxl" width="300px"> | Openpyxl | Openpyxl és una biblioteca de Python de codi obert que permet als desenvolupadors treballar amb fitxers d'Excel (.xlsx). Permet la creació, lectura i modificació de fitxers Excel de manera programàtica. En el nostre cas l’hem fet servir per darrere com a motor perquè la funció `.to_excel()` de Pandas pugui passar el dataframe final a un arxiu Excel.  <br><br> `final.to_excel("dataset.xlsx")` |
| <img src="https://github.com/albertarrebola08/bigdataUABopt4/assets/104431726/319461bf-f746-4ed6-a72e-8397ad7ae261" alt="Spotipy" width="50px"> | Spotipy | Spotipy és una llibreria de Python que proporciona un accés fàcil a l'API de Spotify. Suporta una gran quantitat de funcions pròpies que connecten directament amb Spotify i et donen accés a informació d’artistes, cançons… la resposta de l’API sempre és en format JSON. El nostre script parteix d’spotipy, i l’utilitzem per obtenir artistes relacionats partint d’un id. <br><br> `artist_id = '7ltDVBr6mKbRvohxheJ9h1'`<br> `results = spotify.artist_related_artists(artist_id)` |

<hr>

 ### Tasques 

 <img src="https://cdn-icons-png.freepik.com/512/10748/10748293.png" width="40px">
 
 #### 1) Obtenir la màxima informació dels artistes partint de la mateixa API 
   
 - [x] ID de l'artista
 - [x] Nom
 - [x] Enllaç a Spotify
 - [x] Followers (total)
 - [x] Gèneres
 - [x] Referència
 - [x] Popularitat
 - [x] Tipus
 - [x] URI




