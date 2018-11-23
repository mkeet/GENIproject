from tkinter import *
from controller import *

mainwindow = Tk()
status = StringVar()
scrollbar = Scrollbar(mainwindow)
textArea = Text(mainwindow, fg="blue", state=DISABLED, wrap=NONE, yscrollcommand=scrollbar.set)
scrollbar.config(command=textArea.yview)
textArea.tag_config("noun", foreground="red")
textArea.tag_config("verb", foreground="green")
textArea.tag_config("title", foreground="black")

END = INSERT
def printToTextArea(data, formats, lnum):
    textArea.config(state=NORMAL)
    textArea.insert(END, data)

    for f in formats:
        if f[0] == 'n':
            name = 'noun'
        elif f[0] == 'v':
            name = 'verb'
        else:
            name = 'title'

        # print(f)
        s = "{ln}.{s} {ln}.{e}".format(ln=lnum, s = f[1], e = f[2])
        [startIndex, endIndex] = s.split(' ')
        textArea.tag_add(name, startIndex, endIndex)

    textArea.insert(END, '\n')
    textArea.config(state=DISABLED)


def run(path_str, iri_str):
    if len(path_str) < 1 or len(iri_str) < 1:
        status.set("Enter path or IRI")
        return

    if not loadOntology(path_str, iri_str):
        status.set("Enter correct path or IRI")
    else:
        status.set("Ontology Loaded")
        inp = data(path_str, iri_str)

        textArea.config(state=NORMAL)
        textArea.delete(1.0, END)
        textArea.config(state=DISABLED)

        for i in range(0,len(inp)):
            sentence = inp[i][0]
            param = inp[i][1]
            printToTextArea(sentence, getFormats(sentence, param) , i+1)

path = Entry(mainwindow, width=80)
iri = Entry(mainwindow, width=80)


loadButton = Button(mainwindow, text='Load', command=lambda: run(path.get(), iri.get()))

mainwindow.title('Zulu Ontology Verbaliser')
Label(mainwindow, text="Ontology Path:").grid(sticky=E)
Label(mainwindow, text="Ontology IRI:").grid(sticky=E)
path.grid(row=0, column=1)
iri.grid(row=1, column=1)
loadButton.grid(row=2, column=1, padx=15, pady=15, sticky=W)
textArea.grid(row=3, column=0, columnspan=2)
scrollbar.grid(row=3, column=2)

# ***** Status Bar *****
status.set("Welcome")
Label(mainwindow, textvariable=status, bd=1, relief=SUNKEN, anchor=W)\
    .grid(columnspan=3, sticky=W+E)

mainwindow.mainloop()
