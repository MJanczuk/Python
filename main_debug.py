import tkinter
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
from PIL import ImageTk, Image


Konstruktor = tkinter.Tk()
Konstruktor.geometry("600x300")
Konstruktor.title("Tytuł aplikacji")

def DodajTekst():
    #tkinter.Label(Konstruktor, text=CB.get()).grid()
    if CB.get() == "Ping":
        tkinter.Label(Konstruktor, text="1").grid()
    else:
        tkinter.Label(Konstruktor, text="0").grid()
    #tkinter.Label(Konstruktor, text=Wpis.get()).grid()

def pop():
    wynikpopup = messagebox.askyesno("Tytuł", "Treść")
    if wynikpopup == 1:
        tkinter.Label(Konstruktor, text="Tak").grid()
    else:
        tkinter.Label(Konstruktor, text="Nie").grid()

def KonstruktorNowegoOkna():
    NowyKonstruktor = tkinter.Toplevel()
    NowyKonstruktor.geometry("200x200")
    NowyKonstruktor.title("Nowe okno")
    Obrazek = ImageTk.PhotoImage(Image.open("OIP.jpg"))
    insLabel = tkinter.Label(NowyKonstruktor,image=Obrazek, text="Nowe okno").pack()
    NowyKonstruktor.mainloop()

Okno_Glowne = tkinter.Frame(Konstruktor, borderwidth=2)

TekstGlowny = tkinter.Label(Konstruktor, text="Hello, World")
Przycisk = tkinter.Button(Konstruktor, text="Exit", command=DodajTekst)
Wpis = tkinter.Entry(Konstruktor)
CB = tkinter.StringVar()

CheckButt = tkinter.Checkbutton(Konstruktor, text="Ping", variable=CB, onvalue="Ping", offvalue="No Ping")
CheckButt.deselect()

PopButt = tkinter.Button(Konstruktor, text="Popup", command=pop)

Opcje = ["Pon","Wt","Śr",]
CombBox = ttk.Combobox(Konstruktor,value=Opcje)

PrzyciskNoweOkno = tkinter.Button(Konstruktor, text="Nowe okno", command=KonstruktorNowegoOkna)

filenamebox = filedialog.askopenfilename(initialdir="/", title="szukane" , filetypes=(("PNG","*.png"),("ALL","*.*")))
TekstGlowny.grid(row=0, column=0)
Przycisk.grid(row=0, column=1)
Wpis.grid(row=0, column=2)
CheckButt.grid(row=0, column=3)
PopButt.grid(row=0, column=4)
CombBox.grid(row=0, column=5)
PrzyciskNoweOkno.grid(row=0, column=6)

Konstruktor.mainloop()