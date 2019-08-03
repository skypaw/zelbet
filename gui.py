from tkinter import *
import slupy_symetryczne
import slupy_niesymetryczne
import slupy_diagnostyka

def zbroj_sym():


    opis_tytul = Label(ramka, text="Zbrojenie symetryczne")
    opis_1 = Label(ramka, text="Wysokość przekroju h [cm]")
    opis_2 = Label(ramka, text="Szerokość przekroju b [cm]")
    opis_3 = Label(ramka, text="Odległość a1 [mm]")
    opis_4 = Label(ramka, text="Odległość a2 [mm]")
    opis_5 = Label(ramka, text="Obliczeniowa wartość momentu zginającego [kNm]")
    opis_6 = Label(ramka, text="Obliczeniowa wartość siły normalnej [kN]")

    dane_1 = Entry(ramka, width=6)
    dane_2 = Entry(ramka, width=6)
    dane_3 = Entry(ramka, width=6)
    dane_4 = Entry(ramka, width=6)
    dane_5 = Entry(ramka, width=6)
    dane_6 = Entry(ramka, width=6)

    ramka.pack(side=LEFT)


    opis_tytul.grid(row=0, columnspan=2)
    opis_1.grid(row=1, sticky=E)
    opis_2.grid(row=2, sticky=E)
    opis_3.grid(row=3, sticky=E)
    opis_4.grid(row=4, sticky=E)
    opis_5.grid(row=5, sticky=E)
    opis_6.grid(row=6, sticky=E)

    dane_1.grid(row=1, column=1)
    dane_2.grid(row=2, column=1)
    dane_3.grid(row=3, column=1)
    dane_4.grid(row=4, column=1)
    dane_5.grid(row=5, column=1)
    dane_6.grid(row=6, column=1)

    def clicked():

        obliczenia.pack(side=LEFT, fill=X)

        h = float(dane_1.get().replace(',', '.')) * 10 ** -2
        b = float(dane_2.get().replace(',', '.')) * 10 ** -2
        a1 = float(dane_3.get().replace(',', '.')) * 10 ** -3
        a2 = float(dane_4.get().replace(',', '.')) * 10 ** -3
        m_ed = float(dane_5.get().replace(',', '.'))
        n_ed = float(dane_6.get().replace(',', '.'))

        as1, as2 =slupy_symetryczne.main(h, b, a1, a2, m_ed, n_ed)

        wynik_1 = Label(obliczenia, text=f"A_s1 = {as1} [cm^2]")
        wynik_1.grid(row=8, sticky=E)
        wynik_2 = Label(obliczenia, text=f"A_s2 = {as2} [cm^2]")
        wynik_2.grid(row=9, sticky=E)



    button5 = Button(ramka, text="Obliczenia", command=clicked)
    button5.grid(row=7, columnspan=2, pady=10)


def zbroj_niesym():  # XD "end" have to do smth with that, maybe function again 


    opis_tytul = Label(ramka, text="Zbrojenie niesymetryczne")
    opis_1 = Label(ramka, text="Wysokość przekroju h [cm]")
    opis_2 = Label(ramka, text="Szerokość przekroju b [cm]")
    opis_3 = Label(ramka, text="Odległość a1 [mm]")
    opis_4 = Label(ramka, text="Odległość a2 [mm]")
    opis_5 = Label(ramka, text="Obliczeniowa wartość momentu zginającego [kNm]")
    opis_6 = Label(ramka, text="Obliczeniowa wartość siły normalnej [kN]")

    dane_1 = Entry(ramka, width=6)
    dane_2 = Entry(ramka, width=6)
    dane_3 = Entry(ramka, width=6)
    dane_4 = Entry(ramka, width=6)
    dane_5 = Entry(ramka, width=6)
    dane_6 = Entry(ramka, width=6)

    ramka.pack(side=LEFT)


    opis_tytul.grid(row=0, columnspan=2)
    opis_1.grid(row=1, sticky=E)
    opis_2.grid(row=2, sticky=E)
    opis_3.grid(row=3, sticky=E)
    opis_4.grid(row=4, sticky=E)
    opis_5.grid(row=5, sticky=E)
    opis_6.grid(row=6, sticky=E)

    dane_1.grid(row=1, column=1)
    dane_2.grid(row=2, column=1)
    dane_3.grid(row=3, column=1)
    dane_4.grid(row=4, column=1)
    dane_5.grid(row=5, column=1)
    dane_6.grid(row=6, column=1)

    def clicked():

        obliczenia.pack(side=LEFT, fill=X)

        h = float(dane_1.get().replace(',', '.')) * 10 ** -2
        b = float(dane_2.get().replace(',', '.')) * 10 ** -2
        a1 = float(dane_3.get().replace(',', '.')) * 10 ** -3
        a2 = float(dane_4.get().replace(',', '.')) * 10 ** -3
        m_ed = float(dane_5.get().replace(',', '.'))
        n_ed = float(dane_6.get().replace(',', '.'))

        as1, as2 =slupy_niesymetryczne.main(h, b, a1, a2, m_ed, n_ed)

        wynik_1 = Label(obliczenia, text=f"A_s1 = {as1} [cm^2]")
        wynik_1.grid(row=8, sticky=E)
        wynik_2 = Label(obliczenia, text=f"A_s2 = {as2} [cm^2]")
        wynik_2.grid(row=9, sticky=E)



    button5 = Button(ramka, text="Obliczenia", command=clicked)
    button5.grid(row=7, columnspan=2, pady=10)

def diagnostyka():


    opis_tytul = Label(ramka, text="Diagnostyka")
    opis_1 = Label(ramka, text="Wysokość przekroju h [cm]")
    opis_2 = Label(ramka, text="Szerokość przekroju b [cm]")
    opis_3 = Label(ramka, text="Odległość a1 [mm]")
    opis_4 = Label(ramka, text="Odległość a2 [mm]")
    opis_5 = Label(ramka, text="Obliczeniowa wartość momentu zginającego [kNm]")
    opis_6 = Label(ramka, text="Obliczeniowa wartość siły normalnej [kN]")
    opis_7 = Label(ramka, text="Przyjęte zbrojenie As_1 [cm^2]")
    opis_8 = Label(ramka, text="Przyjęte zbrojenie As_2 [cm^2]")

    dane_1 = Entry(ramka, width=6)
    dane_2 = Entry(ramka, width=6)
    dane_3 = Entry(ramka, width=6)
    dane_4 = Entry(ramka, width=6)
    dane_5 = Entry(ramka, width=6)
    dane_6 = Entry(ramka, width=6)
    dane_7 = Entry(ramka, width=6)
    dane_8 = Entry(ramka, width=6)

    ramka.pack(side=LEFT)


    opis_tytul.grid(row=0, columnspan=2)
    opis_1.grid(row=1, sticky=E)
    opis_2.grid(row=2, sticky=E)
    opis_3.grid(row=3, sticky=E)
    opis_4.grid(row=4, sticky=E)
    opis_5.grid(row=5, sticky=E)
    opis_6.grid(row=6, sticky=E)
    opis_7.grid(row=7, sticky=E)
    opis_8.grid(row=8, sticky=E)

    dane_1.grid(row=1, column=1)
    dane_2.grid(row=2, column=1)
    dane_3.grid(row=3, column=1)
    dane_4.grid(row=4, column=1)
    dane_5.grid(row=5, column=1)
    dane_6.grid(row=6, column=1)
    dane_7.grid(row=7, column=1)
    dane_8.grid(row=8, column=1)

    def clicked():

        obliczenia.pack(side=LEFT, fill=X)

        h = float(dane_1.get().replace(',', '.')) * 10 ** -2
        b = float(dane_2.get().replace(',', '.')) * 10 ** -2
        a1 = float(dane_3.get().replace(',', '.')) * 10 ** -3
        a2 = float(dane_4.get().replace(',', '.')) * 10 ** -3
        m_ed = float(dane_5.get().replace(',', '.'))
        n_ed = float(dane_6.get().replace(',', '.'))
        a_s1 = float(dane_7.get().replace(',', '.')) * 10 ** -4
        a_s2 = float(dane_8.get().replace(',', '.')) * 10 ** -4

        m_rd, n_rd =slupy_diagnostyka.main(h, b, a1, a2, m_ed, n_ed, a_s1, a_s2)

        wynik_1 = Label(obliczenia, text=f"Med = {m_rd} [cm^2]")
        wynik_1.grid(row=8, sticky=E)
        wynik_2 = Label(obliczenia, text=f"Ned = {n_rd} [cm^2]")
        wynik_2.grid(row=9, sticky=E)



    button5 = Button(ramka, text="Obliczenia", command=clicked)
    button5.grid(row=10, columnspan=2, pady=10)



root = Tk()

menu = Label(root, bg="#003366", fg="white")
menu.pack(side=LEFT, fill=Y)
ramka = Frame(root, padx=20, pady=10)
obliczenia = Frame(root)


button1 = Button(menu, text="Zbrojenie symetryczne", command=zbroj_sym)
button2 = Button(menu, text="Zbrojenie niesymetryczne", command=zbroj_niesym)
button3 = Button(menu, text="Diagnostyka", command=diagnostyka)

button1.pack()
button2.pack()
button3.pack()

root.mainloop()
