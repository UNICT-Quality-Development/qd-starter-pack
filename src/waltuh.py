"""
    Opens a random (but epic) Breaking Bad meme video
"""
import random
import webbrowser

random = random.randint(0, 5)
match random:
    case 0:
        webbrowser.open('https://www.youtube.com/watch?v=_Cnqxd1iEcc')
    case 1:
        webbrowser.open('https://www.youtube.com/watch?v=Myt9ybv0IaU')
    case 2:
        webbrowser.open('https://www.youtube.com/watch?v=EgvToUoIN8s')
    case 3:
        webbrowser.open('https://www.youtube.com/watch?v=a3_PPdjD6mg')
    case 4:
        webbrowser.open('https://www.youtube.com/watch?v=OuoZqLyMMI4')
    case 5:
        webbrowser.open('https://www.youtube.com/watch?v=gDjMZvYWUdo')
