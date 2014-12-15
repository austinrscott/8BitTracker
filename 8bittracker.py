'''
Main python file. Manages event loops.
'''
__author__ = 'Austin Scott and Samuel Volk'


import pygame
import gui

# Init
pygame.init()
screen_surface = pygame.display.set_mode((gui.SCREEN_WIDTH, gui.SCREEN_HEIGHT))
pygame.display.set_caption("8BitTracker")
# Create character array to hold chars to be displayed and the colours (FG & BG)
screen_chars = []
for row in range(gui.SCREEN_HEIGHT):
    screen_chars.append([])
    for col in range(gui.SCREEN_WIDTH):
        screen_chars[row].append([0,0,0])

# Main Loop

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


# draw screen
gui.draw_screen(screen_surface, screen_chars)
pygame.display.flip()

pygame.time.delay(10000)

# Clean-up
pygame.quit()
