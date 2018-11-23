__author__ = 'mariakeet'

################################################## pluralising the noun

# this plural version based on plural_zu5 form plurals.py, but adjusted for getting the (word,nc) not from file,
# and the regular case is now in a separate method so as to avoid duplication
# plural_zu5: basic version + compound nouns (for nc 1/2, 3a/2a,7/8 and 9/10 only) + mass nouns + class exceptions + prefix exceptions (done for nc1/2 and nc7/8)
def plural_zu(word,nc):
    pl = 'zzzz'
    p = noun_except(word)  #real exceptions in singular and plural
    if p != 'x':
        pl = p
    elif ' ' in word and 'm' not in nc:  # the multi-word nouns, essentially doing only two words, for now
        nounpart, rest = word.split(' ',1)
        p = plural_zu(nounpart,nc)  #pluralizing the first word in the multi-word
        descr = rest
        if nc == '1' and rest[0] not in 'aeiou':
            descr = 'b' + rest[1:]
        elif nc =='1' and rest[0] in 'aeiou':
            descr = 'aba' + rest[1:]  #added this one after more testing (not in plural_zu5)
        elif nc == '3a':
            descr = 'aba' + rest[1:]
        elif (nc == '9' or nc == '7') and rest[0] not in 'aeiou':
            descr = 'z' + rest[1:]
        elif (nc == '9' or nc == '7') and rest[0] in 'aeiou':
            descr = rest[0] + 'zi' + rest[3:]
        pl = p + ' ' + descr
    elif 'm' in nc:
        pl = word   #mass nouns
    else:
        pl = plural_zu_regular(word,nc)
    return pl

# regular plurals (mostly regular)
def plural_zu_regular(noun,nc):
    pl = 'ccc'
    if (noun.startswith('um') or noun.startswith('uM')) and noun[2] != 'u' and nc == '1':
        pl = 'aba' + noun[2:]
    elif (noun.startswith('um') or noun.startswith('uM')) and noun[2] in 'aeio':
        pl = 'ab' + noun[2:]
    elif noun.startswith('umu') and nc == '1':
        pl = 'aba' + noun[3:]
    elif noun.startswith('u') and nc == '1a' or nc == '3a':
        pl = 'o' + noun[1:]
    elif noun.startswith('um') and noun[2] != 'u' and nc == '3':
        pl = 'imi' + noun[2:]
    elif noun.startswith('umu') and nc == '3':
        pl = 'imi' + noun[3:]
    elif noun.startswith('i') and noun[0:2] != 'ili' and (nc == '5' or nc == '9a'):
        pl = 'ama' + noun[1:]
    elif noun.startswith('ili') and nc == '5':
        pl = 'ama' + noun[3:]
    elif noun.startswith('isi') and nc == '7':
        pl = 'izi' + noun[3:]
    elif noun.startswith('is') and nc == '7' and noun[2] in 'aeou':
        pl = 'iz' + noun[2:]
    elif noun.startswith('i') and noun[1] != 'n' and nc == '9':
        pl = 'izi' + noun[1:]
    elif (noun.startswith('in') or noun.startswith('iN')) and nc == '9':
        pl = 'izin' + noun[2:]
    elif noun.startswith('u') and noun[1:2] != 'lu' and nc == '11':
        pl = 'izi' + noun[1:]
    elif noun.startswith('ulu') and nc == '11':
        pl = 'izi' + noun[3:]
    elif noun.startswith('ubu') and nc == '14':
        pl = noun
    elif (noun.startswith('uku') or noun.startswith('uk')) and (nc == '15' or nc == '17'): #added the uk- cf plural_zu5
        pl = noun
    elif nc in '24682a' or nc == '10':
        pl = noun
    else:
        pl = 'YYY' + noun
    return pl


# method for handling the sg pl exceptions that are stored separately in a file
def noun_except(n):
    pl = 'y'
    exceptN = open('nounExcept.txt').readlines()
    for sg in exceptN:
        w = sg.strip()
        s, p = w.split(',')
        if n == s:
            pl = p
            break
        else:
            pl = 'x'
    return pl


################################################## finding the noun class

# we assume all terms in the ontology are in the singular, as is customary practice
def find_nc(word):
    nnc = open('nncPairs.txt').readlines()
    for nounnc in nnc:
        while word in nounnc:
            noun, c = nounnc.split(',') #separate noun from nc
            nc = c.strip()
            if word == noun:
                return nc
            else:
                break
