import requests
from time import sleep
from xml.etree import ElementTree

import subprocess
from gpiozero import RGBLED



##################


INSTAGRAM_USER_ID = "XXXXXXXXXXXXXXXXXXXXXX"
INSTAGRAM_ACCESS_TOKEN = "XXXXXXXXXXXXXXXXXXXXXX"
YOUTUBE_CHANNEL_ID = "XXXXXXXXXXXXXXXXXXXXXX"
GOOGLE_API_KEY = "XXXXXXXXXXXXXXXXXXXXXX"
FACEBOOK_PAGE_URL = "XXXXXXXXXXXXXXXXXXXXXX"

# Time in seconds between two requests
REFRESH_TIME = 1
# Make a special sound every 100 followers
APPLAUSE_THRESHOLD = 100
# Raspberry GPIO where the RED pin of your LED strip is connected
RED_PIN = 9
# Raspberry GPIO where the GREEN pin of your LED strip is connected
GREEN_PIN = 10
# Raspberry GPIO where the BLUE pin of your LED strip is connected
BLUE_PIN = 11

##################


fk_url = "http://api.facebook.com/restserver.php?method=links.getStats&urls=" + FACEBOOK_PAGE_URL
yt_url = "https://www.googleapis.com/youtube/v3/channels?part=statistics&id=" + YOUTUBE_CHANNEL_ID + "&fields=items/statistics/subscriberCount&key=" + GOOGLE_API_KEY
insta_url = "https://api.instagram.com/v1/users/" + INSTAGRAM_USER_ID + "/?access_token=" + INSTAGRAM_ACCESS_TOKEN
likes = new_likes = subscribers = new_subscribers = followers = new_followers = 0
led = RGBLED(red=RED_PIN, green=GREEN_PIN, blue=BLUE_PIN)
green = red = blue = 0

while True:
    fk_response = requests.get(fk_url)
    yt_response = requests.get(yt_url)
    insta_response = requests.get(insta_url)

    if fk_response.status_code == 200:
        tree = ElementTree.fromstring(fk_response.content)
        new_likes = int(tree[0][5].text)

    if yt_response.status_code == 200:
        new_subscribers = int(yt_response.json()['items'][0]['statistics']['subscriberCount'])

    if insta_response.status_code == 200:
        new_followers = int(insta_response.json()['data']['counts']['followed_by'])

    if new_likes - likes > 0:
        blue = 1
        if new_likes % APPLAUSE_THRESHOLD == 0:
            subprocess.call(["sudo", "omxplayer", "applause.wav"])
        else:
            subprocess.call(["sudo", "omxplayer", "blop.wav"])
        sleep(0.1)
    if new_subscribers - subscribers > 0:
        red = 1
        if new_subscribers % APPLAUSE_THRESHOLD == 0:
            subprocess.call(["sudo", "omxplayer", "applause.wav"])
        else:
            subprocess.call(["sudo", "omxplayer", "blop.wav"])
        sleep(0.1)
    if new_followers - followers > 0:
        green = 1
        if new_followers % APPLAUSE_THRESHOLD == 0:
            subprocess.call(["sudo", "omxplayer", "applause.wav"])
        else:
            subprocess.call(["sudo", "omxplayer", "blop.wav"])
        sleep(0.1)
    led.color = (red, green, blue)
    sleep(1)
    red = green = blue = 0
    led.color = (red, green, blue)
    likes = new_likes
    followers = new_followers
    subscribers = new_subscribers
    sleep(REFRESH_TIME)



# import pygame.mixer
# from pygame.mixer import Sound
# pygame.mixer.init(48000, -16, 1, 1024)
# elec_ping = pygame.mixer.Sound("samples/elec_ping.wav")
# elec_ping.play()
