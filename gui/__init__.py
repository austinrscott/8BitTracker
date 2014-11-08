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
    for row in xrange(25):
        for col in xrange(80):
            char = screen_array[row][col]
            #print char
            dest = Rect(col * FONT_WIDTH, row * FONT_HEIGHT, FONT_WIDTH,
                        FONT_HEIGHT)
            # draw bg colour
            #pygame.draw.rect(screen, colour[screen_array[row][col][2]], dest)
            # draw char
            char_surface = pygame.Surface((FONT_WIDTH, FONT_HEIGHT))
            pixelarray = pygame.PixelArray(char_surface)
            #print screen_array[row][col]
            for y in xrange(FONT_HEIGHT):
                for x in xrange(FONT_WIDTH):
                    x2 = 7 - x
                    if (cp437[char[0]][y] & (1<<x)):
                        pixelarray[x2][y] = colour[char[1]]
                    else:
                        pixelarray[x2][y] = colour[char[2]]
            #pixelarray[0:100] = (255, 255, 255)
            #pixelarray[:8] = (255, 0, 0)
            del pixelarray
            screen_surface.blit(char_surface, dest)
            #pygame.display.flip()
            #pygame.time.wait(100)

def printline(screen_array, text, row=0, col=0, fg=7, bg=0):
    for i, char in enumerate(text):
        screen_array[row][col+i] = [ord(char), fg, bg]
        #print ord(char)



# Init
pygame.init()
screen_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PyMUSH")
# Create character array to hold chars to be displayed and the colours (FG & BG)
screen_chars = []
for row in range(SCREEN_HEIGHT):
    screen_chars.append([])
    for col in range(SCREEN_WIDTH):
        screen_chars[row].append([0,0,0])

time_start = pygame.time.get_ticks()

# Main Loop

# set test data
screen_chars[0][0] = [1, 14, 0]
screen_chars[24][79] = [4, 12, 0]
screen_chars[0][40] = [3, 9, 7]

string = ""
for i in xrange(36):
    string += chr(i)
printline(screen_chars, string, 1, 0)
printline(screen_chars, "0 1 2 3 4 5 6 7 8 9", 3, 5, 5)
printline(screen_chars, "Hello, World!")


# draw screen
draw_screen(screen_surface, screen_chars)

pygame.display.flip()
time_end = pygame.time.get_ticks()
print 'Took', time_start - time_end, 'ticks.'
pygame.time.delay(10000)

# Clean-up
pygame.quit()
