#!/usr/bin/env python

'''8bittracker.py: Main python file. Manages event loops.'''

__author__ = 'Austin Scott and Sam Volk'

import sys

import pygame

from engine import synths

# Initialize pygame
pygame.init()

# Initialize the pygame display so that the program can receive keyboard input (requires window focus)
pygame.display.set_mode((640, 480))

while 1:
    for event in pygame.event.get():
        if event.type is pygame.KEYDOWN:

            # Press ESCAPE to exit the program
            if event.key is pygame.K_ESCAPE:
                sys.exit()

            # Press SPACE to hear the synthesized beep
            elif event.key is pygame.K_SPACE:
                synths.sound.play()