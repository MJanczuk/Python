import tkinter


def IEN_v1(SciezkaPliku = './Dane surowe/P1.rec'):
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

def main():
    import tkinter
    from tkinter import messagebox
    from tkinter import filedialog
    class Ramka(tkinter.Frame):
        def __init__(self, parent, label='o', **kwargs):
            super().__init__(parent, **kwargs)
            self.Ramka = tkinter.LabelFrame(parent,text=label).grid(row=0,column=0)
            self.Lista = tkinter.Listbox(self.Ramka).grid()


    TestGui = tkinter.Tk()
    TestGui.geometry("1000x300")
    TestGui.title("Import danych")
    W = tkinter.StringVar()
    T = tkinter.StringVar()
    C = tkinter.StringVar()
    K = tkinter.StringVar()
    KL = tkinter.StringVar()
    tkinter.Entry(TestGui,textvariable=W).grid(sticky=tkinter.E)
    tkinter.Entry(TestGui,textvariable=T).grid(sticky=tkinter.E)
    tkinter.Entry(TestGui,textvariable=C).grid(sticky=tkinter.E)
    tkinter.Entry(TestGui,textvariable=K).grid(sticky=tkinter.E)
    tkinter.Entry(TestGui,textvariable=KL).grid(sticky=tkinter.E)

    Dane = IEN_v1()
    W.set(Dane['Wersja'])
    T.set(Dane['Tytul'])
    C.set(Dane['Czas'])
    K.set(Dane['Kanaly'])
    KL.set(Dane['Kolory'])
    TestGui.mainloop()


if __name__ == '__main__':
    main()