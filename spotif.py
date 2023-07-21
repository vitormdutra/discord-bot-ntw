import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials

spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id='bf4f5f8fb16240e594f8bf440c848483',
                                                                client_secret='2db8ef640cc54512a9b8067873510495'))

name = 'Gojira'


# results = spotify.search(q='artist:' + name, type='artist')

# https://open.spotify.com/track/0OPPvKAYRm89hWfO3tQwEs?si=572c73a6f7034637
def test(search: str):
    spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id='bf4f5f8fb16240e594f8bf440c848483',
                                                                    client_secret='2db8ef640cc54512a9b8067873510495'))

    results = spotify.search(q='artist: ' + search, type='track')
    items = results['tracks']['items']
    artist = items[0]
    music = (artist['artists'][0]['name'])
    # print(artist['artists'][0]['name'],artist['name'],artist['id'])
    print(music)


test(name)
######
