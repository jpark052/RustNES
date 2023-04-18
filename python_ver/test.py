import pygame
import time, sys
from pygame import mixer

pygame.init()
pygame.mixer.music.load('debussy-clair-de-lune.mid')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    continue