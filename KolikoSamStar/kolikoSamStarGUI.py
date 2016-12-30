# !/usr/bin/python3
from tkinter import *
from tkinter import messagebox
import datetime
from dateutil.relativedelta import relativedelta

top = Tk()
top.geometry("300x300")
top.title("Koliko sam star?")

def hello():
    try:
        rodjendan = datetime.date(int(godina.get()), int(mjesec.get()), int(dan.get()))
        star = relativedelta(datetime.date.today(), rodjendan)
        var2.set('Rođen si %s.%s.%s.\n Ti si danas star točno\n%s godina, %s mjeseci i %s dana.' % (rodjendan.day, rodjendan.month, rodjendan.year, star.years, star.months, star.days))
    except (ValueError, TypeError):
        var2.set("Upisao si nevažeći datum.\n Pokušaj ponovno.")

    label2 = Label( top, width= 25, textvariable=var2)
    label2.place(relx=0.5, rely=0.8, anchor=CENTER)

var2 = StringVar()

B1 = Button(top, text = "Izračunaj koliko sam star", command = hello)
B1.place(relx=0.5, rely=0.6, anchor=CENTER)

var = StringVar()
label = Label( top, textvariable=var)
label.place(relx=0.5, rely=0.1, anchor=CENTER)
var.set("Unesi dan, mjesec i godinu rođenja:")

varDan = StringVar()
labelDan = Label( top, textvariable=varDan)
labelDan.place(relx=0.5, rely=0.2, anchor=E)
varDan.set("Dan:  ")

dan = Spinbox(top, wrap=True, width=5, from_=1, to=31)
dan.place(relx=0.5, rely=0.2, anchor=W)

varMjesec = StringVar()
labelMjesec = Label( top, textvariable=varMjesec)
labelMjesec.place(relx=0.5, rely=0.3, anchor=E)
varMjesec.set("Mjesec:  ")

mjesec = Spinbox(top, wrap=True, width=5, from_=1, to=12)
mjesec.place(relx=0.5, rely=0.3, anchor=W)

varGodina = StringVar()
labelGodina = Label( top, textvariable=varGodina)
labelGodina.place(relx=0.5, rely=0.4, anchor=E)
varGodina.set("Godina:  ")

godina = Spinbox(top, wrap=True, width=5, from_=1950, to=2016)
godina.place(relx=0.5, rely=0.4, anchor=W)

top.mainloop()