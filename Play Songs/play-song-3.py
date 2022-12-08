#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import pygame

pygame.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()
while True:
    print("Digite Stop para parar a musica:")
    a = input("")
    if a == "stop":
        break