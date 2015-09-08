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
                self.chars[row].append([0,0,0,False])

        self.surface = pygame.display.set_mode((self.width, self.height))

# Widgets

class label():
    def __init__(self, x=0, y=0, text="default", fg=7, bg=0):
        self.x = x
        self.y = y
        self.text = text
        self.fg = fg
        self.bg = bg
    def draw(self, screen_array):
        printl(screen_array, self.text, self.x, self.y, self.fg, self.bg)

class button(label):
    def __init__(self, x=0, y=0, text="default", fg=7, bg=0, border=False):
        self.x = x
        self.y = y
        self.text = text
        self.fg = fg
        self.bg = bg
        self.border = border
        #self.event = pygame.event.Event(MOUSEBUTTONDOWN)

    def draw(self, screen_array):
        #if self.border == False:
        #    rect(screen_array, self.x-1, self.y-1, len(self.text)+2, 3, self.fg, self.bg, 1);

        printl(screen_array, self.text, self.x, self.y, self.fg, self.bg)


def init_screen(width, height):
    """Starts a fake terminal screen
    :return: screen object
    """
    scr = screen(width, height)
    return scr


def draw_screen(screen, screen_array):
    """Draws the fake terminal screen

    :param screen: The screen surface
    :param screen_array: Array holding the current screen data
    :return: None
    """
    char_surface = pygame.Surface((FONT_WIDTH, FONT_HEIGHT))
    for row in xrange(25):
        for col in xrange(80):
            char = screen_array[row][col]
            dest = Rect(col * FONT_WIDTH, row * FONT_HEIGHT, FONT_WIDTH,
                        FONT_HEIGHT)
            # draw bg colour
            #pygame.draw.rect(screen, colour[screen_array[row][col][2]], dest)
            # draw char
            if char[3]: # if character has changed draw it
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
                char[3] = False
            char_surface.fill((0,0,0))

def printl(screen_array, text, col=0, row=0, fg=7, bg=0):
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
        screen_array[row][col+i] = [ord(char), fg, bg, True]

def line(screen_array, x0, y0, x1, y1, char, fg, bg):
    # Modified: http://rosettacode.org/wiki/Bitmap/Bresenham%27s_line_algorithm#Python
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    x, y = x0, y0
    sx = -1 if x0 > x1 else 1
    sy = -1 if y0 > y1 else 1
    if dx > dy:
        err = dx / 2.0
        while x != x1:
            printl(screen_array, char, y, x, fg, bg)
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
    else:
        err = dy / 2.0
        while y != y1:
            printl(screen_array, char, y, x, fg, bg)
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy
    printl(screen_array, char, y, x, fg, bg)

def rect(screen_array, x, y, w, h, fg, bg, border):
    char = 32 # space
    for row in xrange(h):
        for col in xrange(w):
            if border == 1:
                # top left corner
                if row == 0 and col == 0:
                    char = 218
                # top right corner
                elif row == 0 and col == w-1:
                    char = 191
                # bottom left corner
                elif row == h-1 and col == 0:
                    char = 192
                # bottom right corner
                elif row == h-1 and col == w-1:
                    char = 217
                # top & bottom edges
                elif row == 0 or row == h-1:
                    char = 196
                # side edge
                elif col == 0 or col == w-1:
                    char = 179
                else:
                    char = 32 # space

            # put char into array
            screen_array[x + row][y + col][0] = char
            screen_array[x + row][y + col][1] = fg
            screen_array[x + row][y + col][2] = bg
            screen_array[x + row][y + col][3] = True
