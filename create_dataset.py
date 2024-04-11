import json
import re

import lyricsgenius as genius


def make_data():
    with open('artist.json', encoding='utf-8') as f:
        aux = json.load(f)
    lyrics = [song['lyrics'] for song in aux['songs']]
    titles = [song['title'] for song in aux['songs']]
    for i in range(len(titles)):
        lyric = lyrics[i]
        title = titles[i]

        file = aux['name'] + " " + title
        file = re.sub(r'[^\w\s]+|[\d]+', r'', file).strip()
        file = "data/" + file + ".txt"
        with open(file, mode='w+', encoding='utf-8') as f:
            f.write(lyric)


def download_dataset(artist):  # api call
    api = genius.Genius('qKFW-47bQhciA2POBZTClBVZp0Kru3qbhtrkavXWzC8nHAL298zON-KDOeIiekRz')
    artist = api.search_artist(artist, get_full_info=False)
    artist.save_lyrics(filename='artist', overwrite=True, verbose=True)


def choose_artist():
    artists = [import os
import json
import time
import re
import lyricsgenius as genius

def download_lyrics(artist_name, api):
    try:
        artist = api.search_artist(artist_name, get_full_info=False)
        if artist:
            artist.save_lyrics(filename='artist_' + re.sub(r'[^\w\s]', '', artist_name), overwrite=True, verbose=False)
        else:
            print(f"No data found for {artist_name}")
    except Exception as e:
        print(f"Error downloading data for {artist_name}: {e}")
        # Optionally, retry or log the error for further investigation.

def save_lyrics_to_file():
    """ Assumes artist data is saved in 'artist.json' after download """
    try:
        with open('artist.json', encoding='utf-8') as f:
            data = json.load(f)
        for song in data['songs']:
            title = re.sub(r'[^\w\s]', '', song['title'])
            lyrics = song['lyrics']
            filename = f"data/{data['name']} {title}.txt"
            with open(filename, mode='w+', encoding='utf-8') as file:
                file.write(lyrics)
    except Exception as e:
        print(f"Failed to save lyrics to file: {e}")

def choose_artist():
    api_key = os.getenv("GENIUS_API_KEY")
    if not api_key:
        raise ValueError("GENIUS_API_KEY is not set. Please set the environment variable.")
    
    api = genius.Genius(api_key, timeout=20)  # Increased timeout
    artists = ["Ariana Grande", "Ed Sheeran", "Lady Gaga", "The Weeknd", "Dua Lipa",
               "Bruno Mars", "Billie Eilish", "Post Malone", "SZA", "Kendrick Lamar",
               "Travis Scott", "Maroon 5", "Adele", "Taylor Swift", "Justin Bieber",
               "Rihanna", "Kanye West", "Coldplay", "Imagine Dragons", "Drake"]

    for artist in artists:
        download_lyrics(artist, api)
        save_lyrics_to_file()
        time.sleep(5)  # Delay of 5 seconds between requests to avoid rate limits

if __name__ == '__main__':
    choose_artist()
]

    for artist in artists:
        download_dataset(artist)
        make_data()


# script was used to download lyrics of arbitrary artists specified in the artists array from genius.com
if __name__ == '__main__':
    choose_artist()
