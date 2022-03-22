import tkinter
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
from PIL import ImageTk, Image


Konstruktor = tkinter.Tk()
Konstruktor.geometry("800x400")
Konstruktor.title("Tytuł aplikacji")

def DodajTekst():
    #tkinter.Label(Konstruktor, text=CB.get()).grid()
    if CB.get() == "Ping":
        tkinter.Label(Konstruktor, text="1").grid()
        Konstruktor.quit()
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
    Obrazek = ImageTk.PhotoImage(Image.open("Python/OIP.jpg"))
    insLabel = tkinter.Label(NowyKonstruktor,image=Obrazek, text="Nowe okno").pack()
    NowyKonstruktor.mainloop()

def WybranieZdarzenia():
    #print(ListaZdarzen.get(ListaZdarzen.curselection()))
    wynikpopup = messagebox.askyesno("Tytuł", str(ListaZdarzen.get(ListaZdarzen.curselection())))

Okno_Glowne = tkinter.Frame(Konstruktor, borderwidth=2)

TekstGlowny = tkinter.Label(Konstruktor, text="Hello, World")
Przycisk = tkinter.Button(Konstruktor, text="Exit", command=DodajTekst)
Wpis = tkinter.Entry(Konstruktor)
CB = tkinter.StringVar()
ListaZdarzen = tkinter.Listbox(Konstruktor)
SuwakListyZdarzen = tkinter.Scrollbar(Konstruktor)


CheckButt = tkinter.Checkbutton(Konstruktor, text="Ping", variable=CB, onvalue="Ping", offvalue="No Ping")
CheckButt.deselect()

PopButt = tkinter.Button(Konstruktor, text="Popup", command=pop)

Opcje = ["Pon","Wt","Śr",]
CombBox = ttk.Combobox(Konstruktor,value=Opcje)

PrzyciskNoweOkno = tkinter.Button(Konstruktor, text="Nowe okno", command=KonstruktorNowegoOkna)
PrzyciskWybranejPozycjiZListy = tkinter.Button(Konstruktor,text='Wybrane Zdarzenie', command=WybranieZdarzenia)


filenamebox = filedialog.askopenfilename(initialdir="/", title="szukane" , filetypes=(("PNG","*.png"),("ALL","*.*")))
TekstGlowny.grid(row=0, column=0)
Przycisk.grid(row=0, column=1)
Wpis.grid(row=0, column=2)
CheckButt.grid(row=0, column=3)
PopButt.grid(row=0, column=4)
CombBox.grid(row=0, column=5)
PrzyciskNoweOkno.grid(row=0, column=6)
PrzyciskWybranejPozycjiZListy.grid(row=0, column=7)

ListaZdarzen.grid(row=1, column=0)
SuwakListyZdarzen.grid(row=1, column=1, sticky="NSEW")
SuwakListyZdarzen.config(command=ListaZdarzen.yview)
ListaZdarzen.config(yscrollcommand=SuwakListyZdarzen)

for a in range(20):
    ListaZdarzen.insert(a, "Zdarzenie" + str(a))
ListaZdarzen.activate(0)
#ListaZdarzen.bind("<<ListboxSelect>>",WybranieZdarzenia())

#print((ListaZdarzen.get(ListaZdarzen.curselection())))
Konstruktor.mainloop()