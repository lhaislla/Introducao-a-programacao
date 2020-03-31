#Arquivo Python que reproduza MP3
#Tocando música no python:

import pygame
pygame.mixer.init()
pygame.mixer.music.load('ex21.mp3.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

