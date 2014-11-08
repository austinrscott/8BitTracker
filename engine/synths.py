#!/usr/bin/env python

'''synths.py: A module which uses pygame audio functions to synthesize waveforms.'''

__author__ = 'Austin Scott'

import pygame.mixer
import pygame.sndarray

import numpy as np

# The samplerate used by the synths
SOUND_SAMPLERATE = 22050

# Initialize the pygame mixer with our project samplerate, 16bits of data per sample (with negative integers) and mono
pygame.mixer.init(SOUND_SAMPLERATE, -16, 1)

# Tells the pygame.sndarray engine that we are using numpy arrays
pygame.sndarray.use_arraytype('numpy')

def make_beep(frequency, duration):
    '''Synthesizes a square wave from a numpy array.

    :param frequency: Frequency of the note in Hz
    :param duration: Duration of the note in seconds
    :return: pygame.mixer.Sound object
    '''

    # Creates the waveform's period, measured by the number of sound samples it spans across.
    wave_period = SOUND_SAMPLERATE / frequency

    # Creates a numpy array representing one of those waves.
    wave = np.zeros(wave_period, np.int16)
    wave[0:wave_period/2] = -32767
    wave[wave_period/2:-1] = 32767

    # Multiplies the array until it reaches the desired duration.
    total_sample_length = (duration * SOUND_SAMPLERATE)
    wave_list = [wave for i in range(int(total_sample_length / wave_period))]
    final_wave = np.concatenate(wave_list)

    # Returns the pygame.mixer.Sound object.
    return pygame.sndarray.make_sound(final_wave)

# Testing beep. This one lasts for 100 milliseconds and is at 880Hz (A5).
sound = make_beep(880, .1)