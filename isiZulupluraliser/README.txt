This zip file contains the following files:

===== isiZulu pluraliser =====
in the isiZulu directory

Files for proper working of some of the functions of the pluraliser:
nounExcept.txt - singulars with truly deviating noun class plural prefix; ensure this file is in the same folder as the plurals.py

To run the script in the Python 3.x interpreter:
>>> import plurals
>>> from plurals import *
>>> plural_zuXX(‘YY.txt')
where XX is the pluraliser version (a number between 0 and 6), and YY the name of the input file.
Upon execution, it generates a file plurals.txt with the output, which are the plurals of the nouns listed in the input file.

Input files (ensure they are in the same folder as plurals.py):
setR1.txt - the first word list, with domain coverage
setR1NC.txt - same list as in setR1, but with noun classes added
setR1NCm.txt - same list as setR1NC, but where the noun classes of the mass nouns are appended with an ‘m’
dictW.txt - the dictionary-based wordlist
dictWnc.txt - the dictionary-based wordlist, with the noun classes for each noun
dictWncM.txt - the dictionary-based wordlist, with the noun classes for each noun, and where the noun classes of the mass nouns are appended with an ‘m’ 

Output files (these files in the directory have been renamed for indicative purpose):
pluralsPluralZu0setR1 - plurals generated with plural_zu0, taking setR1.txt as input
pluralsPluralZu1setR1NC - plurals generated with plural_zu1, taking setR1NC.txt as input
pluralsPluralZu2setR1NC - plurals generated with plural_zu2, taking setR1NC.txt as input
pluralsPluralZu3setR1NCm - plurals generated with plural_zu3, taking setR1NCm.txt as input
pluralsPluralZu4setR1NCm - plurals generated with plural_zu4, taking setR1NCm.txt as input
pluralsPluralZu5setR1NCm - plurals generated with plural_zu5, taking setR1NCm.txt as input
pluralsZU0dictW - plurals generated with plural_zu0, taking dictW.txt as input
pluralsZU1dictWnc - plurals generated with plural_zu1, taking dictWnc.txt as input
pluralsZU2dictWnc - plurals generated with plural_zu2, taking dictWnc.txt as input
pluralsZU3dictWncM - plurals generated with plural_zu3, taking dictWncM.txt as input
pluralsZU4dictWncM - plurals generated with plural_zu4, taking dictWncM.txt as input
pluralsZU5dictWncM - plurals generated with plural_zu5, taking dictWncM.txt as input
pluralsZU6dictWncM - plurals generated with plural_zu6, taking dictWncM.txt as input

Analysis:
PluraliserOutputsCompared.xlsx - copied in/out files, with highlighting of errors and some comments.

===== Runyankore pluraliser =====
in the Runyankore directory

Application: in the ‘Final’ subdirectory of the Runyankore directory. They can be run as:
java Pluralizer Set1r
java Pluralizer Set2r

Output files: 
each run produces two output files, one of just the plurals, and another with the singular and plural side-by-side. (the files in the directory have been renamed for indicative purpose)


