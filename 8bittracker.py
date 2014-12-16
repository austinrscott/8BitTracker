'''
Main python file. Manages event loops.
'''
__author__ = 'Austin Scott and Samuel Volk'


import sys
import pygame
import gui
import engine

# Init
pygame.mixer.init(engine.synths.SAMPLERATE, -16, 1)
pygame.init()
pygame.display.set_caption("8BitTracker")
screen = gui.init_screen(gui.SCREEN_WIDTH, gui.SCREEN_HEIGHT)

# Testing beep. This one lasts for 100 milliseconds and is at 880Hz (A5).
sound = engine.synths.make_beep(880, .1)

labelName = gui.label(10, 10, "Samuel Volk")

gui.rect(screen.chars, 9, 9, 13, 3, 12, 4, 0)

# Main Loop
while 1:
    # draw screen
    labelName.draw(screen.chars)
    gui.draw_screen(screen.surface, screen.chars)
    pygame.display.flip()

    # events
    for event in pygame.event.get():
        if event.type is pygame.KEYDOWN:

            # Press ESCAPE to exit the program
            if event.key is pygame.K_ESCAPE:
                sys.exit()

            # Press SPACE to hear the synthesized beep
            elif event.key is pygame.K_SPACE:
                sound.play()

# Clean-up
pygame.quit()
