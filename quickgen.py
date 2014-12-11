#!/usr/local/bin/python -tt
# -*- coding: utf-8 -*-
import os, sys, random

fout = open('output.txt', 'w')

random.seed(None)

phonemes = []
rules = []
syllables = ['ONC', 'ON', 'NC', 'N']

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

