# __author__ = 'removed for double-blind review'


########################

# this script contains several versions of the isiZulu pluraliser, going from plural_zu0() that takes a
# file of words (one per line) to plural_zu5, which takes a file of words with (comma-separated) noun class.
# you'll also need the file nounExcept.txt for the exceptions.
# teh output is written to a file capped plurals.txt
# there's also a plural_zu1_ind for individual word + noun class (that is periodically extended).

#########################

# extremely basic one, using whole words only. takes a file with nouns in singular, makes plural, adn write it to the file
# this is problematic because sometimes several options are possible, but well, it makes a point.
def plural_zu0(wf):
    pl = 'zzzz'
    testWord = open(wf).readlines()
    testPl = open('plurals.txt','a')
    for word in testWord:
        if word.startswith('um') and word[2] != 'u':
            pl = 'aba' + word[2:]
        elif word.startswith('umu'):
            pl = 'aba' + word[3:]
        elif word.startswith('u') and word[1] != 'm' and word[1:2] != 'bu' and word[1:2] != 'ku':
            pl = 'o' + word[1:]
        elif word.startswith('um') and word[2] != 'u':
            pl = 'imi' + word[2:]
        elif word.startswith('umu'):
            pl = 'imi' + word[3:]
        elif word.startswith('i') and not (word[0:2] == 'ili' or word[0:2] == 'isi' or word[1] == 'n'):
            pl = 'ama' + word[1:]
        elif word.startswith('ili'):
            pl = 'ama' + word[3:]
        elif word.startswith('isi'):
            pl = 'izi' + word[3:]
        elif word.startswith('i') and word[1] != 'n':
            pl = 'izi' + word[1:]
        elif word.startswith('in'):
            pl = 'izin' + word[2:]
        elif word.startswith('u') and word[1:2] != 'lu':
            pl = 'izi' + word[1:]
        elif word.startswith('ulu'):
            pl = 'izi' + word[3:]
        elif word.startswith('ubu'):
            pl = word
        elif word.startswith('uku'):
            pl = word
        else:
            pl = 'NNN' + word
        # fpl = word + ';' + pl
        testPl.write(pl)
    testPl.close()


# basic version, that takes a file with comma-separated word + its noun class
def plural_zu1(wf):
    pl = 'zzzz'
    testWord = open(wf).readlines()
    testPl = open('plurals.txt','a')
    for word in testWord:
        noun, c = word.split(',')
        nc = c.strip()
        if noun.startswith('um') and noun[2] != 'u' and nc == '1':
            pl = 'aba' + noun[2:]
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
        elif noun.startswith('i') and noun[1] != 'n' and nc == '9':
            pl = 'izi' + noun[1:]
        elif noun.startswith('in') and nc == '9':
            pl = 'izin' + noun[2:]
        elif noun.startswith('u') and noun[1:2] != 'lu' and nc == '11':
            pl = 'izi' + noun[1:]
        elif noun.startswith('ulu') and nc == '11':
            pl = 'izi' + noun[3:]
        elif noun.startswith('ubu') and nc == '14':
            pl = noun
        elif noun.startswith('uku') and nc == '15':
            pl = noun
        else:
            pl = 'YYY' + noun
        testPl.write(pl + '\n')
    testPl.close()



# basic one, guided with NC input, by individual word
def plural_zu1_ind(word,nc):
    if '?' in nc:
        return 'no nc for ' + word
    elif word.startswith('um') and word[2] != 'u' and nc == '1':
        return 'aba' + word[2:]
    elif word.startswith('umu') and nc == '1':
        return 'aba' + word[3:]
    elif word.startswith('u') and nc == '1a' or nc == '3a':
        return 'o' + word[1:]
    elif word.startswith('um') and word[2] != 'u' and nc == '3':
        return 'imi' + word[2:]
    elif word.startswith('umu') and nc == '3':
        return 'imi' + word[3:]
    elif word.startswith('i') and word[0:2] != 'ili' and (nc == '5' or nc == '9a'):
        return 'ama' + word[1:]
    elif word.startswith('ili') and nc == '5':
        return 'ama' + word[3:]
    elif word.startswith('isi') and nc == '7':
        return 'izi' + word[3:]
    elif word.startswith('i') and word[1] != 'n' and nc == '9':
        return 'izi' + word[1:]
    elif word.startswith('in') and nc == '9':
        return 'izin' + word[2:]
    elif word.startswith('u') and word[1:2] != 'lu' and nc == '11':
        return 'izi' + word[1:]
    elif word.startswith('ulu') and nc == '11':
        return 'izi' + word[3:]
    elif word.startswith('ubu') and nc == '14':
        return word
    elif word.startswith('uku') and nc == '15':
        return word
    else:
        return print('That noun class is not used in isiZulu or the noun is misspelled.')


# basic version + compound nouns (for nc 1/2, 3a/2a,7/8 and 9/10 only), that takes a file with comma-separated word + its noun class
def plural_zu2(wf):
    pl = 'zzzz'
    testWord = open(wf).readlines()
    testPl = open('plurals.txt','a')
    for word in testWord:
        noun, c = word.split(',')
        nc = c.strip()
        if ' ' in noun:
            nounpart, rest = noun.split(' ',1)
            p = plural_zu1_ind(nounpart,nc)
            descr = rest
            if nc == '1' and rest[0] not in 'aeiou':
                descr = 'b' + rest[1:]
            elif nc == '3a':
                descr = 'aba' + rest[1:]
            elif (nc == '9' or nc == '7') and rest[0] not in 'aeiou':
                descr = 'z' + rest[1:]
            elif (nc == '9' or nc == '7') and rest[0] in 'aeiou':
                descr = rest[0] + 'zi' + rest[3:]
            pl = p + ' ' + descr
        else:
            if noun.startswith('um') and noun[2] != 'u' and nc == '1':
                pl = 'aba' + noun[2:]
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
            elif noun.startswith('i') and noun[1] != 'n' and nc == '9':
                pl = 'izi' + noun[1:]
            elif noun.startswith('in') and nc == '9':
                pl = 'izin' + noun[2:]
            elif noun.startswith('u') and noun[1:2] != 'lu' and nc == '11':
                pl = 'izi' + noun[1:]
            elif noun.startswith('ulu') and nc == '11':
                pl = 'izi' + noun[3:]
            elif noun.startswith('ubu') and nc == '14':
                pl = noun
            elif noun.startswith('uku') and nc == '15':
                pl = noun
            else:
                pl = 'YYY' + noun
        testPl.write(pl + '\n')
    testPl.close()

# basic version + compound nouns (for nc 1/2, 3a/2a,7/8 and 9/10 only) + mass nouns,
# that takes a file with comma-separated word + its noun class,
# where mass nouns have an extra 'm'
def plural_zu3(wf):
    pl = 'zzzz'
    testWord = open(wf).readlines()
    testPl = open('plurals.txt','a')
    for word in testWord:
        noun, c = word.split(',')
        nc = c.strip()
        if ' ' in noun and 'm' not in nc:
            nounpart, rest = noun.split(' ',1)
            p = plural_zu1_ind(nounpart,nc)
            descr = rest
            if nc == '1' and rest[0] not in 'aeiou':
                descr = 'b' + rest[1:]
            elif nc == '3a':
                descr = 'aba' + rest[1:]
            elif (nc == '9' or nc == '7') and rest[0] not in 'aeiou':
                descr = 'z' + rest[1:]
            elif (nc == '9' or nc == '7') and rest[0] in 'aeiou':
                descr = rest[0] + 'zi' + rest[3:]
            pl = p + ' ' + descr
        else:
            if 'm' in nc:
                pl = noun
            else:
                if noun.startswith('um') and noun[2] != 'u' and nc == '1':
                    pl = 'aba' + noun[2:]
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
                elif noun.startswith('i') and noun[1] != 'n' and nc == '9':
                    pl = 'izi' + noun[1:]
                elif noun.startswith('in') and nc == '9':
                    pl = 'izin' + noun[2:]
                elif noun.startswith('u') and noun[1:2] != 'lu' and nc == '11':
                    pl = 'izi' + noun[1:]
                elif noun.startswith('ulu') and nc == '11':
                    pl = 'izi' + noun[3:]
                elif noun.startswith('ubu') and nc == '14':
                    pl = noun
                elif noun.startswith('uku') and nc == '15':
                    pl = noun
                else:
                    pl = 'YYY' + noun
        testPl.write(pl + '\n')
    testPl.close()

# basic version + compound nouns (for nc 1/2, 3a/2a,7/8 and 9/10 only) + mass nouns + class exceptions
def plural_zu4(wf):
    pl = 'zzzz'
    testWord = open(wf).readlines()
    exceptN = open('nounExcept.txt').readlines()
    testPl = open('plurals.txt','a')
    for word in testWord:
        noun, c = word.split(',')
        nc = c.strip()
        p = noun_except(noun)
        if p != 'x':
            pl = p
        elif ' ' in noun and 'm' not in nc:
            nounpart, rest = noun.split(' ',1)
            p = plural_zu1_ind(nounpart,nc)
            descr = rest
            if nc == '1' and rest[0] not in 'aeiou':
                descr = 'b' + rest[1:]
            elif nc == '3a':
                descr = 'aba' + rest[1:]
            elif (nc == '9' or nc == '7') and rest[0] not in 'aeiou':
                descr = 'z' + rest[1:]
            elif (nc == '9' or nc == '7') and rest[0] in 'aeiou':
                descr = rest[0] + 'zi' + rest[3:]
            pl = p + ' ' + descr
        elif 'm' in nc:
            pl = noun
        else:
            if noun.startswith('um') and noun[2] != 'u' and nc == '1':
                pl = 'aba' + noun[2:]
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
            elif noun.startswith('i') and noun[1] != 'n' and nc == '9':
                pl = 'izi' + noun[1:]
            elif noun.startswith('in') and nc == '9':
                pl = 'izin' + noun[2:]
            elif noun.startswith('u') and noun[1:2] != 'lu' and nc == '11':
                pl = 'izi' + noun[1:]
            elif noun.startswith('ulu') and nc == '11':
                pl = 'izi' + noun[3:]
            elif noun.startswith('ubu') and nc == '14':
                pl = noun
            elif noun.startswith('uku') and nc == '15':
                pl = noun
            else:
                pl = 'YYY' + noun
        testPl.write(pl + '\n')
    testPl.close()

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


# basic version + compound nouns (for nc 1/2, 3a/2a,7/8 and 9/10 only) + mass nouns + class exceptions + prefix exceptions (done for nc1/2 and nc7/8)
def plural_zu5(wf):
    pl = 'zzzz'
    testWord = open(wf).readlines()
    exceptN = open('nounExcept.txt').readlines()  #I don't think I need this one here.
    testPl = open('plurals.txt','a')
    for word in testWord:
        noun, c = word.split(',') #separate noun from nc
        nc = c.strip()
        p = noun_except(noun)  #real exceptions in singular and plural
        if p != 'x':
            pl = p
        elif ' ' in noun and 'm' not in nc:  # the multi-word nouns, essentially doing only two words, for now
            nounpart, rest = noun.split(' ',1)
            p = plural_zu1_ind(nounpart,nc)  #pluralizing the first word in the multi-word, where the same is as the 'else' below; it should be recursive, though
            descr = rest
            if nc == '1' and rest[0] not in 'aeiou':
                descr = 'b' + rest[1:]
            elif nc == '3a':
                descr = 'aba' + rest[1:]
            elif (nc == '9' or nc == '7') and rest[0] not in 'aeiou':
                descr = 'z' + rest[1:]
            elif (nc == '9' or nc == '7') and rest[0] in 'aeiou':
                descr = rest[0] + 'zi' + rest[3:]
            pl = p + ' ' + descr
        elif 'm' in nc:
            pl = noun   #mass nouns
        else:
            if noun.startswith('um') and noun[2] not in 'aeiou' and nc == '1':   #the regular plurals
                pl = 'aba' + noun[2:]
            elif noun.startswith('um') and noun[2] in 'aeio':
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
            elif noun.startswith('in') and nc == '9':
                pl = 'izin' + noun[2:]
            elif noun.startswith('u') and noun[1:2] != 'lu' and nc == '11':
                pl = 'izi' + noun[1:]
            elif noun.startswith('ulu') and nc == '11':
                pl = 'izi' + noun[3:]
            elif noun.startswith('ubu') and nc == '14':
                pl = noun
            elif noun.startswith('uku') and nc == '15':
                pl = noun
            else:
                pl = 'YYY' + noun
        testPl.write(pl + '\n')
    testPl.close()

# basic version + compound nouns (for nc 1/2, 3a/2a,7/8 and 9/10 only) + mass nouns + class exceptions + prefix exceptions (done for nc1/2 and nc7/8) + those that exist in pl only.
def plural_zu6(wf):
    pl = 'zzzz'
    testWord = open(wf).readlines()
    exceptN = open('nounExcept.txt').readlines()  #I don't think I need this one here.
    testPl = open('plurals.txt','a')
    for word in testWord:
        noun, c = word.split(',') #separate noun from nc
        nc = c.strip()
        p = noun_except(noun)  #real exceptions in singular and plural
        if p != 'x':
            pl = p
        elif ' ' in noun and 'm' not in nc:  # the multi-word nouns, essentially doing only two words, for now
            nounpart, rest = noun.split(' ',1)
            p = plural_zu1_ind(nounpart,nc)  #pluralizing the first word in the multi-word, where the same is as the 'else' below; it should be recursive, though
            descr = rest
            if nc == '1' and rest[0] not in 'aeiou':
                descr = 'b' + rest[1:]
            elif nc == '3a':
                descr = 'aba' + rest[1:]
            elif (nc == '9' or nc == '7') and rest[0] not in 'aeiou':
                descr = 'z' + rest[1:]
            elif (nc == '9' or nc == '7') and rest[0] in 'aeiou':
                descr = rest[0] + 'zi' + rest[3:]
            pl = p + ' ' + descr
        elif 'm' in nc:
            pl = noun   #mass nouns
        else:
            if noun.startswith('um') and noun[2] not in 'aeiou' and nc == '1':   #the regular plurals
                pl = 'aba' + noun[2:]
            elif noun.startswith('um') and noun[2] in 'aeio':
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
            elif noun.startswith('in') and nc == '9':
                pl = 'izin' + noun[2:]
            elif noun.startswith('u') and noun[1:2] != 'lu' and nc == '11':
                pl = 'izi' + noun[1:]
            elif noun.startswith('ulu') and nc == '11':
                pl = 'izi' + noun[3:]
            elif noun.startswith('ubu') and nc == '14':
                pl = noun
            elif noun.startswith('uku') and nc == '15':
                pl = noun
            elif nc in '24682a' or nc == '10':
                pl = noun
            else:
                pl = 'YYY' + noun
        testPl.write(pl + '\n')
    testPl.close()