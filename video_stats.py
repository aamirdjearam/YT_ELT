import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("API_KEY")
CHANNEL = 'cosmonautvarietyhour'

def getPlayslistID(CHANNEL):
    try:
        URL = f'https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL}&key={API_KEY}'
        response = requests.get(URL)
        response.raise_for_status()

        data = response.json()
        channel_items = data['items'][0]
        channel_playlistID = channel_items['contentDetails']['relatedPlaylists']['uploads']
        return channel_playlistID
    except requests.exceptions.RequestException as e:
        raise e
        

if __name__ == "__main__":
    print(getPlayslistID(CHANNEL))
else:
    print("Error")