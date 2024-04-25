# SeniorProject24-PiPlayer
We made a Raspberry Pi record player for Spotify for our senior project. In the digital age of music, streaming services like Spotify are the most popular form of music listening today. With this device, we aimed to bring back a tangible relationship with music. It also offers quicker access to people’s favorite music which is beneficial for people that listen to a lot of music daily. 

## Description
Our goal was to create a customizable record player that’s easy to use. The “records” are RFID tags that the user can scan as an album or a playlist, and they’re able to play it through speakers connected to the Raspberry Pi. This project is a proof of concept.

## Getting Started

### Dependencies
Here's the tech stack for the project:
* Raspberry Pi 4 (with a USB keyboard, USB mouse, and a monitor)
* RFID RC522 Module
* Python
* Raspotify Package
* Spotify API

### Development
* Gather materials mentioned in dependencies
* Solder RFID pins to the RFID module
* Connect the RFID scanner to the Pi
* Test the Scanner using the read.py script
* If the scanner is successful, download the Raspotify package (https://github.com/dtcooper/raspotify.git)
* If music can play through the Pi, implement the player.py script. You can use your songs by obtaining the song's URI then typing it into the code. The RFIDs might also be different, so use the read.py script to obtain & utilize the RFID values in player.py.
* The last step was a startup script to activate the program when the Pi is turned on.

## Future Ideas
Here's a list of future ideas that we could implement for the record player:
* Each tag’s info could be saved in a locally stored database, with a user interface displaying that database
* This could start a new market for music distribution where each tag could be packaged in a small vinyl record case
* Integration from more streaming services like Apple Music, Tidal, SoundCloud, etc
