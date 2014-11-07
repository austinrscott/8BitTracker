'''
synths is a module which uses pygame audio functions to synthesize waveforms.
'''
__author__ = 'Austin Scott'

import sys

import pygame
import numpy as np

# Sets a constant samplerate for the whole project
SOUND_SAMPLERATE = 22050

pygame.mixer.init(SOUND_SAMPLERATE, -16, 1)
pygame.init()

# Tells the pygame.sndarray engine that we are using numpy arrays
pygame.sndarray.use_arraytype('numpy')

def make_beep(frequency, duration):
    '''Synthesizes a square wave from a numpy array.

    :param frequency: Frequency of the note in Hz
    :param duration: Duration of the note in seconds
    :return: pygame.mixer.Sound object
    '''

    # Creates the waveform's period, measured by the number of sound samples it spans across.
    wave_period = SOUND_SAMPLERATE // frequency

    # Creates a numpy array representing one of those waves.
    wave = np.zeros(wave_period, np.int16)
    wave[0:wave_period//2] = -32767
    wave[wave_period//2:-1] = 32767

    # Multiplies the array until it reaches the desired duration.
    total_sample_length = (duration * SOUND_SAMPLERATE) // 1
    wave_list = [wave for i in range((total_sample_length // wave_period))]
    final_wave = np.concatenate(wave_list)

    # Returns the pygame.mixer.Sound object.
    return pygame.sndarray.make_sound(final_wave)

# Testing beep. This one lasts for one second and is at 880Hz (A5).
sound = make_beep(880, 1)

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
                sound.play()