from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv

load_dotenv()
CLIENT_ID = os.getenv('Client_ID')
CLIENT_SECRET = os.getenv('client_Secret')

date = input("Which year do you want to travel to?\n "
             "Type the date in this format YYYY-MM-DD:")

header = {"User-Agent" :  "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                          " AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/135.0.0.0 Safari/537.36"}

url = f"https://www.billboard.com/charts/hot-100/{date}"
response = requests.get(url=url, headers=header)
soup = BeautifulSoup(response.text, 'html.parser')

song_names_spans = soup.select("li ul li h3")
artist_names_spans = soup.select("li ul li span.c-label.a-no-trucate")

song_names = [song.get_text(strip=True) for song in song_names_spans]
artist_names = [artist.get_text(strip=True) for artist in artist_names_spans]

print(f"\n🎶 Billboard Hot 100 for {date} 🎶\n")

for i,  (artist, song) in enumerate(zip(artist_names, song_names), start=1):
    print(f"{i}: {artist} - {song}")

