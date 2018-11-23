from ontologyExtractor import OntologyExtractor
from sentenceGenerator import evaluate

WORDTYPE = ['n','v']

TYPE1 = ['exists','enziwe','nexist','akhiwe','umunxa','disjoint',\
    'ingxenye','ingxenye_s','hlanganyele']
TYPE2 = ['subclasses','intersection','bbbb','ffff','aaaa','dddd','cccc']

def formatType1(sentence, n, words):
    end = len(words[0]); lst = []

    for i in range(0, n):
        start = end + 1
        end = start + len(words[i+1])
        lst.append([WORDTYPE[i%2], start, end])

    return lst

def formatType2(sentence, noun2, words):

    if len(words) == 2:
        start = 0; end = len(words[0]); index = 1
    else:
        start = len(words[0]) + 1
        end = start + len(words[1])
        index = 2

    lst = [[WORDTYPE[0], start, end]]

    noun2 = noun2[1:]
    length = len(noun2)
    wordlength = len(words[index])

    if not words[index].endswith(noun2, 0, wordlength):
        length += 2

    isenzo = words[index][:wordlength-length]
    start = sentence.find(isenzo, 0, len(sentence))
    end = start + len(isenzo)

    lst.append([WORDTYPE[1], start, end])
    lst.append([WORDTYPE[0], end, end + length])
    return lst

def getFormats(sentence, n):
    words = sentence.split(' ')

    if type(n) == str:
        return formatType2(sentence, n, words)
    elif n == 0:
        return [['t', 0, len(sentence)]]
    elif n == -1:
        return []
    else:
        return formatType1(sentence, n, words)

def loadOntology(path, iri):
    try:
        onto_extractor = OntologyExtractor(path, iri)
    except Exception as e:
        return False

    return True

def printlog(title, errors, descr):
    with open('Error.log','a') as logfile:
        print(title, descr, file=logfile)
        [print(e, file=logfile) for e in errors]
        print('',file=logfile)

def printResult(path, iri):
    onto_extractor = OntologyExtractor(path, iri)
    onto_extractor.extract()

    for (k, v) in onto_extractor.my_dict.items():
        print(k)
        for i in v:
            [r, e] = evaluate(k, i)
            if e != None:
                print(e)
            else:
                print(r)
        print()

def storeResult(result, errors, body, i, k):
    [r, e] = result
    if e != None:
        errors.append(e)
    elif k in TYPE1:
        body.append([r, 3])
    elif k in TYPE2:
        body.append([r, i[1]])
    else:
        body.append([r, 0])

def data(path, iri):
    onto_extractor = OntologyExtractor(path, iri)
    onto_extractor.extract()
    result = []

    for (k, v) in onto_extractor.my_dict.items():
        body = []; errors = []

        [storeResult(evaluate(k, i), errors, body, i, k) for i in v]

        if len(body) > 0:
            result = result + [[k, 0]] + body + [['', -1]]

        diff = len(v) - len(body)
        if len(errors) != 0:
            printlog(k, errors,"{d}:{t}".format(d=str(diff), t=str(len(v))))

    return result
