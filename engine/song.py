#!/usr/bin/env python

'''song.py: Manages the currently opened song. Holds all data about the current song in a time-related form.'''

__author__ = 'Austin Scott'

# 8BITMUSH PLAY DOCUMENTATION (FOR REFERENCE) --------------------------------------------------------------------------

# PLAY(<score>)
#
#  PLAY will play music according to the ANSI Music format outlined below.
#
#  If PLAY() is called with the same <score> two or more times, the music
#  will be queued up to loop over again when the score is complete. This can be
#  done as many times as you like.
#
#  If play() is called with a new score, the music will stop and start
#  playing the new score immediately.
#
#  The exception to this rule is in using the SFX channel (MX), which will
#  play its score independently of the Foreground (MF) and Background (MB)
#  channels.
#
#  It is not recommended to use the SFX channel as a part of your musical scores since it may be interrupted often.
#
#  Mode commands:
#  MF Plays music on the foreground channel. (default)
#  MB Plays music on the background channel.
#  MX Plays music on the SFX channel.
#
#  Octave and tone commands:
#  O<octave> Sets the current octave (0 - 6).
#  < or > Moves up or down one octave.
#  A - G Plays the specified note in the current octave.
#  N<note> Plays a specified note (0 - 84) in the seven-octave
#  range (0 is a rest).
#
#  Duration and tempo commands:
#  L<length> Sets the length of each note (1 - 64). L1 is whole note,
#  L2 is a half note, etc. The default is L4 (quarter notes)
#  ML Sets music legato.
#  MN Sets music normal. (default)
#  MS Sets music staccato.
#  P<pause> Specifies a pause (1 - 64). P1 is a whole-note pause,
#  P2 is a half-note pause, etc.
#  T<tempo> Sets the tempo in quarter notes per minute (32 - 255).
#  R Repeats the MF and MB channels.
#
#  Suffix commands:
#  # or + Turns preceding note into a sharp.
#  - Turns preceding note into a flat.
#  . Plays the preceding note 3/2 as long as specified.
#
#  Examples:
#  > th [play(MFcdefgab>c)]

# ----------------------------------------------------------------------------------------------------------------------

class Song(object):
    '''Song: The overarching class which holds all data about a song.'''
    pass

class Note(object):
    '''Note: Represents a note.'''

    def __init__(self, tone, length):
        """Initializes a Note object.

        :param tone: Must be a number between 0 and 84. If 0 is given, the Note is a rest.
        :param length: The actual duration of the note (measured in tracker frames instead of traditional notation).
        """
        self.tone = tone
        self.length = length

class Rest(Note):
    '''Rest: Represents a rest.'''

    def __init__(self, length):
        """Initializes a Rest object.

        :param length: The actual duration of the rest (measured in tracker frames instead of traditional notation).
        """
        super().__init__(0, length)

class SongEvent(object):
    '''SongEvent: Represents a change of settings in the song. '''
    pass