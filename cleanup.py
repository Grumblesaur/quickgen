#!/usr/local/bin/python -tt
# -*- coding: utf-8 -*-
import os, sys, string

#supply input as raw_input if running Python 3 or higher
if sys.version_info >= (3,0):
	raw_input = input

#ask for name of input file of cleanup rules
rules = raw_input("What is the name of your cleanup rules file? (Leave blank for 'rules.txt') ")
if rules == "":
	rules = "rules.txt"

#ask for name of input file of raw wordgen output
words = raw_input("What is the name of your file of raw wordgen output? (Leave blank for 'output.txt') ")
if words == "":
	words = "output.txt"

#ask for the name of output file for clean wordgen
clean = raw_input("What is the name of your cleaned output file? (Leave blank for 'clean.txt') ")
if clean == "":
	clean = "clean.txt"

#prepare list of rewrite rules
rewrites = []

#prepare output file
fout = open(clean, 'w')

#extract from rule file
with open(rules) as fin:
	#get rules line-by-line
	for line in fin:
		#skip blank lines
		if line.strip() == "":
			continue
		#split rewrite conditions from rules
		list = line.split()
		
		#if a line has an isolated # sign in it, stop extraction
		if list[0][0] == "#":
			break

		#and if there's no slash, append it to the list
		elif list[0][0] != '/':
			rewrites.append(list)
fin.close()


#pull one string from the file at a time
with open(words) as fin:
	#start loop to rewrite each word in file
	for line in fin:
		#prepare word variable
		word = line
		cleanword = ""
		#step through all rewrite rules
		for i in range (0, len(rewrites)):
			for j in range (0, len(rewrites[i]) - 1):
				#variable to hold current substring
				substring = rewrites[i][j]
				#variable to index to replacement substring
				replace = len(rewrites[i]) - 1
				#check if substring is in the word
				if substring in word:
					#replace it
					cleanword = string.replace(word, substring, rewrites[i][replace])
		#write word to file
		fout.write(cleanword)

#close files
fin.close()
fout.close()

sys.stdout.write("Program finished. \n")

#end program
