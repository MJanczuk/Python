def OdczytPliku(SciezkaPliku):
    with open(SciezkaPliku, "r") as Odczyt:
        Plik = {}
        Plik['Wersja'] = Odczyt.readline()[9:-1]
        Plik['Tytul'] = Odczyt.readline()[7:-1]
        Plik['Czas'] = Odczyt.readline()[7:-1]
        Plik['Kanaly'] = (Odczyt.readline()[7:-1]).split()
        Plik['Kolory'] = (Odczyt.readline()[7:-1]).split()
        Odczyt.readline()
        l = len(Plik['Kanaly'])
        M = []
        for i in range(l):
            M.append([])
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
        return (Plik)
