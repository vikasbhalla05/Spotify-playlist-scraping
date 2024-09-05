import requests
from bs4 import BeautifulSoup

getDate = input("Enter the date you want to travel to format YYYY-MM-DD: ")
webdata = requests.get(f"https://www.billboard.com/charts/hot-100/{getDate}/")

songs_html = webdata.text

htmlParse = BeautifulSoup(songs_html, "html.parser")

titles = htmlParse.select("li h3#title-of-a-story")

all_titles = [title.getText().strip() for title in titles]

print(all_titles)
