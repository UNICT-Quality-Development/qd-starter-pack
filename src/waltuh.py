"""
    Opens a random (but epic) Breaking Bad meme video
"""
from random import randint
import webbrowser

MIN_NUMBER = 0
MAX_NUMBER = 5

random = randint(MIN_NUMBER, MAX_NUMBER)
match random:
    case 0:
        video_id = "Cnqxd1iEcc"
    case 1:
        video_id = "Myt9ybv0IaU"
    case 2:
        video_id = "EgvToUoIN8s"
    case 3:
        video_id = "a3_PPdjD6mg"
    case 4:
        video_id = "OuoZqLyMMI4"
    case 5:
        video_id = "gDjMZvYWUdo"
    case _:
        video_id = "Zv5yvtR5S1I"

webbrowser.open('https://www.youtube.com/watch?v=' + video_id)
