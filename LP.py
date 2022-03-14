def OdczytPliku(SciezkaPliku):
    with open(SciezkaPliku, "r") as Odczyt:
        Plik = {}
        Plik['Wersja'] = Odczyt.readline()[9:-1]
        Plik['Tytul'] = Odczyt.readline()[7:-1]
        Plik['Czas'] = Odczyt.readline()[7:-1]
        Plik['Kanaly'] = (Odczyt.readline()[7:-1]).split('\t')
        Plik['Kolory'] = Odczyt.readline()[7:-1]
        Odczyt.readline()
        l = len(Plik['Kanaly'])
        M = []
        for i in range(l*2):
            M.append([])

        while True:
            dane = Odczyt.readline().replace(',','.')
            if dane == '':
                break
            dane = dane.split()
            for v in range(len(M)):
                M[v].append(float(dane[v]))
        X = []
        Y = []
        for i in range(l):
            X.append(M[i*2])
            Y.append(M[i*2+1])
        Plik['X'] = X
        Plik['Y'] = Y
        return(Plik)

def onselect(evt):
    # Note here that Tkinter passes an event object to onselect()
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    print('You selected item %d: "%s"' % (index, value))

def main():
    import tkinter
    from tkinter import messagebox
    from tkinter import filedialog

    Konstruktor = tkinter.Tk()
    Konstruktor.geometry("1000x300")
    Konstruktor.title("Import danych")

    def pop():
        if 1==0:
            wynikpopup = messagebox.askyesno("Tytuł", "Treść")
            if wynikpopup == 1:
                tkinter.Label(Konstruktor, text="Tak").grid()
            else:
                tkinter.Label(Konstruktor, text="Nie").grid()
        a = Kanaly.curselection()
        tkinter.Label(Konstruktor, text=a).grid()
        for x in a:
            tkinter.Label(Konstruktor, text=Kanaly.get(x)).grid()


        #import GRAF
        #GRAF.Standard(Dane)



    filenamebox = filedialog.askopenfilename(initialdir="/", title="Rejestracja" , filetypes=(("REC","*.rec"),("ALL","*.*")))
    import LP
    Dane = LP.OdczytPliku(filenamebox)

    tkinter.Label(Konstruktor,text=filenamebox).grid(column=0,row=0)
    PopButt = tkinter.Button(Konstruktor, text="Odczyt", command=pop).grid(column=1,row=0)
    Kanaly = tkinter.Listbox(Konstruktor, selectmode='multiple')
    Kanaly.bind('<<ListboxSelect>>', onselect)
    for e in Dane['Kanaly']:
        Kanaly.insert(tkinter.END,e)
    Kanaly.grid(column=0,row=1)
    Konstruktor.mainloop()

if __name__ == '__main__':
    main()