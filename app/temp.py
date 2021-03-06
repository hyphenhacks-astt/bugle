# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#TODO: beats, diff for a and b

import math
from midiutil import MIDIFile
import hashlib
import random
import os

def createMidiFile(s=None,swing=True):
    partLength = 0

    chordWeights = (
        (2,1,4,1,4,1,1), #root
        (4,1,4,1,4,1,1), #2nd
        (4,1,2,4,4,1,4), #3rd
        (2,1,2,2,4,1,1), #4th
        (4,1,4,1,2,4,1), #5th
        (2,1,1,1,4,1,4), #6th
        (4,1,4,1,4,3,2)  #7th
    )

    allKeys = [] #allKeys is a list of lists, each list is a series of MIDI tones
    A = []
    B = []
    #h = hashlib.sha256()
    #h.update(s.encode('utf-8'))
    random.seed(s)

    timeSigRandom = random.random()
    keyRandom = random.random()
    tempoRandom = random.random()
    numberOfPhrases = random.random()

    def randomChoice(choices, weights):
        # [(choice, weight)]
        wtot = 0
        for c, w in zip(choices, weights):
            wtot += w
        r = random.random() * wtot
        for c, w in zip(choices, weights):
            r -= w
            if r <= 0:
                return c

    def pickForm():
        return randomChoice(
            (('A','B','A'),
            ('A','B','A','B'),
            ('A','A','B','B'),
            ('A','B','B','A')),
            (1,1,1,1))


    def writeProgression(timeSig, isA):
        if(isA):
            if(timeSig==3):
                chords = [0]
            elif(timeSig==4):
                chords = [0, 0]
            elif(timeSig==5):
                chords = [0, 0, 0]
        else:
            if(timeSig==3):
                chords = [5]
            elif(timeSig==4):
                chords = [5, 5]
            elif(timeSig==5):
                chords = [5, 5, 5]
        last = 0
        x = len(chords)
        print(chords)
        while len(chords) < 100:
            x = len(chords)
            tone = randomChoice(range(0,7),chordWeights[last])
            if timeSig == 3:
                if x % 3 == 0:
                    chords.append(tone)
                elif x % 3 == 1:
                    chords.append(tone)
                    chords.append(tone)
                else:
                    continue
                last = tone
            elif timeSig == 4:
                if x % 2 == 0:
                    chords.append(tone)
                    chords.append(tone)
                else:
                    continue
                last = tone
            else:
                if x % 5 == 0:
                    chords.append(tone)
                    chords.append(tone)
                    chords.append(tone)
                elif x % 5 == 3:
                    chords.append(tone)
                    chords.append(tone)
                else:
                    continue
                last = tone
        print(chords)
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

    def pickNote(key, currentChord, nextChord, songLength, swing):
        rand = 5*random.random()
        offset = 0
        if(rand<=2):
            length = 1
        elif(rand<=4):
            if(swing):
                if(songLength%1==0):
                    length = .67
                else:
                    length=.33
            else:
                length = .5
        elif(rand <=5):
            length = 2
        
        if(length < 0.5):
            pitch = randomChoice(
                (allKeys[key][currentChord],
                allKeys[key][currentChord+1-7],
                allKeys[key][currentChord+2-7],
                allKeys[key][currentChord+3-7],
                allKeys[key][currentChord+4-7],
                allKeys[key][currentChord+5-7],
                allKeys[key][currentChord+6-7]),(4,1,4,3,4,2,1)) #TODO: Use chordWeights?
        else:
            pitch = randomChoice(
                (allKeys[key][nextChord],
                allKeys[key][nextChord+1-7],
                allKeys[key][nextChord+2-7],
                allKeys[key][nextChord+3-7],
                allKeys[key][nextChord+4-7],
                allKeys[key][nextChord+5-7],
                allKeys[key][nextChord+6-7]),(4,0,4,0,4,0,0)) #TODO: Use chordWeights?
        #pitch = randomChoice(allKeys[key],(4,1,4,2,4,2,3)) #what if...
        return([0, 0, pitch, songLength+offset, length, 100])

    def pickTempo(n):
        return(int(math.floor(100*n+80)))

    timeSig = pickTimeSig(timeSigRandom)

    key = pickKey(keyRandom) #key is a number between 0 and 23

    tempo = pickTempo(tempoRandom)

    addKeys(allKeys)

    progressiona = writeProgression(timeSig, True)
    alen = 0
    blen = 0
    partLength = 0
    for i in range(2):
        phraseCurrent = []
        phraseLength = 2*timeSig*(math.ceil(2*random.random()))
        phraseLengthCurrent = 0
        while(phraseLengthCurrent<phraseLength):
            noteCurrent = pickNote(key, progressiona[math.floor(partLength)],progressiona[math.floor(partLength)+1], partLength, swing)
            if(phraseLengthCurrent+noteCurrent[4]<phraseLength):
                phraseCurrent.append(noteCurrent)
                phraseLengthCurrent += noteCurrent[4]
                partLength += noteCurrent[4]
            else:
                phraseCurrent[-1][4] += phraseLength-phraseLengthCurrent
                partLength += phraseLength-phraseLengthCurrent
                A.append(phraseCurrent)
                break
    alen = int(partLength)
    progressiona = progressiona[:alen]
    partLength = 0
    progressionb = writeProgression(timeSig, False)
    for i in range(2):
        phraseCurrent = []
        phraseLength = 2*timeSig*(math.ceil(2*random.random()))
        phraseLengthCurrent = 0
        while(phraseLengthCurrent<phraseLength):
            noteCurrent = pickNote(key, progressionb[math.floor(partLength)], progressionb[math.floor(partLength)+1], partLength, swing)
            if(phraseLengthCurrent+noteCurrent[4]<phraseLength):
                phraseCurrent.append(noteCurrent)
                phraseLengthCurrent += noteCurrent[4]
                partLength += noteCurrent[4]
            else:
                phraseCurrent[-1][4] += phraseLength-phraseLengthCurrent
                partLength += phraseLength-phraseLengthCurrent
                B.append(phraseCurrent)
                break
    blen = int(partLength)
    progressionb = progressionb[:blen]

    finalMIDI = MIDIFile(2)
    finalMIDI.addTempo(0, 0, tempo)
    finalMIDI.addTempo(1, 0, tempo)

    print(timeSig)

    form = pickForm()
    print(form)
    totalSongLength = 0

    for part in form:
        if part is 'A':
            progression = progressiona
            for phrase in A:
                for note in phrase:
                    finalMIDI.addNote(note[0], note[1], note[2], note[3]+totalSongLength, note[4], note[5])
            for i, c in enumerate(progression):
                # TODO: Don't play every beat
                finalMIDI.addNote(1,1,allKeys[key][c-7]-12,i+totalSongLength,1,60)
                finalMIDI.addNote(1,1,allKeys[key][c+2-7]-12,i+totalSongLength,1,60)
                finalMIDI.addNote(1,1,allKeys[key][c+4-7]-12,i+totalSongLength,1,60)
            totalSongLength += alen
        else:
            progression = progressionb
            for phrase in B:
                for note in phrase:
                    finalMIDI.addNote(note[0], note[1], note[2], note[3]+totalSongLength, note[4], note[5])
            for i, c in enumerate(progression):
                # TODO: Don't play every beat
                # TODO: anticipate chords on swing?
                finalMIDI.addNote(1,1,allKeys[key][c-7]-12,i+totalSongLength,1,60)
                finalMIDI.addNote(1,1,allKeys[key][c+2-7]-12,i+totalSongLength,1,60)
                finalMIDI.addNote(1,1,allKeys[key][c+4-7]-12,i+totalSongLength,1,60)
            totalSongLength += blen
    finalMIDI.addNote(0,0,allKeys[key][0],totalSongLength,timeSig,100)
    finalMIDI.addNote(1,1,allKeys[key][0]-12,totalSongLength,timeSig,60)
    finalMIDI.addNote(1,1,allKeys[key][2]-12,totalSongLength,timeSig,60)
    finalMIDI.addNote(1,1,allKeys[key][4]-12,totalSongLength,timeSig,60)

    with open("/tmp/out.mid", "wb") as output_file:
        finalMIDI.writeFile(output_file)


if __name__ == "__main__":
    createMidiFile(os.urandom(24))
