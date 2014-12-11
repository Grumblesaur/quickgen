#!/usr/local/bin/python -tt
# -*- coding: utf-8 -*-
import os, sys, random

fout = open('output.txt', 'w')

random.seed(None)

phonemes = []

with open('input.txt') as fin:

	for line in fin:
		list = line.split()
		if list[0][0] == '#':
			break
		elif list[0][0] != '/':
			phonemes.append(list)

print "%s \n" % phonemes[0]
print "%s \n" % phonemes[1]
print "%s \n" % phonemes[2]

print phonemes[2][4]
