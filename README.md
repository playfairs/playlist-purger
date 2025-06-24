# Playlist Sanitizer (Kills 99.9% of Duplicate Songs)

Hi there :3

# Setup

## Clone the Repository

```Bash
git clone git@github.com:playfairs/playlist-sanitizer.git
```

## cd into the directory

```Bash
cd playlist-sanitizer
```

## Create an Application and .env file

In the .env file paste the following

```
CLIENT_ID="YOUR_CLIENT_ID" # Replace this with your client id
CLIENT_SECRET="YOUR_CLIENT_SECRET" # Replace this with your client secret
REDIRECT_URL="https://google.com" # Replace this with whatever redirect URL you want to use
```

If you don't know how to get a Client ID or Client Secret, go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
Then create an Application, put in the Name and Description, the Redirect URL has to be the same as in the .env file, and for the API select "Web API", agree to the Terms and continue.


## Create and Active a Virtual Environemnt

```Bash
python -m venv "venv"
source bin/venv/activate
```

### Or

```Bash
python3 -m venv "venv"
source bin/venv/activate
```

## Then install the requirements

```Bash
pip install -r requirements.txt
```

### Or

```Bash
pip3 install -r requirements.txt
```

## Then run the script

```Bash
python src/main.py
```

### Or

```Bash
python3 src/main.py
```

## Once the script is running, go to your select playlist, paste the Playlist ID amd hit enter.

For the Playlist ID, copy the Playlist URL, then copy the array of numbers and letters after open.spotify.com/playlist/

For example

https://open.spotify.com/playlist/3H02Sd7T8xo5I6w5mONk9F?si=cbfcec684f23452f

This Playlists ID is 3H02Sd7T8xo5I6w5mONk9F, so that's what you would paste into the terminal, and it would go from that.

## Lastly, put the Redirect URL Code in the terminal

Once you put the Playlist ID in the terminal, it will then ask you to put in the URL or code of the Website it redirected you to
Copy everything after "?code=" and paste that in the terminal, you should only need to do this once.
Once you do that, everything should work from there :3