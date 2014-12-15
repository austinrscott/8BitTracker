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
screen_surface = pygame.display.set_mode((gui.SCREEN_WIDTH, gui.SCREEN_HEIGHT))
pygame.display.set_caption("8BitTracker")
# Create character array to hold chars to be displayed and the colours (FG & BG)
screen_chars = []
for row in range(gui.SCREEN_HEIGHT):
    screen_chars.append([])
    for col in range(gui.SCREEN_WIDTH):
        screen_chars[row].append([0,0,0])

# set test data
screen_chars[0][0] = [1, 14, 0]
screen_chars[24][79] = [4, 12, 0]
screen_chars[0][40] = [3, 9, 7]

string = ""
for i in xrange(36):
    string += chr(i)
gui.printl(screen_chars, string, 1, 0)
gui.printl(screen_chars, "0 1 2 3 4 5 6 7 8 9", 3, 5, 5)
gui.printl(screen_chars, "Hello, World!")


# Testing beep. This one lasts for 100 milliseconds and is at 880Hz (A5).
sound = engine.synths.make_beep(880, .1)

# Main Loop
while 1:
    # draw screen
    gui.draw_screen(screen_surface, screen_chars)
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
