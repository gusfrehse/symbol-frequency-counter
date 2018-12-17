#!/usr/bin/env python3

import sys

if (len(sys.argv) < 2):
    print("Usage: main.py <pathToInputFile>")
    quit(1)

with open(sys.argv[1]) as f:
    txt = f.read()

characters = {}
numOfChars = len(txt)

for c in txt:
    if c not in characters:
        characters[c] = 1
    else:
        characters[c] += 1

for k,v in characters.items():
    characters[k]  = v / numOfChars
    print(f"{characters[k]} {k}")
