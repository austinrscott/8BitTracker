'''
timeline.py will manage the project timeline, which holds all data about the current song.
'''
__author__ = 'Austin Scott and Samuel Volk'


class song():
    def __init__(self):
        self.length = 0
        self.data = [[], [], []]    # three channels

    def clear(self):
        self.length = 0
        self.data = []
