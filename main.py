import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import dotenv_values

# Load environment variables
env_values = dotenv_values(".env")
clientId = env_values["clientId"]
clientSecret = env_values["clientSecret"]
redirectURI = env_values["redirectURI"]

# Spotify auth flow
scope = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=clientId, client_secret=clientSecret, scope=scope, redirect_uri=redirectURI))

# Get the current user
results = sp.current_user()
print(f"Logged in as: {results['id']}")

# Billboard Hot 100 chart scrape script
getDate = input("Enter the date you want to travel to (format YYYY-MM-DD): ")
webdata = requests.get(f"https://www.billboard.com/charts/hot-100/{getDate}/")
songs_html = webdata.text
htmlParse = BeautifulSoup(songs_html, "html.parser")

# Check the correct CSS selector for the song titles on Billboard's website
titles = htmlParse.select("li h3#title-of-a-story")  # Update the selector as needed
all_titles = [title.getText().strip() for title in titles]

print(all_titles)
# Search and print Spotify links for each song
for title in all_titles:
    result = sp.search(title)
    if result['tracks']['items']:  # Ensure there are results
        print(f"Song: {title}")
        print(result['tracks']['items'][0]['external_urls']['spotify'])
    else:
        print(f"No result found for: {title}")
