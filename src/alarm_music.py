import pygame
import os
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.mixer.init()

class Music():
    def __init__(self):
        music_title = 'kwon.mp3'  # wprwadź nazwę muzyki
        pygame.mixer.pre_init(44100, 16, 2, 4096)
        pygame.mixer.init()

    def play(self):
        filepath = os.path.abspath(__file__)
        filedir = os.path.dirname(filepath) + "\\audio"
        musicpath = os.path.join(filedir, 'Kwon.mp3')
        pygame.mixer.music.load(musicpath)
        pygame.mixer.music.play(loops=0)

    def stop(self):
        pygame.mixer.music.stop()

c = Music()
c.play()
