#!/usr/bin/env python
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()
try:
    print("Waiting for you to scan an RFID sticker/card")
    id = reader.read()[0]
    print("The ID for this card is:", id)
finally:
    GPIO.cleanup()
    
# /home/piplayer24/piplayer/lib/python3.11/site-packages/mfrc522 - mfrc522

# sudo apt-get -y install curl && curl -sL https://dtcooper.github.io/raspotify/install.sh | sh