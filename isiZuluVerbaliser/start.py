import sys

ui = True

if len(sys.argv) == 2:
    ui = eval(sys.argv[1].replace('-ui=',''))

if ui:
    import ui
else:
    print()
    path = input('Enter Path :')
    iri = input('Enter IRI :')
    print()
    
    from controller import printResult
    printResult(path, iri)
