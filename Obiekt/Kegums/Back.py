import tkinter as tk
from tkinter import ttk


def Zakres(Arr, Min, Max):
    for i in range(len(Arr)):
        if Arr[i] <= Min:
            Imin = i
        if Arr[i] <= Max:
            Imax = i
    return (Imin+1,Imax)
'''
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