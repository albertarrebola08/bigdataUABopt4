# Classe 4 - API Twitch

> 05/03/2024

### Primera part
Partint de la classe anterior on ens connectavem a l'API d'Spotify hem afegit dificultat i s'han utilitzat noves tècniques mètodes i llibreries per explotar amb més precisió les dades aportades.
Un dels processos que hem fet ha estat: Crear JSON's de playlist utilitzant **offset** i processar-los després de recopilar-los. Posteriorment també s'haxplicat la llibreria **glob** nativa de Python que ens ha servit per obtneri tots els arxius excel generats al nostre projecte.

<code>import json</code>
<code>import glob</code>
```
#serveix per agafar elements d'una playlist més enllà dels 100 items.
offset = 0

def get_playlist(playlist,offset):
    resposta = spotify.playlist_items(playlist,offset=offset)
    with open(f"{playlist}-{offset}.json", "w", encoding="utf-8") as f:
        json.dump(resposta, f, indent=4)


    if resposta["next"] == None:
        print("Final")
        pass
    else:
        offset = offset + 100
        print("nova petició")
        get_playlist(playlist, offset)


for playlist in playlist_list:
    offset = 0
    get_playlist(playlist,offset)
"""

files = glob.glob("*.json")
print(files)
```

### Segona part

<img src="https://dev.twitch.tv/marketing-assets/images/TwitchDev.png" width="100px">

L'última part de la classe ha constat en configurar el nostre accés a l'API de Twitch. Hem creat un nou projecte i hem obtingut la les credencials per poder treballar amb ella. 

__main.py__ utilitza aquesta API per obtenir streams: **get_streams** i agruparlos en diferents JSON's amb un identificador propi. Un nou mètode après i bastant imprescindible en l'obtenció de dades és time.sleep (de la llibreria time nativa de Python). Això el que ens permetrà és donar marge entre captacions de dades per evitar col·lapses i que Twith ens denegui l'accés.

```

# Hello Twitch API

import json
from twitchAPI.twitch import Twitch

import time #serveix per "adormir" el loop i que no t'expulsi la api

#definim les credencials d'accés a l'API
public = ''
secret  = ''

twitch = Twitch(public, secret)

next = None
loop = 0
def get_str(next, loop):
    resposta = twitch.get_streams(after=next, language="es", first=100)
    print(len(resposta['data']))
    with open(f'{loop}.json', 'w', encoding='utf-8') as f:
        json.dump(resposta, f, ensure_ascii=False, indent=4)

    try:
        next = resposta['pagination']['cursor']
        print('hi ha nova pagina')
        loop = loop + 1
        time.sleep(2) #afegim 2 segons abans de la seguent recaptació
        get_str(next, loop)

    except :
        print('final')
        pass

get_str(next, loop)

```
