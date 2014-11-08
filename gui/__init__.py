import pygame
from pygame.locals import *

from cp437 import cp437

__author__ = 'Austin Scott and Samuel Volk'


# Constants
FONT_WIDTH = 8
FONT_HEIGHT = 12
SCREEN_WIDTH = FONT_WIDTH * 80
SCREEN_HEIGHT = FONT_HEIGHT * 25

colour = [
    (0, 0, 0),
    (168, 0, 0),
    (0, 168, 0),
    (168, 84, 0),
    (0, 0, 168),
    (168, 0, 168),
    (0, 168, 168),
    (168, 168, 168),
    (84, 84, 84),
    (255, 84, 84),
    (84, 255, 84),
    (255, 255, 84),
    (84, 84, 255),
    (255, 84, 255),
    (84, 255, 255),
    (255, 255, 255)
]


def draw_screen(screen, screen_array):
    """Draws the fake terminal screen

    :param screen:
    :param screen_array: Array holding the current screen data
    :return: None
    """
    for row in xrange(25):
        for col in xrange(80):
            char = screen_array[row][col]
            dest = Rect(col * FONT_WIDTH, row * FONT_HEIGHT, FONT_WIDTH,
                        FONT_HEIGHT)
            # draw bg colour
            #pygame.draw.rect(screen, colour[screen_array[row][col][2]], dest)
            # draw char
            char_surface = pygame.Surface((FONT_WIDTH, FONT_HEIGHT))
            pixelarray = pygame.PixelArray(char_surface)

            for y in xrange(FONT_HEIGHT):
                for x in xrange(FONT_WIDTH):
                    x2 = 7 - x
                    if (cp437[char[0]][y] & (1<<x)):
                        pixelarray[x2][y] = colour[char[1]]
                    else:
                        pixelarray[x2][y] = colour[char[2]]
            del pixelarray
            screen_surface.blit(char_surface, dest)

def printl(screen_array, text, row=0, col=0, fg=7, bg=0):
    """Prints a line of text on the screen.

    :param screen_array: The screen array
    :param text: Text to write
    :param row: Row number
    :param col: Column number
    :param fg: foreground color
    :param bg: background color
    :return: None
    """
    for i, char in enumerate(text):
        screen_array[row][col+i] = [ord(char), fg, bg]
        #print ord(char)



# Init
pygame.init()
screen_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("8BitTracker")
# Create character array to hold chars to be displayed and the colours (FG & BG)
screen_chars = []
for row in range(SCREEN_HEIGHT):
    screen_chars.append([])
    for col in range(SCREEN_WIDTH):
        screen_chars[row].append([0,0,0])

# Main Loop

# set test data
screen_chars[0][0] = [1, 14, 0]
screen_chars[24][79] = [4, 12, 0]
screen_chars[0][40] = [3, 9, 7]

string = ""
for i in xrange(36):
    string += chr(i)
printl(screen_chars, string, 1, 0)
printl(screen_chars, "0 1 2 3 4 5 6 7 8 9", 3, 5, 5)
printl(screen_chars, "Hello, World!")


# draw screen
draw_screen(screen_surface, screen_chars)
pygame.display.flip()

pygame.time.delay(10000)

# Clean-up
pygame.quit()
