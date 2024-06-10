import glob
import json
"""import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import pandas as pd
import glob

api_client_id = "2d24e72bccfc459d8c6eb1408f954097"
api_client_secret = "29126da8bfd742a39389cb3a03766b64"

# Configurar el cliente de Spotify
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(api_client_id, api_client_secret))

# ID de la playlist que deseas obtener
playlist_list = ["3EPibIZjyrJDGTZpvI86HQ","4jQOYNbq4xQ94tRe5Y3g85","1yugX4RYk0Y9r27UC8U4xt"]
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

def read_json():
    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            json_data = json.load(f)
            tracks = json_data["items"]
            for track in tracks:
                name = track["track"]["name"]
                print(name)


read_json()

