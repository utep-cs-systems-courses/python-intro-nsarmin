import pickle
import re
import os
file = open("declaration.txt", "r")
data = file.read()
#keeps track of the total the number of times each word occurs in the text file
#print len(words)
for line in file:
    line=file.strip()  #remove the leading spaces and newline characters
    line= line.lower()
    piece=line.split(" ") #split into words
    for word in piece:
        if word in file:
            piece[word]=piece[word]+1
        else:
            piece[word]=1

for key in list(piece.keys()):
    print(key, ":", piece[key])
