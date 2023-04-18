import pygame

pygame.init()
pygame.mixer.music.load('audio.MP3')
pygame.mixer.music.play()
input()
pygame.event.wait()