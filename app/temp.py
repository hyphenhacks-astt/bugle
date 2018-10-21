# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np

allKeys = []
song = []

timeSigRandom = np.random.seed()
keyRandom = np.random.seed()
tempoRandom = np.random.seed()
numberOfPhrases = np.random.seed()

def pickTimeSig(n):
    return(int(np.floor(4*n+2)))

def pickKey(n):
    return(int(np.floor(12*n)))
    
def addKeys(n):
    for i in range(12):
        temp = []
        temp.append(60+i)
        temp.append(62+1)
        temp.append(64+i)
        temp.append(65+i)
        temp.append(67+i)
        temp.append(69+i)
        temp.append(71+i)
        temp.append(72+i)
        n.append(temp)
    for i in range(12):
        temp = []
        temp.append(60+i)
        temp.append(62+1)
        temp.append(63+i)
        temp.append(65+i)
        temp.append(67+i)
        temp.append(68+i)
        temp.append(70+i)
        temp.append(72+i)
        n.append(temp)

def pickNote(key, chord, i, j):
    rand = 5*i
    if(rand<=2):
        length = 1
    elif(rand<=4):
        length = .5
    elif(rand <=5):
        length = 2
    
    if(key>11):
        possible = [allKeys[key][chord], allKeys[key][chord]+4, allKeys[key][chord]+7]
    else:
        possible = [allKeys[key][chord], allKeys[key][chord]+3, allKeys[key][chord]+7]
    pitch = possible[np.floor(3*j)]
    
    return([pitch, length])

def writePhrase(timeSig, n, key, chord):
    phraseCurrent = []
    phraseLength = timeSig*(np.ceil(3*n))
    phraseLengthCurrent = 0
    while(phraseLengthCurrent<phraseLength):
        noteCurrent = pickNote(key, chord, np.random.random(), np.random.random())
        if(phraseLengthCurrent+noteCurrent.length<phraseLength):
            phraseCurrent.append(noteCurrent)
            phraseLengthCurrent += noteCurrent[1]
        else:
            song.append(phraseCurrent)

def writeSong(n, timeSig, key, chord):
    numPhrases = 4*(np.ceil(8*n)+8)
    for i in range(numPhrases):
        writePhrase(timeSig, np.random.random(), key, chord)

def pickTempo(n):
    return(int(np.floor(100*n+80)))

timeSig = pickTimeSig(timeSigRandom)

key = pickKey(keyRandom)

tempo = pickTempo(tempoRandom)

addKeys(allKeys)