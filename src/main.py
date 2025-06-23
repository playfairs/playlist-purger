import os
import re
import spotipy

from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
from fuzzywuzzy import fuzz

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="playlist-read-private playlist-modify-public playlist-modify-private",
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    redirect_uri=os.getenv("REDIRECT_URL"),
))

def extract_playlist_id(url: str) -> str:
    """Extract the playlist ID from a Spotify URL."""
    match = re.search(r'playlist/([a-zA-Z0-9]+)', url)
    return match.group(1) if match else None

def purge_dupes(playlist_id, official_artist=None, threshold=90):
    seen = set()
    keep_tracks_urls = []

    results = sp.playlist_items(playlist_id, additional_types=['track'])
    items = results['items']

    while results['next']:
        results = sp.next(results)
        items.extend(results['items'])

    print(f"Found {len(items)} tracks in the playlist.")

    for item in items:
        track = item['track']
        if not track:
            continue
        if 'name' not in track or 'artists' not in track:
            continue
        if 'external_urls' not in track or 'spotify' not in track['external_urls']:
            continue

        title = track['name'].strip().lower()
        artists = [a['name'].strip() for a in track['artists']]
        main_artist = artists[0] if artists else None

        artist_key = main_artist.lower()
        key = f"{title} - {artist_key}"
        if key not in seen:
            seen.add(key)
            keep_tracks_urls.append(track['external_urls']['spotify'])

    sp.playlist_replace_items(playlist_id, keep_tracks_urls[:100])
    for i in range(100, len(keep_tracks_urls), 100):
        sp.playlist_add_items(playlist_id, keep_tracks_urls[i:i+100])
    print(f"Purged {len(items) - len(keep_tracks_urls)} duplicate tracks from the playlist, kept {len(keep_tracks_urls)} unique tracks.")

if __name__ == "__main__":
    url = input("Paste the Spotify Playlist ID:").strip()
    purge_dupes(url)