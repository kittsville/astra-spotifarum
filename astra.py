import configparser
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from mqtt_listener import start_listener

config = configparser.ConfigParser()
config.read('config.ini')
print('Connecting to Spotify...')
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=config['spotify']['client_id'],
                                               client_secret=config['spotify']['client_secret'],
                                               redirect_uri="http://localhost:4000/callback",
                                               scope="user-read-playback-state user-modify-playback-state"))

print("Fetching list of user's Spotify devices...")
results = sp.devices()

device_id, device_name = next(((device['id'], device['name']) for device in results['devices'] if device['is_active']), None)

if device_id is None:
    raise Exception('Failed to find device running Spotify. Try playing a song')

print(f"Found device, name: '{device_name}', id: '{device_id}'")

def on_message(client, userdata, msg):
    user_command = msg.payload.decode('utf-8')
    print(f"Recieved command: '{user_command}'")

    if user_command == 'pause':
        print('Pausing music')
        sp.pause_playback(device_id)
    elif user_command in ['play', 'resume']:
        print('Playing music')
        sp.start_playback(device_id)

start_listener(config['mqtt'], on_message)
