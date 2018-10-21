# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import math
from midiutil import MIDIFile

totalSongLength = 0

chordWeights = (
    (4,1,4,1,4,1,1), #root
    (4,4,4,1,4,1,1), #2nd
    (4,1,4,4,4,1,4), #3rd
    (2,1,2,4,4,1,1), #4th
    (4,1,4,1,4,4,1), #5th
    (2,1,1,1,4,4,4), #6th
    (4,1,4,1,4,3,4)  #7th
)

allKeys = [] #allKeys is a list of lists, each list is a series of MIDI tones
song = []
np.random.seed(None)

timeSigRandom = np.random.random()
keyRandom = np.random.random()
tempoRandom = np.random.random()
numberOfPhrases = np.random.random()

def randomChoice(choices, weights):
    # [(choice, weight)]
    wtot = 0
    for c, w in zip(choices, weights):
        wtot += w
    r = np.random.random() * wtot
    for c, w in zip(choices, weights):
        r -= w
        if r <= 0:
            return c

def writeProgression():
    chords = []
    last = randomChoice(range(0,7),(8,1,2,1,4,1,1))
    for x in range(0,128):
        chords.append(randomChoice(range(0,7),chordWeights[last]))
    return chords

def pickTimeSig(n):
    return(int(math.floor(3*n+3)))

def pickKey(n):
    return(int(math.floor(12*n)))
    
def addKeys(n):
    for i in range(12):
        temp = []
        temp.append(60+i)
        temp.append(62+i)
        temp.append(64+i)
        temp.append(65+i)
        temp.append(67+i)
        temp.append(69+i)
        temp.append(71+i)
        n.append(temp)
    for i in range(12):
        temp = []
        temp.append(60+i)
        temp.append(62+i)
        temp.append(63+i)
        temp.append(65+i)
        temp.append(67+i)
        temp.append(68+i)
        temp.append(70+i)
        n.append(temp)

def pickNote(key, chord, songLength):
    rand = 5*np.random.random()
    if(rand<=2):
        length = 1
    elif(rand<=4):
        length = .5
    elif(rand <=5):
        length = 2
    
    if(key>11):
        possible = [allKeys[key][chord], allKeys[key][chord]+3, allKeys[key][chord]+7]
    else:
        possible = [allKeys[key][chord], allKeys[key][chord]+4, allKeys[key][chord]+7]
    pitch = possible[math.floor(3*np.random.random())]
    
    return([0, 0, pitch, songLength, length, 100])

def currentChord(l):
    return(progression[math.floor(l/2)])

def pickTempo(n):
    return(int(math.floor(100*n+80)))

timeSig = pickTimeSig(timeSigRandom)

key = pickKey(keyRandom) #key is a number between 0 and 23

tempo = pickTempo(tempoRandom)

addKeys(allKeys)

progression = writeProgression()
for i in range(16):
    phraseCurrent = []
    phraseLength = 2*timeSig*(math.ceil(2*np.random.random()))
    phraseLengthCurrent = 0
    while(phraseLengthCurrent<phraseLength):
        noteCurrent = pickNote(key, currentChord(totalSongLength), totalSongLength)
        if(phraseLengthCurrent+noteCurrent[4]<phraseLength):
            phraseCurrent.append(noteCurrent)
            phraseLengthCurrent += noteCurrent[4]
            totalSongLength += noteCurrent[4]
        else:
            song.append(phraseCurrent)
            break

finalMIDI = MIDIFile(2)
finalMIDI.addTempo(0, 0, tempo)
finalMIDI.addTempo(1, 0, tempo)

for phrase in song:
    for note in phrase:
        finalMIDI.addNote(note[0], note[1], note[2], note[3], note[4], note[5])

with open("major-scale.mid", "wb") as output_file:
    finalMIDI.writeFile(output_file)