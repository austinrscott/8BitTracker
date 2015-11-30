#!/usr/bin/env python

__author__ = 'Samuel Volk'

import argparse, sys
import engine

def readnumber(score, index):
    number = 0
    readchar = score[index]
    while readchar.isdigit():
        # number x 10
        number = number * 10
        # add to number
        number = number + int(char)
        index += 1
        # read char
        readchar = score[index]

    # no number after so return -1
    if number == []:
        return -1
    # normal return
    return number

def parsescore(score):
    score_list = []
    tempo = 120
    channel = 'F'
    length = 4 # ^(-1)
    i = 0
    while i < len(score):
        char = score[i]

        if char == ' ':
            pass
        elif char == 'T':
            #read the number
            temp = readnumber(score, i)
            if temp >= 32 and temp <= 255:
                tempo = temp
            score_list[i][0] = 
        elif char == 'M':
            # read the channel
            i += 1
            channel = score[i]
        elif char == 'O':
            pass
        elif char == 'N':
            pass
        elif char == 'L':
            pass
        elif char == 'P':
            pass

        i += 1

    return score_list


# Parser
parser = argparse.ArgumentParser(description='Play 8bit play() music from a text file.')
parser.add_argument('FILE', nargs='+', type=argparse.FileType('r'), default=sys.stdin,
                    help='file to obtain music score from')
args = parser.parse_args()
scorefiles = args.FILE
scores = []
for i, file in enumerate(scorefiles):
    scores.append(scorefiles[i].read())

# run through each score and parse it into a list format
print parsescore(scores[0])
