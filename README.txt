#000 :: TABLE OF CONTENTS
=========================

#000 = Table of Contents
#100 = Licensing Information
#200 = General Instructions and Information
#300 = Instructions for quickgen.py
	#310 = Category Example
	#320 = General Rules and Guidelines for Editing
	#330 = Tips for Dealing with Language Oddities
#400 = Instructions for cleanup.py

	
#100 :: LICENSING INFORMATION
=============================

quickgen.py is a lightweight Python-based random word generator in progress.

    Copyright (C) 2014  James Murphy

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
    
    (See LICENCSE.md for additional details.)


#200 :: GENERAL INSTRUCTIONS AND INFORMATION
============================================

This package is compatible with Python 2 and Python 3.
Lines beginning with a / character in user-edited rule
configuration files are ignored by both the quickgen.py
script and the cleanup.py script. Lines starting with
the # character delimit blocks. Details for
file-specific use of # are listed below.

One of the arguments which quickgen.py will ask you to
pass it is a seed for the random number generator. Any
integer is an acceptable input for this. Leaving that
input blank will merely use the system time to seed
the random number generator.

Entering the same seed at different times will allow
you to go back to a word list you used previously, in
case you didn't get to save it before, or if you're
trying to keep your working directory uncluttered by
extraneous text files.

While quickgen.py will take any positive number as the
target amount of words to generate, cleanup.py is not
always so successful at cleaning large amounts of words.
50 is the recommended amount since it seems to fairly
consistently manage to clean at least the first 50 words
in a given batch.

This problem is one I am currently working on fixing, but
as long as you don't generate and attempt to clean more
than 50-60 words at a time, you probably won't have as much
garbage output in your clean.txt file.


#300 :: INSTRUCTIONS FOR quickgen.py
====================================

The # sign on its own line delimits a block of phoneme
or structure definitions and should be between each section
or else the program will fail. Blank lines are ignored by
the program, so feel free to space your categories and groups
as you please.

When prompted for input at runtime, the default values (the
values passed when you press Enter/Return without typing
anything) are "input.txt", "output.txt", and "100".


#310 :: CATEGORY EXAMPLE
========================

I recommend naming your phoneme categories with comments as
in this example:

//CONSONANTS
//plosives :: 0
p t k b d g

//fricatives :: 1
f v s z s s

//nasals :: 2
m n

//sonorants :: 3
l r
#

//VOWELS
//front vowels :: 0
a e i

//back vowels :: 1
o u
#

//PARTS OF SYLLABLES
//onsets :: 0
0 1 2 0,3 1,3

//nuclei :: 1
0 1

//codas :: 2
2 3
#

//SYLLABLES
//syllable patterns
N ON NC ONC
#


#320 :: GENERAL RULES AND GUIDELINES FOR EDITING
================================================

You define consonants, vowels, syllable parts, and syllable
structures. In each category (commented with ALL CAPS text
in the example above), a line represents a phonemic group.
The program will assign a number to each line of phonemes,
and you should number the groups in order (starting from
zero), since you'll need to know those numbers for the
PARTS OF SYLLABLES section.

Note that CONSONANTS can have any number of categories,
with the first category being treated as "0" instead of "1",
and that VOWELS can have any number of categories, with the
first category being treated as "0" instead of "1".

When you're defining parts of syllables, onsets and codas
take note of the group numbers of consonants, while
nuclei take note of the group numbers of vowels.

Defining an onset rule "0,3" here takes a plosive (group 0)
and a sonorant (group 3) and puts them in a sequence.
Defining an onset rule "1,3" here takes a fricative
(group 1) and a sonorant (group 3) and puts them in
a sequence.

In each category, you can increase the probability that a
given phoneme or pattern with appear by listing it more
than once. For example:

//fricatives :: 1
f v s z s s

This means that "s" is three times more likely to appear
than "f", "v", or "z". You can mix and match these as
needed.

The same process may be done for syllable parts and syllable
structures as well.

For example:

//codas :: 2
2 3 2

This means that nasals will appear twice as often as
sonorants in codas.

//onsets :: 0
0 1 2 3 0,3 1,3 1,3 0 0 2

This means that fricative-sonorant onsets and plosive-only
onsets are more likely to appear than others.

//syllable structures
ONC ON N NC ON ON ON

This means that Onset-Nucleus syllables are more likely
to occur than other types.


#330 :: TIPS FOR DEALING WITH LANGUAGE ODDITIES
===============================================

If your language, by chance, doesn't allow for syllables
with codas, put at least one number in the //codas :: 2
category, but remove any of the syllable structures with
"C" in them from the syllable structures list.

Likewise with "O" if you have a similar case with onsets.

So even for unused codas, do:

//codas :: 2
0

This ensures that the program won't break in the case of
an empty list. (I don't know if it actually would break,
but it's better not to take any chances.)

If your language has syllabic nasals or sonorants, create
a group for them in vowels. You can still have a group
for them in consonants as well, but they won't appear in
any syllable nucleus positions.

This program accepts UTF-8 unicode characters. If you put
any characters in categories not separated by whitespace,
for example, the string "ss", then that string will be
treated as a separate phoneme.


#400 :: INSTRUCTIONS FOR cleanup.py
===================================

This script takes two inputs: a rules file, whose
specification is described below; a raw words file,
which takes quickgen.py's "output.txt" by default; and
has one output, called "clean.txt" by default. This is
where the rewritten words go before the program finishes.

As quickgen.py is a relatively "dumb" wordgen, having rewrite
rules to tidy the output will probably be useful.

Here is an example of a rules file:

ee ae oe ie ue é
mn mñ mm m

//simplify stop clusters
pt pp pk p
kt kk kp k

ll j

oi oe

//dental aspirates to fricatives
th þ
dh ð
#

Empty lines and lines beginning with / are ignored.
In a line of rules, all elements but the last of the
row are substrings that the script searches for. If
it finds that substring in a word from your word file
(which is one of the files that cleanup.py takes as
input), that substring is replaced with the element at
the end of the relevant row of rewrite rules.

So using this example ruleset, the string "theepp"
would become "þép".
