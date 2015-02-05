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

#prepare list of words to be rewritten
rawtext = []

#pull in all the words from quickgen.py's output file
fin = open(words)
for line in fin:
	rawtext.append(line)
fin.close() #close the file

#open new input file as rules file, read in rules
fin = open(rules):
for line in fin:
	rewrites.append(line.split())
fin.close() #close rules file

print rawtext
print rewrites


