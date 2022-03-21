import tkinter
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
from PIL import ImageTk, Image

import TKEasy


Konstruktor = tkinter.Tk()
Konstruktor.geometry("1250x900")
Konstruktor.title("Program do obrabiania danych")

def DodajTekst(CB):
    #tkinter.Label(Konstruktor, text=CB.get()).grid()
    if CB.get() == "Ping":
        tkinter.Label(Konstruktor, text="1").grid()
    else:
        tkinter.Label(Konstruktor, text="0").grid()
    #tkinter.Label(Konstruktor, text=Wpis.get()).grid()
def RysujWykres():
    from matplotlib.backends.backend_tkagg import (
        FigureCanvasTkAgg, NavigationToolbar2Tk)
    # Implement the default Matplotlib key bindings.
    from matplotlib.backend_bases import key_press_handler
    from matplotlib.figure import Figure

    fig = Figure(figsize=(6, 3), dpi=200)
    ax = fig.add_subplot()
    for a in Kanaly.curselection():
        line, = ax.plot(Dane['X'][a], Dane['Y'][a], label=Kanaly.get(a))
        line.set_linewidth(1)
    ax.grid(True)
    ax.legend(bbox_to_anchor=(1,0), loc="lower right",bbox_transform=fig.transFigure, ncol=3)
    if (t1.get())>0 and (t2.get())>0:
        ax.set_xlim(xmin=t1, xmax=t2)
    ax.set_title(tytul.get())
    canvas = FigureCanvasTkAgg(fig, master=Konstruktor)  # A tk.DrawingArea.
    canvas.draw()
    toolbar = NavigationToolbar2Tk(canvas, Konstruktor, pack_toolbar=False)
    toolbar.update()
    #canvas.mpl_connect("key_press_event", lambda event: print(f"you pressed {event.key}"))
    #canvas.mpl_connect("key_press_event", key_press_handler)
    canvas.get_tk_widget().grid(row=1,pady=10,padx=10)
    #toolbar.grid(row=3)


def KonstruktorNowegoOkna():
    NowyKonstruktor = tkinter.Toplevel()
    NowyKonstruktor.geometry("200x200")
    NowyKonstruktor.title("Nowe okno")
    Obrazek = ImageTk.PhotoImage(Image.open("OIP.jpg"))
    insLabel = tkinter.Label(NowyKonstruktor,image=Obrazek, text="Nowe okno").pack()
    NowyKonstruktor.mainloop()


Okno_Glowne = tkinter.Frame(Konstruktor, borderwidth=2)

#TekstGlowny = tkinter.Label(Konstruktor, text="Hello, World")
#PrzyciskExit = tkinter.Button(Konstruktor, text="Exit", command=quit)

#CB = tkinter.StringVar()
#CheckButt = tkinter.Checkbutton(Konstruktor, text="Ping", variable=CB, onvalue="Ping", offvalue="No Ping")
#CheckButt.deselect()

#Opcje = ["Pon","Wt","Śr",]
#CombBox = ttk.Combobox(Konstruktor,value=Opcje)

#PrzyciskNoweOkno = tkinter.Button(Konstruktor, text="Nowe okno", command=KonstruktorNowegoOkna)

filenamebox = filedialog.askopenfilename(initialdir="/", title="Rejestracja" , filetypes=(("REC","*.rec"),("ALL","*.*")))
import AdapterIO
Dane = AdapterIO.OdczytPliku(filenamebox)

t1 = tkinter.IntVar()
t2 = tkinter.IntVar()
tytul = tkinter.StringVar('')
import GRAF
#GRAF.Standard((Dane['X'],Dane['Y']))

#PrzyciskExit.grid(column=2,row=0)


Kanaly = tkinter.Listbox(Konstruktor, selectmode='multiple')
#Kanaly.bind('<<ListboxSelect>>', RysujWykresEv)
for e in Dane['Kanaly']:
    Kanaly.insert(tkinter.END, e)
Kanaly.grid(column=1, row=1)


RamkaTytul = ttk.Labelframe(Konstruktor, text='Tytuł wykresu', borderwidth=2).grid(row=2, column=0)
ttk.Entry(RamkaTytul, textvariable=tytul).grid(row=2, column=1)
RamkaPolaT1 = ttk.Labelframe(Konstruktor,text='T0', borderwidth=2).grid(row=2, column=2)
PoleT1 = ttk.Entry(RamkaPolaT1,textvariable=t1).grid(row=2, column=3, padx=5, pady=5)
RamkaPolaT2 = ttk.Labelframe(Konstruktor,text='T1', borderwidth=2).grid(row=2, column=4)
PoleT2 = ttk.Entry(Konstruktor,textvariable=t2).grid(row=2, column=5)

ttk.Button(Konstruktor,text = 'Rysuj', command=RysujWykres).grid()

tkinter.Label(Konstruktor,text=(Dane['Tytul']+'       '+Dane['Czas'])).grid(column=0,row=0)

Konstruktor.mainloop()