#!/usr/local/bin/python -tt
# -*- coding: utf-8 -*-
import os, sys, random

fout = open('output.txt', 'w')

random.seed(None)

shortv = ["a", "e", "i", "o", "u", "y"]
longv = ["á", "é", "í", "ó", "ú", "ý"]
vowels = shortv + longv

plosivesV = ["b", "d", "g"]
plosivesVl = ["p", "t", "k"]
plosives = plosivesVl + plosivesV

fricativesV = ["v", "z", "ð"]
fricativesVl = ["f", "s", "þ"]
fricatives = fricativesV + fricativesVl

obstruents = plosives + fricatives

nasals = ["m", "n", "ñ"]
liquids = ["l", "r"]
glides = ["j", "w"]
approximants = liquids + glides
sonorants = liquids + nasals + glides

consonants = obstruents + sonorants

i = raw_input("Number of words you'd like to make? ")
print '\n'
i = int(float(i))

while i >= 0:
	p = int(float(random.random() * 5)) + 2
	word = ""
	while p >= 0:
		if p % 2 == 1:
			word += consonants[int(float(random.random() * 100)) % len(consonants)]
		elif p % 2 == 0:
			word += vowels[int(float(random.random() * 100)) % len(vowels)]
		p = p - 1
	fout.write(word)
	fout.write('\n')
	i = i - 1
