#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import os
import pygame
from pygame.locals import *

os.system("pkill raspivid")
time.sleep(1)
os.system("/home/pi/gstream.sh")
GPIO.cleanup()

pinlist = [7, 11, 13, 15, 16]

GPIO.setmode(GPIO.BOARD)

for i in pinlist:
 GPIO.setup(i, GPIO.OUT)

pygame.init()
screen = pygame.display.set_mode((320, 240))
pygame.display.set_caption('Pharlan rc-car')
pygame.mouse.set_visible(1)

print"pygame started"

GPIO.output(7,False)

print "relay turned on"
done = False
while not done:
 for event in pygame.event.get():
  if event.type == KEYDOWN:
   if event.key == (K_UP):
       GPIO.output(16,True)
       GPIO.output(13,True)

   if event.key == (K_DOWN):
       GPIO.output(15,True)
       GPIO.output(11,True)

   if event.key == (K_LEFT):
       GPIO.output(13,True)
       GPIO.output(15,True)

   if event.key == (K_RIGHT):
       GPIO.output(16,True)
       GPIO.output(11,True)

  if event.type == KEYUP:
   if event.key == (K_UP):
       GPIO.output(16,False)
       GPIO.output(13,False)

   if event.key == (K_DOWN):
       GPIO.output(15,False)
       GPIO.output(11,False)

   if event.key == (K_LEFT):
       GPIO.output(13,False)
       GPIO.output(15,False)

   if event.key == (K_RIGHT):
       GPIO.output(16,False)
       GPIO.output(11,False)


   if (event.key == K_ESCAPE):
       done = True

os.system("pkill raspivid")
GPIO.output(7,True)
print "relay turned off"
GPIO.cleanup()
