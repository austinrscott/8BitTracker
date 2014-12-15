import pygame
from pygame.locals import *

from cp437 import cp437

__author__ = 'Austin Scott and Samuel Volk'


# Constants
FONT_WIDTH = 8
FONT_HEIGHT = 12
SCREEN_WIDTH = FONT_WIDTH * 80
SCREEN_HEIGHT = FONT_HEIGHT * 25

COLOR = [
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

class screen():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.chars = []
        for row in range(self.height):
            self.chars.append([])
            for col in range(self.width):
                self.chars[row].append([0,0,0])

        self.surface = pygame.display.set_mode((self.width, self.height))


def init_screen(width, height):
    """Starts a fake terminal screen
    :return: screen object
    """
    scr = screen(width, height)
    return scr


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
                        pixelarray[x2][y] = COLOR[char[1]]
                    else:
                        pixelarray[x2][y] = COLOR[char[2]]
            del pixelarray
            screen.blit(char_surface, dest)

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
