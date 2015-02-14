#!/usr/local/bin/python -tt
# -*- coding: utf-8 -*-
import os, sys, random

#supply input as raw_input if running Python 3 or higher
if sys.version_info >= (3,0):
	raw_input = input

def parse(structure, part, phonemes):
	#grab a random phoneme from the relevant category and return it
	#structure can be O, N, or C, passed as 0, 1, or 2, respectively
	
	#initialize the segment string as empty
	seg = ""
	
	#focus in on relevant O, N, or C possibilities
	pattern = part[structure]

	#ensure that values fall within the bounds of list
	listrange = len(pattern) 

	#pick an O, N, or C to construct
	index = random.randrange(0, listrange)	
	onc = pattern[index] #obtain an onset, nucleus, or coda pattern
	if "," in onc:
		onc = onc.split(",") #if it is a cluster, split on commas
					 #this creates a list of indices to be accessed

	#loop to construct O, N, or C
	for i in range(0, len(onc)):
		pclass = int(onc[i]) #obtain an index for a class of phoneme
		phone = int(random.random() * 1000) % len(phonemes[pclass])
			#obtain an index for a specific phone
		seg += phonemes[pclass][phone] #add phone to segment
	
	return seg #return the segment to the main script
#end parse function definition

#ask for name of input file (default = "input.txt")
inn = raw_input("What is the name of your input file? (Leave blank for 'input.txt') ")
if inn == "":
	inn = "input.txt"

#ask for name of output file (default = "output.txt")
out = raw_input("What is the name of your output file? (Leave blank for 'output.txt') ")
if out == "":
	out = "output.txt"

seed = raw_input("Insert seed for RNG (leave blank for system time) ")

if seed == "":
	seed = None
else:
	seed = int(seed)

#use system time for seed
random.seed(seed)

#prepare lists
consonants = []
vowels = []
parts = []
structures = []

#prepare the output file
fout = open(out, 'w')

#extract from input file
with open(inn) as fin:

	#get consonants
	for line in fin:
		if line.strip() == "":
			continue
		list = line.split()
		if list[0][0] == '#':
			break
		elif list[0][0] != '/':
			consonants.append(list)

	#get vowels
	for line in fin:
		if line.strip() == "":
			continue
		list = line.split()
		if list[0][0] == '#':
			break
		elif list[0][0] != '/':
			vowels.append(list)

	#get parts
	for line in fin:
		if line.strip() == "":
			continue
		list = line.split()
		if list[0][0] == '#':
			break
		elif list[0][0] != '/':
			parts.append(list)

	#get structures
	for line in fin:
		if line.strip() == "":
			continue
		list = line.split()
		if list[0][0] == '#':
			break
		elif list[0][0] != '/':
			structures.append(list)

#un-nest the syllable patterns
structures = structures[0]

#ask for number of words (default = 100)
i = raw_input("How many words would you like to build? (Leave blank for 50) ")
if i == "":
	i = 50
else:
	i = int(i)

low = raw_input("Enter minimum number of syllables per word (Defaults to 1) ")
if low == "":
	low = 1
else:
	low = int(low)

high = raw_input("Enter maximum number of syllables per word (Defaults to 5) ")
if high == "":
	high = 5
else:
	high = int(high)

while i > 0:
	#working word variable
	word = ""

	#create word in this loop
	for j in range(0, int(random.triangular(low, high, low + 1))):

		#working syllable variable
		syll = ""

		#choose a random syllable pattern to follow
		form = structures[random.randrange(0, len(structures))]
		for k in range(0, len(form)):

			if form[k] == "O":
				#retrieve a string that is a valid onset
				syll += parse(0, parts, consonants)

			elif form[k] == "C":
				#retrieve a string that is a valid coda
				syll += parse(2, parts, consonants)

			elif form[k] == "N":
				#retrieve a string that is a valid nucleus
				syll += parse(1, parts, vowels)

		#add new syllable to the word		
		word += syll

	#print out the word followed by a newline
	fout.write(word)
	fout.write('\n')

	#decrement loop iterator
	i -= 1

#close files
fin.close()
fout.close()

sys.stdout.write("Program finished. \n")
#end program
