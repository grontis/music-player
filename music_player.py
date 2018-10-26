import time
import pygame
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)

pygame.init()
pygame.mixer.init()

synth_c = pygame.mixer.Sound('synth_notes/synth_C.wav')
synth_d = pygame.mixer.Sound('synth_notes/synth_D.wav')
synth_e = pygame.mixer.Sound('synth_notes/synth_E.wav')
synth_f = pygame.mixer.Sound('synth_notes/synth_F.wav')
synth_g = pygame.mixer.Sound('synth_notes/synth_G.wav')
synth_a = pygame.mixer.Sound('synth_notes/synth_A.wav')
synth_b = pygame.mixer.Sound('synth_notes/synth_B.wav')

from gpiozero import Button

synth_c_btn = Button(21)
synth_d_btn = Button(20)
synth_e_btn = Button(16)
synth_f_btn = Button(12)
synth_g_btn = Button(26)
synth_a_btn = Button(19)
synth_b_btn = Button(13)

sleepTime = 0.25


while True:
    synth_c_btn.when_pressed = synth_c.play
    if synth_c_btn.is_pressed:
        GPIO.output(18,GPIO.HIGH)
        time.sleep(sleepTime)
        GPIO.output(18,GPIO.LOW)

    synth_d_btn.when_pressed = synth_d.play
    if synth_d_btn.is_pressed:
        GPIO.output(23,GPIO.HIGH)
        time.sleep(sleepTime)
        GPIO.output(23,GPIO.LOW)

    synth_e_btn.when_pressed = synth_e.play
    if synth_e_btn.is_pressed:
        GPIO.output(24,GPIO.HIGH)
        time.sleep(sleepTime)
        GPIO.output(24,GPIO.LOW)

    synth_f_btn.when_pressed = synth_f.play
    if synth_f_btn.is_pressed:
        GPIO.output(25,GPIO.HIGH)
        time.sleep(sleepTime)
        
    synth_g_btn.when_pressed = synth_g.play
    if synth_g_btn.is_pressed:
        GPIO.output(8,GPIO.HIGH)
        time.sleep(sleepTime)
        GPIO.output(8,GPIO.LOW)

    synth_a_btn.when_pressed = synth_a.play
    if synth_a_btn.is_pressed:
        GPIO.output(7,GPIO.HIGH)
        time.sleep(sleepTime)
        GPIO.output(7,GPIO.LOW)

    synth_b_btn.when_pressed = synth_b.play
    if synth_b_btn.is_pressed:
        GPIO.output(6,GPIO.HIGH)
        time.sleep(sleepTime)
        GPIO.output(6,GPIO.LOW)
