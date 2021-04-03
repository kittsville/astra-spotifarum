# Astra Spotifarum

Control Spotify on your computer remotely with a Google Nest e.g. "hey Google, music pause". Useful if you typically listen to music in bed from your Desktop computer.

Google Nest has [native support](https://support.spotify.com/us/article/spotify-on-google-home/) for Spotify remote control, so you should probably only use Astra if you have additional requirements to what they offer.

Works by connecting these services up to each other, in order:
1. Google Nest
2. IFTTT
2. Adafruit MQTT
3. Astra (this app)
4. Spotify Web API
5. Spotify on your computer

## Requirements

- [Python 3](https://www.python.org/downloads/)

## Installation

1. Install Python libraries: `pip3 install -r requirements.txt`
2. Copy `example.ini` to `config.ini`
3. Set up an MQTT topic:
    1. Set up an [IO Adafruit account](https://io.adafruit.com/)
    2. Create a new [feed](https://io.adafruit.com/kittsville/feeds) called `astra`
    3. In `config.ini` under `mqtt` set:
        - `topic` from _Feed Info_ under the feed's name
        - `username` is from _My Key_ -> _Username_ at the top of the page
        - `password` is from _My Key_ -> _Active Key_ at the top of the page
4. Set up a Spotify App:
    1. Create your [Spotify app](https://developer.spotify.com/dashboard)
    2. In `config.ini` under `spotify` set `client_id`/`client_secret`
    3. Edit your app settings to add the Redirect URI `http://localhost:4000/callback`
5. Set up IFTTT:
    1. [Create](https://ifttt.com/create) an IFTTT Applet
    2. Set _If This_ to the _Google Assistant_ trigger _Say a phrase with both a number and a text ingredient_
    3. Choose your activation phrase/reply, remembering to include the `$` in the phrase e.g. "music $"
    4. Set _Then That_ to _Adafruit IO_
    5. Choose your _Feed_ from earlier as the _Feed name_
    6. For _Data to save_ use _Add ingredient_ and select _TextField_

## Usage

1. Run the script with `python3 astra.py`
2. Log in to Spotify to give Astra access to control your Spotify player.
3. Use the voice commands you set up in IFTTT to control playback:
  1. "hey google, music play" -> Plays music on Spotify desktop
  2. "hey google, music pause" -> Pauses music on Spotify desktop
