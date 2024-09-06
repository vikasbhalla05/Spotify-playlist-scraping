import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import dotenv_values

env_values = dotenv_values(".env")
clientId = env_values["clientId"]
clientSecret = env_values["clientSecret"]
redirectURI = env_values["redirectURI"]

# Spotify auth flow
scope = "playlist-modify-private" 

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=clientId,client_secret=clientSecret,scope=scope,redirect_uri=redirectURI))
results = sp.current_user()
print(results["id"])

# hot 100 chart billboard scrape script
getDate = input("Enter the date you want to travel to format YYYY-MM-DD: ")
webdata = requests.get(f"https://www.billboard.com/charts/hot-100/{getDate}/")
songs_html = webdata.text
htmlParse = BeautifulSoup(songs_html, "html.parser")
titles = htmlParse.select("li h3#title-of-a-story")
all_titles = [title.getText().strip() for title in titles]
print(all_titles)
