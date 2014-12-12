#!/usr/local/bin/python -tt
# -*- coding: utf-8 -*-
import os, sys, random

def segment(n, shape, phonemes):
	#grab a phoneme from the right category and return it
	pattern = shape[n]
	seg = ""
	onset = int(random.random() * 100) % len(shape[n])
	for i in range(0, len(shape[n][onset])):
		a = int(shape[n][onset][i])
		b = int(random.random() * 100) % len(phonemes[a])
		seg += phonemes[a][b]
	
	return seg
#end segment function def

#ask for name of input file (default = "input.txt")
inn = raw_input("What is the name of your input file? ")
if inn == "":
	inn = "input.txt"

#ask for name of output file (default = "output.txt")
out = raw_input("What is the name of your output file? ")
if out == "":
	out = "output.txt"

#use system time for seed
random.seed(None)

#prepare lists
consonants = []
vowels = []
types = []
syllables = []

#prepare the output file
fout = open(out, 'w')

#extract from input file
with open(inn) as fin:
	#get consonants
	for line in fin:
		list = line.split()
		if list[0][0] == '#':
			break
		elif list[0][0] != '/':
			consonants.append(list)
	#get vowels
	for line in fin:
		list = line.split()
		if list[0][0] == '#':
			break
		elif list[0][0] != '/':
			vowels.append(list)
	#get types
	for line in fin:
		list = line.split()
		if list[0][0] == '#':
			break
		elif list[0][0] != '/':
			types.append(list)
	#get syllables
	for line in fin:
		list = line.split()
		if list[0][0] == '#':
			break
		elif list[0][0] != '/':
			syllables.append(list)

#un-nest the syllable patterns
syllables = syllables[0]

#ask for number of words (default = 100)
i = raw_input("How many words would you like to build? ")
if i == "":
	i = 100
else:
	i = (int(float(i)))

while i > 0:
	#working word variable
	word = ""
	#create word in this loop
	for j in range(0, int(random.triangular(0,6,1.8)) + 1):
		#working syllable variable
		syll = ""
		#choose a random syllable pattern to follow
		form = syllables[int(random.random() * 100) % len(syllables)]
		for k in range(0, len(form)):
			if form[k] == "O":
				#retrieve a string that is a valid onset
				syll += segment(0, types, consonants)
			elif form[k] == "C":
				#retrieve a string that is a valid coda
				syll += segment(2, types, consonants)
			elif form[k] == "N":
				#retrieve a string that is a valid nucleus
				syll += segment(1, types, vowels)
		#add new syllable to the word		
		word += syll
	#print out the word followed by a newline
	fout.write(word)
	fout.write('\n')
	#decrement loop iterator
	i -= 1
#end while, end program
