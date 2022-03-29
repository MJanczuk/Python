import tkinter


def IEN_v1(SciezkaPliku = './Dane surowe/P1.rec',Surowe=True):
    if SciezkaPliku == '':
        SciezkaPliku = './Dane surowe/P1.rec'
    if '/' not in SciezkaPliku:
        if Surowe:
            SciezkaPliku = './Dane surowe/'+SciezkaPliku
        else:
            SciezkaPliku = './Dane wejściowe/' + SciezkaPliku
    with open(SciezkaPliku, "r") as Odczyt:
        Plik = {}
        Plik['Wersja'] = Odczyt.readline()[9:-1]
        Plik['Tytul'] = Odczyt.readline()[7:-1]
        Plik['Czas'] = Odczyt.readline()[7:-1]
        Plik['Kanaly'] = (Odczyt.readline()[7:-1]).split('\t')
        Plik['Kolory'] = Odczyt.readline()[8:-1].split('\t')
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
def Wpisz(Dane,SciezkaPliku):
    from datetime import datetime
    with open(SciezkaPliku, "w") as Zapis:
        today = datetime.now()
        NazwaPliku = ("Raport "+str(today.strftime("%dd_%mm_%Yr__%HH_%MM_%SS"))+".")
        Zapis.write(Dane)
def Bank(SciezkaDostepu):
    pass

def main1():
    import tkinter
    from tkinter import messagebox
    from tkinter import filedialog
    class Ramka(tkinter.Frame):
        def __init__(self, parent, label='o', **kwargs):
            super().__init__(parent, **kwargs)
            self.Ramka = tkinter.LabelFrame(parent,text=label).grid(row=0,column=0)
            self.Lista = tkinter.Listbox(self.Ramka).grid()


    TestGui = tkinter.Tk()
    TestGui.geometry("900x700")
    TestGui.title("Import danych")
    W = tkinter.StringVar()
    T = tkinter.StringVar()
    C = tkinter.StringVar()

    tkinter.Label(TestGui,text='Wersja:').grid(row=0,column=0,sticky=tkinter.E)
    tkinter.Entry(TestGui,textvariable=W,width=30).grid(row=0,column=1,sticky=tkinter.E)
    tkinter.Label(TestGui, text='Tytuł:').grid(row=1, column=0, sticky=tkinter.E)
    tkinter.Entry(TestGui,textvariable=T,width=30).grid(row=1,column=1,sticky=tkinter.E)
    tkinter.Label(TestGui, text='Czas:').grid(row=2, column=0, sticky=tkinter.E)
    tkinter.Entry(TestGui,textvariable=C,width=30).grid(row=2,column=1,sticky=tkinter.E)
    K = tkinter.Listbox(TestGui,width=30,height=30)
    KL = tkinter.Listbox(TestGui,width=10,height=30)

    #filenamebox = tkinter.filedialog.askopenfilename(initialdir="/", title="Rejestracja",filetypes=(("REC", "*.rec"), ("ALL", "*.*")))

    Dane = IEN_v1('P1.rec')
    W.set(Dane['Wersja'])
    T.set(Dane['Tytul'])
    C.set(Dane['Czas'])
    for e in Dane['Kanaly']:
        K.insert(tkinter.END,e)
    K.grid(column=1,row=3, sticky=tkinter.E)

    for e in Dane['Kolory']:
        KL.insert(tkinter.END,e)
    KL.grid(column=0,row=3,sticky=tkinter.E)


    from matplotlib.backends.backend_tkagg import (
        FigureCanvasTkAgg, NavigationToolbar2Tk)
    # Implement the default Matplotlib key bindings.
    from matplotlib.backend_bases import key_press_handler
    from matplotlib.figure import Figure

    fig = Figure(figsize=(3, 3), dpi=200)
    ax = fig.add_subplot()
    for a in range(len(Dane['X'])):
        line, = ax.plot(Dane['X'][a], Dane['Y'][a])
    line.set_linewidth(1)
    ax.grid(True)
    canvas = FigureCanvasTkAgg(fig, master=TestGui)  # A tk.DrawingArea.
    canvas.draw()
    toolbar = NavigationToolbar2Tk(canvas, TestGui, pack_toolbar=False)
    toolbar.update()
    # canvas.mpl_connect("key_press_event", lambda event: print(f"you pressed {event.key}"))
    # canvas.mpl_connect("key_press_event", key_press_handler)
    canvas.get_tk_widget().grid(row=0,column=2,rowspan=4, pady=10, padx=10)
    toolbar.grid(row=5,column=2)

    TestGui.mainloop()


if __name__ == '__main__':
    pass