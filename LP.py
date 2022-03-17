def OdczytPliku(SciezkaPliku = './Dane surowe/P1.rec'):
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

    def RysujWykres():
        from matplotlib.backends.backend_tkagg import (
            FigureCanvasTkAgg, NavigationToolbar2Tk)
        # Implement the default Matplotlib key bindings.
        from matplotlib.backend_bases import key_press_handler
        from matplotlib.figure import Figure

        fig = Figure(figsize=(5, 4), dpi=200)
        ax = fig.add_subplot()
        for a in Kanaly.curselection():
            line, = ax.plot(Dane['X'][a],Dane['Y'][a])
        ax.set_xlabel("[s]")
        ax.set_ylabel("[%]")
        canvas = FigureCanvasTkAgg(fig, master=Konstruktor)  # A tk.DrawingArea.
        canvas.draw()
        canvas.mpl_connect("key_press_event", lambda event: print(f"you pressed {event.key}"))
        canvas.mpl_connect("key_press_event", key_press_handler)
        canvas.get_tk_widget().grid(row=1, column=1)
    def ImportDanych():
        filenamebox = filedialog.askopenfilename(initialdir="/", title="Rejestracja", filetypes=(("REC", "*.rec"), ("ALL", "*.*")))
        import LP
        Dane = LP.OdczytPliku(filenamebox)
        Kanaly.bind('<<ListboxSelect>>', onselect)
        for e in Dane['Kanaly']:
            Kanaly.insert(tkinter.END, e)

    filenamebox = filedialog.askopenfilename(initialdir="/", title="Rejestracja" , filetypes=(("REC","*.rec"),("ALL","*.*")))
    import LP
    Dane = LP.OdczytPliku()

    tkinter.Label(Konstruktor,text=filenamebox).grid(column=0,row=0)
    NowyWykres = tkinter.Button(Konstruktor, text="Wykres", command=RysujWykres).grid(column=0,row=1)
    NoweDane = tkinter.Button(Konstruktor, text="Dane", command=ImportDanych).grid(column=0, row=2)
    Kanaly = tkinter.Listbox(Konstruktor, selectmode='multiple')
    Kanaly.bind('<<ListboxSelect>>', onselect)
    for e in Dane['Kanaly']:
        Kanaly.insert(tkinter.END, e)
    Kanaly.grid(column=0,row=3)
    Konstruktor.mainloop()

if __name__ == '__main__':
    main()