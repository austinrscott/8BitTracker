'''
synths is a module which uses pygame audio functions to synthesize waveforms.
'''
__author__ = 'Austin Scott'

import sys

import pygame
import numpy as np

# Sets a constant samplerate for the whole project
SAMPLERATE = 22050

# Tells the pygame.sndarray engine that we are using numpy arrays
pygame.sndarray.use_arraytype('numpy')

def make_beep(frequency, duration):
    '''Synthesizes a square wave from a numpy array.

    :param frequency: Frequency of the note in Hz
    :param duration: Duration of the note in seconds
    :return: pygame.mixer.Sound object
    '''

    # Creates the waveform's period, measured by the number of sound samples it spans across.
    wave_period = SAMPLERATE / frequency

    # Creates a numpy array representing one of those waves.
    wave = np.zeros(wave_period, np.int16)
    wave[0:wave_period/2] = -32767
    wave[wave_period/2:-1] = 32767

    # Multiplies the array until it reaches the desired duration.
    total_sample_length = (duration * SAMPLERATE)
    wave_list = [wave for i in range(int(total_sample_length / wave_period))]
    final_wave = np.concatenate(wave_list)

    # Returns the pygame.mixer.Sound object.
    return pygame.sndarray.make_sound(final_wave)
