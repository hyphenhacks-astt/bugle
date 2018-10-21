# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np

allKeys = []
song = []

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

def pickNote(key, chord, n, m):
    rand = 5*n
    if(rand<=2):
        length = 1
    elif(rand<=4):
        length = .5
    elif(rand <=5):
        length = 2
    
    possible = [allKeys[key][chord], allKeys[key][chord+2], allKeys[key][chord+4]]
    pitch = possible[np.floor(3*m)]
    
    return([pitch, length])

def writePhrase(timeSig, n):
    phraseCurrent = []
    phraseLength = timeSig*(np.ceil(3*n))
    phraseLengthCurrent = 0
    while(phraseLengthCurrent<phraseLength):
        noteCurrent = pickNote()
        if(phraseLengthCurrent+noteCurrent.length<phraseLength):
            phraseCurrent.append(noteCurrent)
            phraseLengthCurrent += noteCurrent[1]
        else:
            song.append(phraseCurrent)
            

def pickTempo(n):
    return(int(np.floor(100*n+80)))

temp = np.random.random()
timeSig = pickTimeSig(temp)

temp = np.random.random()
key = pickKey(temp)

temp = np.random.random()
tempo = pickTempo(temp)

addKeys(allKeys)