import configparser
import spotipy
from spotipy.oauth2 import SpotifyOAuth

config = configparser.ConfigParser()
config.read('config.ini')
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=config['spotify']['client_id'],
                                               client_secret=config['spotify']['client_secret'],
                                               redirect_uri="http://localhost:4000/callback",
                                               scope="user-read-playback-state user-modify-playback-state"))

results = sp.devices()

device_id = next((device['id'] for device in results['devices'] if device['type'] == 'Computer' and device['is_active']), None)

if device_id is None:
    raise Exception('Failed to find computer turned on and running Spotify')

print(f'Found device: {device_id}')

while True:
    input('Play?')
    print('Playing...')
    sp.start_playback(device_id)

    input('Pause?')
    print('Pausing...')
    sp.pause_playback(device_id)
