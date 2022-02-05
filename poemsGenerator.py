#!/usr/bin/python3

import random
import requests
import sys

def randomWikipediaTitle():
    S = requests.Session()
    URL = "https://en.wikipedia.org/w/api.php"
    PARAMS = {
        "action": "query",
        "format": "json",
        "list": "random",
        "rnnamespace": "0"
    }
    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()
    return DATA["query"]["random"][0]["title"]

# reads input in format
# (empty line)
# N (integer)
# first line
# second line
# ...
# N-th line 
def readOneTable():
    sys.stdin.readline()
    choicesNr = int(sys.stdin.readline())
    lines = []
    for i in range(choicesNr):
        lines.append(sys.stdin.readline())
    return lines

# linesList - [[line11, line12, line13, ...], [line21, line22, ...], ...]
# returns such a string:
# Poem about [random title name from Wikipedia]
# random line from [line11, line12, ...]
# random line from [line21, line22, ...]
# ...
# random line from [lineN1, lineN2, ...]
def randomPoem(linesList):
    poem = "Poem about " + randomWikipediaTitle() + "\n"
    for l in linesList:
        poem += random.choice(l)
    poem = poem[:-1]
    return poem

def __main__():
    linesNr = int(sys.stdin.readline())
    lines = []
    for i in range(linesNr):
        lines += [readOneTable()]
    print(randomPoem(lines))

__main__()