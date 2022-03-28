import tkinter as tk
from tkinter import ttk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.sankey as sank

def Zakres(Arr, Min, Max):
    for i in range(len(Arr)):
        if Arr[i] <= Min:
            Imin = i
        if Arr[i] <= Max:
            Imax = i
    return (Imin+1,Imax)
def GetDane(Path):
    return(pd.read_csv(Path,sep=',',usecols=["Data operacji","Data waluty","Typ transakcji","Kwota","Waluta","Saldo po transakcji","Opis transakcji","NadawcaOdbiorca","LokalizacjaCzas","Operacja","Karta","Ref"]))



fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, xticks=[], yticks=[], title="Elektrownia wodna")
flows = [ 1,-0.05,-0.15, -0.8]
sankey = sank.Sankey(ax=ax, unit=None)
sankey.add(flows=flows, labels=['Energia\nturbiny','Straty\ngeneratora','Pompa\nhydrauliki','Energia\nelektryczna'], orientations=[0, -1,-1, 0])
diagrams = sankey.finish()
plt.show()

Traficar2022 = [110.87,121.93,100.6,119.03,87.29,96.26,91.43,29.84]
Traficar2021k = [102.47,88.67,190.45,81.77,195.97,107.99,38.69,8.99,9.14,418.16,18.29,24.29,112.40,79.40,77.20,138.60,12.14,12.14,77.80,88.0,63.29,30.29,137.0,82.0,11.99]
Traficar2021d = ['31-12-2021','26-12-2021','30-10-2021','23-10-2021','16-10-2021','24-09-2021','19-09-2021','04-09-2021','02-09-2021','25-08-2021','24-08-2021','10-07-2021','08-07-2021','05-06-2021','15-05-2021','13-05-2021','04-05-2021','22-04-2021','17-04-2021','10-04-2021','06-04-2021','27-03-2021','25-03-2021','24-01-2021','24-01-2021']

'''print(sum(Traficar2021k)-418.16)
plt.figure(figsize=(5,5))
plt.bar(Traficar2021d,Traficar2021k)
plt.tick_params(axis='x',labelsize=15,rotation=90)
plt.tight_layout()
plt.show()
''''''
root = tk.Tk()
root.title('Testowe okno')
class Kanal(tk.Frame):
    def __init__(self, parent, label='Rejestrowana ', Numer='0', input_var=None, input_args=None, label_args=None, **kwargs):
        super().__init__(parent, **kwargs)
        input_args = input_args or {}
        label_args = label_args or {}
        self.variable = input_var
        self.Ramka = ttk.LabelFrame(root, text=(str(label)+str(Numer)), borderwidth=5)
        self.Ramka.grid(row=0, column=0)

        self.Stan = tk.IntVar()
        self.Aktywny = ttk.Checkbutton(self.Ramka, variable=self.Stan)
        self.Aktywny.grid(row=0, column=0)

        self.NazwaKanalu = tk.StringVar(value='Numer')
        self.Nazwa = ttk.Entry(self.Ramka, textvariable=self.NazwaKanalu, width=30)
        self.Nazwa.grid(row=0, column=1)


        self.Opcje = ["", "min", "max", "min/max"]
        PoleOpcja = ttk.Combobox(self.Ramka, value=self.Opcje, width=10)
        PoleOpcja.grid(row=0, column=2)
    def Konf(self):
        print(self.Stan.get(), self.NazwaKanalu.get(), self.OpcjaMinMax.current())
Kanaly = []
for i in range(5):
    Kanaly.append(Kanal(root,Numer=i).grid(row=i,column=i))

B1 = tk.Button(root, text='Print').grid()
tk.mainloop()
'''