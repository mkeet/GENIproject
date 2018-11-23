INTRODUCTION

This directory has all the code and related files we used for the ESWC 2017 demo.

The tool is described here, and please use this reference if you want to cite it:
Keet, C.M. Xakaza, M., Khumalo, L. Verbalising OWL ontologies in isiZulu with Python. The Semantic Web: ESWC 2017 Satellite Events, Blomqvist, E et al. (eds.). Springer LNCS vol 10577, 59-64. Portoroz, Slovenia, May 28 - June 2, 2017.
(CRC: http://www.meteck.org/files/ZUVerbDemoESWC17.pdf)

Note that Owlready is not ours, but developed by Pascal Lamy, over at https://pypi.org/project/Owlready/. it is included in this directory, as with this version, we know the verbaliser works (and we have not tested it with any possible later versions of Owlready). 

HOW TO USE IT

with the colourful user interface:
in the terminal, go to the relevant directory, like 

/Users/joannsoap/PythonProjects/OntologyVerbaliser_Zu-UI/example

(wherever you have downlaoded the directory) then type

python start.py

or, of you have several installations, then pick:

python3.4 start.py

with that, then enter as path and as URI, for the test ontology, the following (following on from the previous): 

/Users/joannsoap/PythonProjects/OntologyVerbaliser_Zu-UI/example

and 

http://www.semanticweb.org/mariakeet/ontologies/2016/10/testOntoisiZuluWithPW.owl

the gui will pop up


without UI:
in the terminal, go to the relevant directory, like 

/Users/joannsoap/PythonProjects/OntologyVerbaliser_Zu/example

(wherever you have downlaoded the directory) then type

python start.py -ui=False

or, of you have several installations, then pick:

python3.4 start.py -ui=False

then, enter at the successive prompts, for the test ontology, the following: 

/Users/joannsoap/PythonProjects/OntologyVerbaliser_Zu/example

and 

http://www.semanticweb.org/mariakeet/ontologies/2016/10/testOntoisiZuluWithPW.owl

the output is printed to the terminal
