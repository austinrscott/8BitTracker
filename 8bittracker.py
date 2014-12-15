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

# set test data
screen.chars[0][0] = [1, 14, 0]
screen.chars[24][79] = [4, 12, 0]
screen.chars[0][40] = [3, 9, 7]

string = ""
for i in xrange(36):
    string += chr(i)
gui.printl(screen.chars, string, 1, 0)
gui.printl(screen.chars, "0 1 2 3 4 5 6 7 8 9", 3, 5, 5)
gui.printl(screen.chars, "Hello, World!")


# Testing beep. This one lasts for 100 milliseconds and is at 880Hz (A5).
sound = engine.synths.make_beep(880, .1)

gui.line(screen.chars, '*', 5, 2, 5, 5, 20, 14)

# Main Loop
while 1:
    # draw screen
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
