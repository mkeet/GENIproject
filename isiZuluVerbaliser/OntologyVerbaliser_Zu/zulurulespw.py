# by maria keet

import Zuplurals
from Zuplurals import *

"""
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
"""

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


def strip_m(nc):
    if nc[-1] == 'm':
        nc = nc[0:-1]
    return nc

################################################## looking up pieces

# given singular nc, give the nc of the plural
def look_ncp(ncs):
    if '?' in ncs:
        nc = 'ff'
    elif ncs == '1':
        nc = '2'
    elif ncs == '1a' or ncs == '3a':
        nc = '2a'
    elif ncs == '3':
        nc = '4'
    elif ncs == '5' or ncs == '9a':
        nc = '6'
    elif ncs == '7':
        nc = '8'
    elif ncs == '9' or ncs == '11':
        nc = '10'
    elif ncs == '14':
        # it doesn't have a plural
        nc = '14'
    elif ncs == '15':
        # it doesn't have a plural
        nc = '15'
    elif ncs == '2a' or ncs in '468' or ncs == '10':
        nc = ncs
    elif ncs[-1] == 'm':
        # the real mass nouns stay in the same class
        nc = ncs[0:-1]
    else:
        # erroneous noun class
        nc = '0'
    return nc

# get the QC forall, for the plurals, adn now also for teh singulars, because some mass nouns may be.
def look_qca(ncp):
    if '?' in ncp:
        qca = 'Dddd'
    elif ncp == '2' or ncp == '2a' or ncp == '14':
        qca = 'Bonke'
    elif ncp == '3a' or ncp == '3':
        qca = 'Wonke'
    elif ncp == '4':
        qca = 'Yonke'
    elif ncp == '5' or ncp == '11' or ncp == '17':
        qca = 'Lonke'
    elif ncp == '6':
        qca = 'Onke'
    elif ncp == '7':
        qca = 'Sonke'
    elif ncp == '8' or ncp == '10':
        qca = 'Zonke'
    elif ncp == '9a' or ncp == '9':
        qca = 'Yonke'
    elif ncp == '15':
        qca = 'Konke'
    else:
        qca = 'Gggg'
    return qca

# lookup the negative subject concord
def look_negsc(nc):
    if '?' in nc:
        negsc = 'ccc'
    elif nc == '1' or nc == '1a' or nc == '3a':
        negsc = 'aka'
    elif nc == '2' or nc == '2a':
        negsc = 'aba'
    elif nc == '3':
        negsc = 'awu'
    elif nc == '4' or nc == '9a' or nc == '9':
        negsc = 'ayi'
    elif nc == '5':
        negsc = 'ali'
    elif nc == '6':
        negsc = 'awa'
    elif nc == '7':
        negsc = 'asi'
    elif nc == '8' or nc == '10':
        negsc = 'azi'
    elif nc == '11':
        negsc = 'alu'
    elif nc == '14':
        negsc = 'abu'
    elif nc == '15':
        negsc = 'aku'
    else:
        negsc = 'xxx'
    return negsc

# lookup the pronomial
def look_pron(nc):
    if '?' in nc:
        pron = 'aaa'
    elif nc == '1' or nc == '1a':
        pron = 'yena'
    elif nc == '2' or nc == '2a' or nc == '14':
        pron = 'bona'
    elif nc == '3a' or nc == '3' or nc == '6':
        pron = 'wona'
    elif nc == '4' or nc == '9a' or nc == '9':
        pron = 'yona'
    elif nc == '5':
        pron = 'lona'
    elif nc == '7':
        pron = 'sona'
    elif nc == '8' or nc == '10':
        pron = 'zona'
    elif nc == '11':
        pron = 'lona'
    elif nc == '15':
        pron = 'khona'
    else:
        pron = 'yyyy'
    return pron


# relative concord lookup
def look_relc(nc):
    if '?' in nc:
        relc = 'bbb'
    elif nc == '1' or nc == '1a' or nc == '3a' or nc == '3':
        relc = 'o'
    elif nc == '2' or nc == '2a':
        relc = 'aba'
    elif nc == '4' or nc == '9a' or nc == '9':
        relc = 'e'
    elif nc == '5':
        relc = 'eli'
    elif nc == '6':
        relc = 'a'
    elif nc == '7':
        relc = 'esi'
    elif nc == '8' or nc == '10':
        relc = 'ezi'
    elif nc == '11':
        relc = 'olu'
    elif nc == '14':
        relc = 'obu'
    elif nc == '15':
        relc = 'oku'
    elif nc == '17':
        relc = 'olu'
    else:
        relc = 'zzz'
    return relc


#qc-exists lookup
def look_qce(nc):
    if '?' in nc:
        qce = 'ggg'
    elif nc == '1' or nc == '1a':
        qce = 'ye'
    elif nc == '2' or nc == '2a' or nc == '14':
        qce = 'bo'
    elif nc == '3a' or nc == '3' or nc == '6':
        qce = 'wo'
    elif nc == '4' or nc == '9a' or nc == '9':
        qce = 'yo'
    elif nc == '5' or nc == '11':
        qce = 'lo'
    elif nc == '7':
        qce = 'so'
    elif nc == '8' or nc == '10':
        qce = 'zo'
    elif nc == '15':
        qce = 'ko'
    elif nc == '17':
        qce = 'lo'
    else:
        qce = 'lll'
    return qce



# subject concord look up for hte noun class. assume 3rd pers sing (reasonable w.r.t. ontologies)
def look_sc(nc):
    if '?' in nc:
        sc = 'hhh'
    elif nc == '1' or nc == '1a' or nc == '3a' or nc == '3':
        sc = 'u'
    elif nc == '2' or nc == '2a':
        sc = 'ba'
    elif nc == '4' or nc == '9a' or nc == '9':
        sc = 'i'
    elif nc == '5':
        sc = 'li'
    elif nc == '6':
        sc = 'a'
    elif nc == '7':
        sc = 'si'
    elif nc == '8' or nc == '10':
        sc = 'zi'
    elif nc == '11':
        sc = 'lu'
    elif nc == '14':
        sc = 'bu'
    elif nc == '15':
        sc = 'ku'
    elif nc == '17':
        sc = 'lu'
    else:
        sc = 'jjj'
    return sc

# look up the possessive concord
def look_pc(nc):
    if '?' in nc:
        pc = 'ppp'
    elif nc == '1' or nc == '1a' or nc == '3a' or nc == '3':
        pc = 'wa'
    elif nc == '2' or nc == '2a' or nc == '14':
        pc = 'ba'
    elif nc == '4' or nc == '9a' or nc == '9':
        pc = 'ya'
    elif nc == '5':
        pc = 'la'
    elif nc == '6':
        pc = 'a'
    elif nc == '7':
        pc = 'sa'
    elif nc == '8' or nc == '10':
        pc = 'za'
    elif nc == '11':
        pc = 'lwa'
    elif nc == '15' or nc == '17':
        pc = 'kwa'
    else:
        pc = 'pnp'
    return pc

################################################## auxiliary phonological issues

# the generic vowel coalescence, takes two words, glues them together
# still incomplete w.r.t. all possible combinations, notably -i and -o are missing
def vowel_coal(first,second):
    if first[-1] == 'a' and second[0] == 'a':
        newword = first[0:-1] + 'a' + second[1:]
    elif first[-1] == 'a' and (second[0] == 'i' or second[0] == 'e'):
        newword = first[0:-1] + 'e' + second[1:]
    elif first[-1] == 'a' and first != 'nga' and second[0] == 'u':
        newword = first[0:-1] + 'o' + second[1:]
    elif first[-1] == 'e' and second[0] == 'a':
        newword = first[0:-1] + 'a' + second[1:]
    elif first[-1] == 'e' and second[0] == 'i':
        newword = first[0:-1] + 'e' + second[1:]
    elif first[-1] == 'e' and (second[0] == 'o' or second[0] == 'u'):
        newword = first[0:-1] + 'o' + second[1:]
    elif first[-1] == 'u':
        newword = first + second[1:]  #assuming the u is a 'stronger' vowel, for now.
    else:
        if first == 'nga' and second[0] == 'o':
            newword = 'ngo' + second[1:]
        elif first == 'nga' and second[0] == 'u':
            newword = 'ngo' + second[1:]
        else:
            newword = 'other'
    return newword

#locative prefix, possibly still incomplete w.r.t. phonological conditioning
def locpre(word,nc):
    phonolocword = 'e' + 'attached'
    if nc == '1a' or nc == '2a' or nc == '3a' or nc == '17':
        phonolocword = vowel_coal('ku',word)
    else:
        phonolocword = vowel_coal('e',word)
    return phonolocword


# phonological conditioning for locative suffix (can be squeezed into the former, but this way I know better what's happening
# the else-statement is to catch the nouns that do not have a vowel at the end
def locsuf_phono(word):
    locsufexceptu = ['imvilophu','idiphu','ifomu']
    if word in locsufexceptu:
        wordlocsuf = word[0:-1] + 'ini'
    elif word[-1] == 'a':
        wordlocsuf = word[0:-1] + 'eni'
    elif word[-1] == 'e':
        wordlocsuf = word[0:-1] + 'eni'
    elif word[-1] == 'i':
        wordlocsuf = word[0:-1] + 'ini'
    elif word[-1] == 'o':
        wordlocsuf = word[0:-1] + 'weni'
    elif word[-1] == 'u' and word[-3:-2] != 'ph':
        wordlocsuf = word[0:-1] + 'wini'
    elif word[-1] == 'u' and word[-3:-2] == 'ph':
        wordlocsuf = word[0:-3] + 'shini'
    else:
        wordlocsuf = word + 'ini'
    return wordlocsuf


# sc deviations for the vowel-commencing stems (so far, we needed only the a- and e- ones)
# changed and extended with o- cf the file for the inlg16 paper
def sc_vowel_vroot(word,nc):
    sc = look_sc(nc)
    if (word[0] == 'a' or word[0] == 'e') and len(sc) >= 2 and sc != 'ku' and sc != 'lu':
        conjv = sc[:-1] + word
    elif (word[0] == 'a' or word[0] == 'e') and sc == 'a':
        conjv = word
    elif (word[0] == 'a' or word[0] == 'e') and sc == 'i':
        conjv = 'y' + word
    elif (word[0] == 'a' or word[0] == 'e') and sc == 'u':
        conjv = 'w' + word
    elif (word[0] == 'a' or word[0] == 'e') and (sc == 'ku' or sc == 'lu'):
        conjv = sc[0] + 'w' + word
    elif word[0] == 'o' and len(sc) >= 2 and sc != 'ku':
        conjv = sc[:-1] + word
    elif word[0] == 'o' and (sc == 'a' or sc == 'i'):
        conjv = word
    elif word[0] == 'o' and sc == 'u':
        conjv = 'w' + word
    elif word[0] == 'o' and sc == 'ku':
        conjv = 'kw' + word
    else:
        conjv = word #or: don't do anything
    return conjv

# deviant phonological conditioning case with not vowel coalescence when neg sc and vowel-commencing stems
# the 'word' that's inputted is the verb root,
def negsc_vowel_vroot(word,negsc):
    if word[0] == 'a' or word[0] == 'e':
        negconjv = negsc + 'y' + word
    else:
        negconjv = negsc + 'ng' + word
    return negconjv

################################################## dealing with verbs

# find root of the verb. we're doing a simple look up now, as a stub,
# and assume the stem is recorded as op, not some arbitrary verb.
# it's a bit clumsy, and it would be nice to find it automatically...
def find_rt(op):
    vroots = open('vroots.txt').read()
    if op[0:-1] in vroots:
        rt = op[0:-1]
    else:
        rt = 'toadd'
    return rt

# see elsewhere for SC

################################################### the ones that generate the sentence

#subsumption
def isa_zu(sub,super):
    if super.startswith('i'):
        return sub + ' y' + super
    elif super.startswith('a') or super.startswith('o') or super.startswith('u'):
        return sub + ' ng' + super
    else:
        return print('this is not a well-formed isiZulu noun.')


#complement/disjointness
def nisa_zu(sub,super):
    nc1m = find_nc(sub)
    nc2m = find_nc(super)
    pl = plural_zu(sub,nc1m)
    nc2 = strip_m(nc2m)
    ncp = look_ncp(nc1m)
    qca = look_qca(ncp) #forall qc
    negsc = look_negsc(ncp)
    pron = look_pron(nc2)
    return qca + ' ' + pl + ' ' + negsc + pron + ' ' + super


#simple existential quantification
# modified cf zulurules to handle also vowel-commencing vroots
def exists_zu(sub,op,super):
    nc1m = find_nc(sub)
    nc2m = find_nc(super)
    pl = plural_zu(sub,nc1m)
    nc2 = strip_m(nc2m)
    ncp = look_ncp(nc1m)
    qca = look_qca(ncp)
    rc = look_relc(nc2)
    qc = look_qce(nc2)
    rt = find_rt(op)
    if rt[0] in 'aeiou':
        conjugrt = sc_vowel_vroot(rt,ncp)
    else:
        sc = look_sc(ncp)
        conjugrt = sc + rt
    return qca + ' ' + pl + ' ' + conjugrt + 'a' + ' ' + super + ' ' + rc + qc + 'dwa'

#simple existential quantification, negated
# added cf the ruleml paper: vowel-commencing roots, but just using the vowel_coalescence for now
def nexist_zu(sub,op,super):
    nc1m = find_nc(sub)
    nc2m = find_nc(super)
    pl = plural_zu(sub,nc1m)
    nc2 = strip_m(nc2m)
    ncp = look_ncp(nc1m)
    qca = look_qca(ncp)
    rc = look_relc(nc2)
    qc = look_qce(nc2)
    rt = find_rt(op)
    negsc = look_negsc(ncp)
    if rt[0] in 'aeiou':
        negconjrt = negsc_vowel_vroot(rt,negsc)
    else:
        negconjrt = negsc + rt
    return qca + ' ' + pl + ' ' + negconjrt + 'i' + ' ' + super + ' ' + rc + qc + 'dwa'

# the enumeration-and, not the connective-and
def conjunct_zu(first,second):
    if second[0] == 'i':
        andsec = 'ne'
    elif second[0] == 'u' or second[0] == 'o':
        andsec = 'no'
    elif second[0] == 'a':
        andsec = 'na'
    else:
        andsec = 'nnn'
    return first + ' ' + andsec + second[1:]


############################## and those part-whole relations:


# structural, involvement, containment, membership, part-subquantities, participation, whole-part relation:
def wp(whole,part):
    nc1m = find_nc(whole)
    nc2m = find_nc(part)
    pl = plural_zu(whole,nc1m)
    nc2 = strip_m(nc2m)
    ncp = look_ncp(nc1m)
    qca = look_qca(ncp)
    sc = look_sc(ncp)
    conjp = vowel_coal('na',part)
    rc = look_relc(nc2)
    qc = look_qce(nc2)
    return qca + ' ' + pl + ' ' + sc + conjp + ' ' + rc + qc + 'dwa'

#wp for spatial portions, witout the -dwa
def wp_spatial(whole,part):
    nc1m = find_nc(whole)
    pl = plural_zu(whole,nc1m)
    ncp = look_ncp(nc1m)
    qca = look_qca(ncp)
    sc = look_sc(ncp)
    conjp = vowel_coal('na',part)
    return qca + ' ' + pl + ' ' + sc + conjp

# structural, involvement, membership, part-subquantities, participation, part-whole relation:
def pw(part,whole):
    nc1m = find_nc(part)
    nc2m = find_nc(whole)
    pl = plural_zu(part,nc1m)
    nc2 = strip_m(nc2m)
    ncp = look_ncp(nc1m)
    qca = look_qca(ncp)
    sc = look_sc(ncp)
    pc = 'ya' #no look-up needed for the PC, because it's always ya- because always ingxenye (nc9)
    pcw = vowel_coal(pc,whole)
    rc = look_relc(nc2)
    qc = look_qce(nc2)
    return qca + ' ' + pl + ' ' + sc + 'yingxenye' + ' ' + pcw + ' ' + rc + qc + 'dwa'

# participation with collectives in singular
def wp_cp(whole,part):
    nc1m = find_nc(whole)
    nc2m = find_nc(part)
    nc1 = strip_m(nc1m)
    nc2 = strip_m(nc2m)
    qca = look_qca(nc1)
    sc = look_sc(nc1)
    conjp = vowel_coal('na',part)
    rc = look_relc(nc2)
    qc = look_qce(nc2)
    return qca + ' ' + whole + ' ' + sc + conjp + ' ' + rc + qc + 'dwa'

# subquantities [as parts] in singular, and no -dwa:
def wp_s(whole,part):
    nc1m = find_nc(whole)
    nc1 = strip_m(nc1m)
    qca = look_qca(nc1)
    sc = look_sc(nc1)
    conjp = vowel_coal('na',part)
    return qca + ' ' + whole + ' ' + sc + conjp

# solid portion has W in singular, and the P with the PC. and assuming that the part-quantity component is one word only...
def wp_solid_p(whole,part):
    nc1m = find_nc(whole)
    quantity = part.partition(' ')[0]
    if len(part.split()) == 2:
        stuff = part.rpartition(' ')[-1]
    else:
        stuff = part.partition(' ')[-1]
    nc2m = find_nc(quantity)
    nc1 = strip_m(nc1m)
    nc2 = strip_m(nc2m)
    qca = look_qca(nc1)
    sc = look_sc(nc1)
    conjp = vowel_coal('na',quantity)
    pcquantity = look_pc(nc2)
    ofstuff = vowel_coal(pcquantity,stuff)
    rc = look_relc(nc2)
    qc = look_qce(nc2)
    return qca + ' ' + whole + ' ' + sc + conjp + ' ' + ofstuff + ' ' + rc + qc + 'dwa'

# part-whole, in the singular as well, to cater for subquantities that can be both mass and count noun, depending on context
def pw_s(part,whole):
    nc1m = find_nc(part)
    nc1 = strip_m(nc1m)
    qca = look_qca(nc1)
    sc = look_sc(nc1)
    pc = 'ya' #no look-up needed for the PC, because it's always ya- because always ingxenye (nc9)
    pcw = vowel_coal(pc,whole)
    return qca + ' ' + part + ' ' + sc + 'yingxenye' + ' ' + pcw

# solid portion-of
def pw_solid_p(part,whole):
    quantity = part.partition(' ')[0]
    if len(part.split()) == 2:
        stuff = part.rpartition(' ')[-1]
    else:
        stuff = part.partition(' ')[-1]
    nc1m = find_nc(quantity)
    nc2m = find_nc(whole)
    nc1 = strip_m(nc1m)
    nc2 = strip_m(nc2m)
    ncp = look_ncp(nc1)
    qca = look_qca(ncp)
    pcquantity = look_pc(ncp)
    ofstuff = vowel_coal(pcquantity,stuff)
    pl = plural_zu(quantity,nc1)
    sc = look_sc(ncp)
    pc = 'sa' #no look-up needed for the PC, because it's always sa- because always isiqephu (nc7)
    pcw = vowel_coal(pc,whole)
    rc = look_relc(nc2)
    qc = look_qce(nc2)
    return qca + ' ' + pl + ' ' + ofstuff + ' ' + sc + 'yisiqephu' + ' ' + pcw + ' ' + rc + qc + 'dwa'

# spatial portion-of
def pw_spatial_p(part,whole):
    nc1m = find_nc(part)
    pl = plural_zu(part,nc1m)
    nc1 = strip_m(nc1m)
    ncp = look_ncp(nc1)
    qca = look_qca(ncp)
    sc = look_sc(ncp)
    pc = 'wa' #no look-up needed for the PC, because it's always wa- because always umunxa (nc3)
    pcw = vowel_coal(pc,whole)
    return qca + ' ' + pl + ' ' + sc + 'ngumunxa' + ' ' + pcw

# participates-in, for collective parts
def pw_pi_c(part,whole):
    nc1m = find_nc(part)
    nc2m = find_nc(whole)
    nc1 = strip_m(nc1m)
    nc2 = strip_m(nc2m)
    qca = look_qca(nc1)
    sc = look_sc(nc1)
    lpre = locpre(whole,nc2)
    lprewlocsuf = locsuf_phono(lpre)
    rc = look_relc(nc2)
    qc = look_qce(nc2)
    return qca + ' ' + part + ' ' + sc + 'hlanganyele' + ' ' + lprewlocsuf + ' ' + rc + qc + 'dwa'

# constitution, of the built type.
# renamed this function after the inlg16
def const_a(whole,part):
    nc1m = find_nc(whole)
    pl = plural_zu(whole,nc1m)
    ncp = look_ncp(nc1m)
    qca = look_qca(ncp)
    conjverb = sc_vowel_vroot('akhiwe',ncp)
    ofpart = vowel_coal('nga',part)
    return qca + ' ' + pl + ' ' + conjverb + ' ' + ofpart

# constitution as well, for other 'non-construction' constitution
def const_e(whole,part):
    nc1m = find_nc(whole)
    pl = plural_zu(whole,nc1m)
    ncp = look_ncp(nc1m)
    qca = look_qca(ncp)
    conjverb = sc_vowel_vroot('enziwe',ncp)
    ofpart = vowel_coal('nga',part)
    return qca + ' ' + pl + ' ' + conjverb + ' ' + ofpart

#incomplete, so commented out
"""
# located in for geographic entities whole-part
def wp_hasloc(whole,part):
    nc1 = find_nc(whole)
    #there are sooo many places that won't be in nncPairs; if foreign name, then i- in from and defaults to nc5
    if nc1 == None:
        sc = 'li'
    else:
        sc = look_sc(nc1)
    conjp = vowel_coal('na',part)
    return whole + ' ' + sc + conjp

# located in for geographic entities part-whole.
def pw_locin(part,whole):
    hole = whole[1:]
    hollocsuf = locsuf_phono(hole)
    return part + ' ' + 'yindawo' + ' ' + 'ese' + hollocsuf
"""

# contained-in
def pw_ci(part,whole):
    nc1m = find_nc(part)
    nc2m = find_nc(whole)
    pl = plural_zu(part,nc1m)
    nc2 = strip_m(nc2m)
    ncp = look_ncp(nc1m)
    qca = look_qca(ncp)
    sc = look_sc(ncp)
    wholels = locsuf_phono(whole)
    locprewls = locpre(wholels,nc2)
    rc = look_relc(nc2)
    qc = look_qce(nc2)
    return qca + ' ' + pl + ' ' + sc + 's' + locprewls + ' ' + rc + qc + 'dwa'