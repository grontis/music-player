import pygame
pygame.init()

bassDrum = pygame.mixer.Sound('samples/bd_haus.wav')
snare = pygame.mixer.Sound('samples/elec_mid_snare.wav')
hat = pygame.mixer.Sound('samples/drum_cymbal_closed.wav')
beep = pygame.mixer.Sound('samples/elec_beep.wav')

from gpiozero import Button

bassDrum_btn = Button(18)
snare_btn = Button(17)
hat_btn = Button(25)
beep_btn = Button(21)

while True:
    bassDrum_btn.when_pressed = bassDrum.play
    snare_btn.when_pressed = snare.play
    hat_btn.when_pressed = hat.play
    beep_btn.when_pressed = beep.play
