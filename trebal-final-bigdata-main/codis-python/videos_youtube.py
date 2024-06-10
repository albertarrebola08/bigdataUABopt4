import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from googleapiclient.discovery import build
import json
import glob

youtube = build(
    "youtube", "v3", developerKey="")

offset = 0
token = ""


def get_videos(youtube, token, offset):
    request = youtube.search().list(
        part="snippet",
        q="como ganar dinero ahorro ahorrar",
        maxResults=50,
        order="date",
        type="video",
        regionCode="es",
        pageToken=token
    )
    response = request.execute()

    with open(f'yt_videos_{offset}.json', 'w', encoding="utf-8") as f:
        json.dump(response, f)

    if offset == 5:
        pass

    else:
        if response["nextPageToken"] == None:
            print("Final")
            pass

        else:
            offset = offset + 1
            print("Nova petició")
            token = response["nextPageToken"]
            get_videos(youtube, token, offset)


get_videos(youtube, token, offset)

#Un cop obtinguts els JSONS amb els videos (resum snippet) ara iterem ID per ID i obtenim statistics de cada video

##### GET STATISTICS VIDEOS
def get_info_videos(youtube, id):
    request = youtube.videos().list(
        part="statistics, contentDetails",
        id=id
    )
    response = request.execute()

    with open(f'statistics/{id}.json', 'w', encoding="utf-8") as f:
        json.dump(response, f)

def read_json(youtube):
    files = glob.glob("json/*.json")
    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            json_data = json.load(f)
            videos = json_data["items"]
            for video in videos:

                idVideo = video["id"]["videoId"]
                print(idVideo)
                get_info_videos(youtube, idVideo)
                break
            break

read_json(youtube)

