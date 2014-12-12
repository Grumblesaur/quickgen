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

INSTRUCTIONS FOR USE
====================

This program is compatible with Python 2 and Python 3.

You should create an input file with your phonemes and rules.
Use "//" or "/" to comment out a line in the input file.
This will prevent the program from extracting that line.
The # sign on its own line delimits a block of phoneme
definitions and should be between each section or else
the program will fail.

When prompted for input at runtime, the default values (the
values passed when you press Enter/Return without typing
anything) are "input.txt", "output.txt", and "100".

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
0 1 2 03 13

//nuclei :: 1
0 1

//codas :: 2
2 3
#

//SYLLABLES
//syllable patterns
N ON NC ONC
#

GENERAL RULES AND GUIDELINES FOR EDITING
========================================
You define consonants, vowels, syllable parts, and syllable
structures. In each category (commented with ALL CAPS text
in the example above), a line represents a phonemic group.
The program will assign a number to each line of phonemes,
and you should number the groups in order (starting from
zero), since you'll need to know those numbers for the
PARTS OF SYLLABLES section.

Note that CONSONANTS can have 10 categories, labeled 0-9,
and that VOWELS can have 10 categories, labeled 0-9.

When you're defining parts of syllables, onsets and codas
take note of the group numbers of consonants, while
nuclei take note of the group numbers of vowels.

Defining an onset rule "03" here takes a plosive (group 0)
and a sonorant (group 3) and puts them in a sequence.
Defining an onset rule "13" here takes a fricative
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
0 1 2 3 03 13 13 0 0 2

This means that fricative-sonorant onsets and plosive-only
onsets are more likely to appear than others.

//syllable structures
ONC ON N NC ON ON ON

This means that Onset-Nucleus syllables are more likely
to occur than other types.

TIPS FOR DEALING WITH LANGUAGE ODDITIES
=======================================

If your language, by chance, doesn't allow for syllables
with codas, put at least one number in the //codas :: 2
category, but remove any of the syllable structures with
"C" in them from the syllable structures list.

Likewise with "O" if you have a similar case with onsets.

If your language has syllabic nasals or sonorants, create
a group for them in vowels. You can still have a group
for them in consonants as well, but they won't appear in
any syllable nucleus positions.

This program accepts UTF-8 unicode characters. If you put
any characters in categories not separated by whitespace,
for example, the string "ss", then that string will be
treated as a separate phoneme.