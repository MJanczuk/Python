import tkinter
import tkinter as tk
from tkinter import ttk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.sankey as sank

def main():
    Root = tk.Tk()
    tk.Label(text='Kierownica',font=18).grid(row=0,column=0,columnspan=2,padx=5,pady=5)
    tk.Label(text='Statyczna').grid(row=1, column=0, columnspan=1,padx=5,pady=5)
    tk.Label(text='Dynamiczna').grid(row=2, column=0, columnspan=1,padx=5,pady=5)
    tk.Label(text='Prędkość').grid(row=3, column=0, columnspan=1,padx=5,pady=5)
    ttk.Combobox().grid(row=1, column=1, columnspan=1)
    ttk.Combobox().grid(row=2, column=1, columnspan=1)
    ttk.Combobox().grid(row=3, column=1, columnspan=1)

    tk.Label(text='Wirnik',font=18).grid(row=0,column=2,columnspan=2,padx=5,pady=5)
    tk.Label(text='Statyczna').grid(row=1, column=2, columnspan=1,padx=5,pady=5)
    tk.Label(text='Dynamiczna').grid(row=2, column=2, columnspan=1,padx=5,pady=5)
    tk.Label(text='Prędkość').grid(row=3, column=2, columnspan=1,padx=5,pady=5)
    ttk.Combobox().grid(row=1, column=3, columnspan=1)
    ttk.Combobox().grid(row=2, column=3, columnspan=1)
    ttk.Combobox().grid(row=3, column=3, columnspan=1)

    tk.Label(text='Iglica',font=18).grid(row=0,column=4,columnspan=2,padx=5,pady=5)
    tk.Label(text='Statyczna').grid(row=1, column=4, columnspan=1,padx=5,pady=5)
    tk.Label(text='Dynamiczna').grid(row=2, column=4, columnspan=1,padx=5,pady=5)
    tk.Label(text='Prędkość').grid(row=3, column=4, columnspan=1,padx=5,pady=5)
    ttk.Combobox().grid(row=1, column=5, columnspan=1)
    ttk.Combobox().grid(row=2, column=5, columnspan=1)
    ttk.Combobox().grid(row=3, column=5, columnspan=1)

    tk.Label(text='Sekwencje regulatora',font=18).grid(row=4,column=0,columnspan=6)
    tk.Label(text='Uruchomienie\nsieć sztywna').grid(row=5, column=0, columnspan=1,padx=5,pady=5)
    tk.Label(text='Odstawienie\nplanowe').grid(row=6, column=0, columnspan=1,padx=5,pady=5)
    tk.Label(text='Odstawienie\nszybkie').grid(row=7, column=0, columnspan=1,padx=5,pady=5)
    tk.Label(text='Odstawienie\nawaryjne').grid(row=8, column=0, columnspan=1,padx=5,pady=5)
    ttk.Combobox().grid(row=5, column=1, columnspan=1)
    ttk.Combobox().grid(row=6, column=1, columnspan=1)
    ttk.Combobox().grid(row=7, column=1, columnspan=1)
    ttk.Combobox().grid(row=8, column=1, columnspan=1)

    tk.Label(text='Uruchomienie\npraca wyspowa').grid(row=5, column=2, columnspan=1,padx=5,pady=5)
    tk.Label(text='Uruchomienie\npraca pompowa').grid(row=6, column=2, columnspan=1,padx=5,pady=5)
    tk.Label(text='Uruchomienie\npraca kompensacyjna').grid(row=7, column=2, columnspan=1,padx=5,pady=5)
    ttk.Combobox().grid(row=5, column=3, columnspan=1)
    ttk.Combobox().grid(row=6, column=3, columnspan=1)
    ttk.Combobox().grid(row=7, column=3, columnspan=1)

    tk.Label(text='Zrzuty mocy', font=18).grid(row=9, column=0, columnspan=6)
    tk.Label(text='Obciążenie\n25%').grid(row=10, column=0, columnspan=1,padx=5,pady=5)
    tk.Label(text='Obciążenie\n50%').grid(row=11, column=0, columnspan=1,padx=5,pady=5)
    tk.Label(text='Obciążenie\n75%').grid(row=12, column=0, columnspan=1,padx=5,pady=5)
    tk.Label(text='Obciążenie\n100%').grid(row=13, column=0, columnspan=1,padx=5,pady=5)
    ttk.Combobox().grid(row=10, column=1, columnspan=1)
    ttk.Combobox().grid(row=11, column=1, columnspan=1)
    ttk.Combobox().grid(row=12, column=1, columnspan=1)
    ttk.Combobox().grid(row=13, column=1, columnspan=1)

    tk.Label(text='Praca\npompowa').grid(row=10, column=2, columnspan=1,padx=5,pady=5)
    tk.Label(text='Praca\nkompensacyjna').grid(row=11, column=2, columnspan=1,padx=5,pady=5)
    ttk.Combobox().grid(row=10, column=3, columnspan=1)
    ttk.Combobox().grid(row=11, column=3, columnspan=1)


    tk.Label(text='Zasilacz hydrauliczny', font=18).grid(row=14, column=0, columnspan=6)
    tk.Label(text='Ilosc suwów z\nminimalnego ciśnienia').grid(row=15, column=0, columnspan=1,padx=5,pady=5)
    tk.Label(text='Progi ciśnienia').grid(row=16, column=0, columnspan=1,padx=5,pady=5)
    tk.Label(text='Praca pompy\nna postoju').grid(row=17, column=0, columnspan=1,padx=5,pady=5)
    tk.Label(text='Praca pompy\npodczas pracy').grid(row=18, column=0, columnspan=1,padx=5,pady=5)
    ttk.Combobox().grid(row=15, column=1, columnspan=1)
    ttk.Combobox().grid(row=16, column=1, columnspan=1)
    ttk.Combobox().grid(row=17, column=1, columnspan=1)
    ttk.Combobox().grid(row=18, column=1, columnspan=1)
    Root.mainloop()
if __name__ == '__main__':
    main()