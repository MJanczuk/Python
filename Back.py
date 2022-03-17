import tkinter as tk
from tkinter import ttk




root = tk.Tk()
root.title('Testowe okno')

def Rysuj():
    print(Stan.get(),NazwaKanalu.get(),OpcjaMinMax.current())



Kanal = ttk.Labelframe(root,text = 'Rejestrowana 1')
Kanal.grid(row=0,column=0)

Stan = tk.IntVar()
Aktywny = ttk.Checkbutton(Kanal, variable=Stan)
Aktywny.grid(row=0,column=0)

NazwaKanalu = tk.StringVar(value='Numer 1')
Nazwa = ttk.Entry(Kanal, textvariable=NazwaKanalu,width=30)
Nazwa.grid(row=0,column=1)

Opcje = ["","min","max","min/max"]
OpcjaMinMax = ttk.Combobox(Kanal,value=Opcje,width=10)
OpcjaMinMax.grid(row=0,column=2)

PrzyciskRysuj = tk.Button(root,text='Rysuj',command=Rysuj)
PrzyciskRysuj.grid(row=1,column=0)

tk.mainloop()