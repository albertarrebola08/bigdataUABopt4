import glob
import json
import pandas as pd
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

list_tracks = []

def read_json():
    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            json_data = json.load(f)
            tracks = json_data["items"]
            for track in tracks:
                track_dicc = {}
                track_dicc['name'] = track["track"]["name"]
                track_dicc['artist_name'] = track["track"]["artists"][0]["name"]
                track_dicc['duracio_ms'] = track["track"]["duration_ms"]
                track_dicc['duracio_min'] = round(track["track"]["duration_ms"]/1000/60, 2)
                track_dicc['popularitat'] = track["track"]["popularity"]

                list_tracks.append(track_dicc)

def to_dataframe(list_tracks):
    df = pd.DataFrame(list_tracks),
    df = pd.DataFrame.from_dict(list_tracks)
    return (df)

read_json()
output = to_dataframe(list_tracks).to_csv('output.csv',sep=";", index=False)

