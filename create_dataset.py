import json
import re
import time
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
    api = genius.Genius('bfCIzRNIVD5S6qjz2A59gMjMso6SNsFHkPcOY_yqNbmPubaFWokKXKwc6Vo2mKau')
    artist = api.search_artist(artist, max_songs=200, get_full_info=False)
    artist.save_lyrics(filename='artist', overwrite=True, verbose=True)


def choose_artist():
    artists = ["KIDZ BOP"]

    for artist in artists:
        download_dataset(artist)
        make_data()
        time.sleep(5)

# script was used to download lyrics of arbitrary artists specified in the artists array from genius.com
if __name__ == '__main__':
    choose_artist()


# script was used to download lyrics of arbitrary artists specified in the artists array from genius.com
if __name__ == '__main__':
    choose_artist()
