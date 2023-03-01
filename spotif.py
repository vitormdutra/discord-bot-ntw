import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials

spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id='bf4f5f8fb16240e594f8bf440c848483',client_secret='2db8ef640cc54512a9b8067873510495'))

if len(sys.argv) > 1:
    name = ' '.join(sys.argv[1:])
else:
    name = 'Gojira'

#results = spotify.search(q='artist:' + name, type='artist')
results = spotify.search(q='search: ' + name,)
items = results['search']['items']
if len(items) > 0:
    artist = items[0]
    print(artist['name'], artist['images'][0]['url'])

    # auth_manager = SpotifyClientCredentials(client_id='bf4f5f8fb16240e594f8bf440c848483',client_secret='2db8ef640cc54512a9b8067873510495')
try:
    track = spotify.SpotifyTrack.search(q='search', return_first=True)
except:
    print('e')