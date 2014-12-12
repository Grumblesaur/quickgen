#!/usr/local/bin/python -tt
# -*- coding: utf-8 -*-
import os, sys, random

fout = open('output.txt', 'w')

random.seed(None)

phonemes = []
rules = []
syllables = ['ON', 'N']

with open('input.txt') as fin:

	for line in fin:
		list = line.split()
		if list[0][0] == '#':
			break
		elif list[0][0] != '/':
			phonemes.append(list)
	
	for line in fin:
		line = line.split()
		if list[0][0] == '#':
			break
		elif list[0][0] != '/':
			rules.append(list)

i = int(float(raw_input("How many words would you like to build? ")))

while i > 0:
	word = ''
	index = int(random.random() * 100) % len(syllables)
	form = syllables[index]
	numsyll = int(random.random() * 100) % 4 + 1
	for k in range(0, numsyll):
		syll = ''
		for j in range(0,  len(form)):
			decide = 'O'
			if form[j] == 'O':
				decide = int(random.random() * 100) % 2
			elif form[j] == 'N':
				decide = 2
			elif form[j] == 'C':
				decide = 1
			chardex = int(random.random() * 100) % len(phonemes[decide])
			syll += phonemes[decide][chardex]
		word += syll
	fout.write(word)
	fout.write('\n')
	i = i - 1
