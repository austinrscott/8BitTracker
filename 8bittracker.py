#!/usr/bin/python

'''
Main python file. Manages event loops.
'''
__author__ = 'Austin Scott and Samuel Volk'


import sys
import pygame
import gui
import engine


FPS_LIMIT = 30 # frames per second

# Init
pygame.mixer.init(engine.synths.SAMPLERATE, -16, 1)
pygame.init()
pygame.display.set_caption("8BitTracker")
screen = gui.init_screen(gui.SCREEN_WIDTH, gui.SCREEN_HEIGHT)

# Testing beep. This one lasts for 100 milliseconds and is at 880Hz (A5).
sound = engine.synths.make_beep(880, .1)

labelFPS = gui.label(0, 24, "60 fps")

buttonAccept = gui.button(10, 15, "Accept", 0, 8, False)

gui.rect(screen.chars, 9, 9, 13, 3, 12, 4, 0)

lastRefresh = 0
currentFPS = 0
# Main Loop
while 1:
    # events
    for event in pygame.event.get():
        if event.type is pygame.KEYDOWN:

            # Press ESCAPE to exit the program
            if event.key is pygame.K_ESCAPE:
                sys.exit()

            # Press SPACE to hear the synthesized beep
            elif event.key is pygame.K_SPACE:
                sound.play()

    # draw screen
    labelFPS.text = str(currentFPS)
    labelFPS.draw(screen.chars)
    buttonAccept.draw(screen.chars)
    gui.draw_screen(screen.surface, screen.chars)
    # delay if next frame doesn't need to be up yet (for framerate)
    while ((pygame.time.get_ticks() - lastRefresh) < 1/1000*FPS_LIMIT):
        pass

    pygame.display.flip()
    currentFPS = 1000 / (pygame.time.get_ticks() - lastRefresh)
    lastRefresh = pygame.time.get_ticks()

# Clean-up
pygame.quit()
