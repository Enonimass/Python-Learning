import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()
CLIENT_ID = os.getenv('Client_ID')
CLIENT_SECRET = os.getenv('client_Secret')



sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://open.spotify.com",
        client_id=CLIENT_ID,
        client_secret= CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
    )
)



user_id = sp.current_user()["id"]

print("Your Spotify User ID is:", user_id)