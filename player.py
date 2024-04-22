#!/usr/bin/env python
# sudo systemctl restart raspotify
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep

DEVICE_ID="98bb0735e28656bac098d927d410c3138a4b5bca"
CLIENT_ID="42ebae9b612049c7b0aa67f598777a3e"
CLIENT_SECRET="b1c291cd767b401f8c40d96de30685c1"

while True:
    try:
        reader=SimpleMFRC522()
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                       client_secret=CLIENT_SECRET,
                                                       redirect_uri="http://localhost:8080",
                                                       scope="user-read-playback-state,user-modify-playback-state"))
        
        # create an infinite while loop that will always be waiting for a new scan
        while True:
            print("Waiting for record scan...")
            id= reader.read()[0]
            print("Card Value is:",id)
            sp.transfer_playback(device_id=DEVICE_ID, force_play=False)
            
            # DONT include the quotation marks around the card's ID value, just paste the number
            if (id==584185942447):
                
                # playing a song
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:0vFOzaXqZHahrZp6enQwQb'])
                sleep(2)
                
            elif (id==486662619943):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:79dL7FLiJFOO0EoehUHQBv')
                sleep(2)
                
                
            elif (id==584186605953):
                
                # playing a song
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:6K4t31amVTZDgR3sKmwUJJ'])
                sleep(2)
                
                
            elif (id==290450229508):
                
                # playing a song
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:5alVCx5tnk0ntmdiinnYvw'])
                sleep(2)
            # continue adding as many "elifs" for songs/albums that you want to play

    # if there is an error, skip it and try the code again (i.e. timeout issues, no active device error, etc)
    except Exception as e:
        print(e)
        pass

    finally:
        print("Cleaning  up...")
        GPIO.cleanup()