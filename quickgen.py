#!/usr/local/bin/python -tt
# -*- coding: utf-8 -*-
import os, sys, random

def segment(n, shape, phonemes):
	#print phonemes
	pattern = shape[n]
	seg = ""
	onset = int(random.random() * 100) % len(shape[n])
	for i in range(0, len(shape[n][onset])):
		a = int(shape[n][onset][i])
		b = int(random.random() * 100) % len(phonemes[a])
		#print "index a = %s, index b = %s" % (a, b)
		seg += phonemes[a][b]
	
	return seg

inn = raw_input("What is the name of your input file? ")
if inn == "":
	inn = "input.txt"

out = raw_input("What is the name of your output file? ")
if out == "":
	out = "output.txt"

random.seed(None)

consonants = []
vowels = []

types = []
syllables = []

fout = open(out, 'w')
with open(inn) as fin:

	for line in fin:
		list = line.split()
		if list[0][0] == '#':
			break
		elif list[0][0] != '/':
			consonants.append(list)
	
	for line in fin:
		list = line.split()
		if list[0][0] == '#':
			break
		elif list[0][0] != '/':
			vowels.append(list)
	
	for line in fin:
		list = line.split()
		if list[0][0] == '#':
			break
		elif list[0][0] != '/':
			types.append(list)
	
	for line in fin:
		list = line.split()
		if list[0][0] == '#':
			break
		elif list[0][0] != '/':
			syllables.append(list)

syllables = syllables[0]

#print "The first class of consonants contains: %s" % consonants[0]
#print "The second class of consonants contains: %s" % consonants[1]
#print "The third class of consonants contains: %s" % consonants[2]
#print "The fourth class of consonants contains: %s" % consonants[3]
#print "The fifth class of consonants contains: %s" % consonants[4]

#print "The first class of vowels contains: %s" % vowels[0]
#print "The second class of vowels contains: %s" % vowels[1]

print "Possible onsets are: %s" % types[0]
print "Possible nuclei are: %s" % types[1]
print "Possible codas are: %s" % types[2]

print "Syllable patterns are: %s" % syllables

i = raw_input("How many words would you like to build? ")

if i == "":
	i = 100
else:
	i = (int(float(i)))

while i > 0:
	#working word variable
	word = ""
	#create word in this loop
	for j in range(0, int(random.random() * 100) % 5 + 1):
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
				
		word += syll
	fout.write(word)
	fout.write('\n')
	i -= 1
