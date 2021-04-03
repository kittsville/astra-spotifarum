import configparser
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from mqtt_listener import start_listener

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

def on_message(client, userdata, msg):
    user_command = msg.payload.decode('utf-8')
    print(f"Recieved command: '{user_command}'")

    if user_command == 'pause':
        sp.pause_playback(device_id)
    elif user_command in ['play', 'resume']:
        sp.start_playback(device_id)

start_listener(config['mqtt'], on_message)
