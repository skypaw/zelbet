from tkinter import *
import slupy_symetryczne
import slupy_niesymetryczne
import slupy_diagnostyka
import slupy_functions


class menu:
    def __init__(self, master):
        menu_bg = Label(master, bg="#003366", fg="white")
        self.button1 = Button(menu_bg, text="Zbrojenie symetryczne", command=lambda: self.onclick(1, master))
        self.button2 = Button(menu_bg, text="Zbrojenie niesymetryczne", command=lambda: self.onclick(2, master))
        self.button3 = Button(menu_bg, text="Diagnostyka")

        menu_bg.pack()
        self.button1.pack()
        self.button2.pack()
        self.button3.pack()

    def onclick(self, args, master):
        if args == 1:
            zbrojenie_symetryczne(master)
        if args == 2:
            zbrojenie_niesymetryczne(master)


class zbrojenie_symetryczne:
    def __init__(self, master):
        self.zbrojenie_bg = Label(master)

        self.opis_1 = Label(self.zbrojenie_bg, text="Wysokość przekroju h [cm]")
        self.opis_2 = Label(self.zbrojenie_bg, text="Szerokość przekroju b [cm]")
        self.opis_3 = Label(self.zbrojenie_bg, text="Odległość a1 [mm]")
        self.opis_4 = Label(self.zbrojenie_bg, text="Odległość a2 [mm]")
        self.opis_5 = Label(self.zbrojenie_bg, text="Obliczeniowa wartość momentu zginającego [kNm]")
        self.opis_6 = Label(self.zbrojenie_bg, text="Obliczeniowa wartość siły normalnej [kN]")
        self.opis_7 = Label(self.zbrojenie_bg, text="Wybór betonu")

        self.dane_1 = Entry(self.zbrojenie_bg, width=6)
        self.dane_2 = Entry(self.zbrojenie_bg, width=6)
        self.dane_3 = Entry(self.zbrojenie_bg, width=6)
        self.dane_4 = Entry(self.zbrojenie_bg, width=6)
        self.dane_5 = Entry(self.zbrojenie_bg, width=6)
        self.dane_6 = Entry(self.zbrojenie_bg, width=6)

        var = StringVar()
        var.set("Wybierz klasę")
        self.dane_7 = OptionMenu(self.zbrojenie_bg, var, "C12","C16","C20","C25","C30","C35","C40","C45","C50","C55","C60","C70","C80","C90", command=self.option_menu)

        self.zbrojenie_bg.pack(side=RIGHT)
        self.opis_1.grid(row=1, sticky=E)
        self.opis_2.grid(row=2, sticky=E)
        self.opis_3.grid(row=3, sticky=E)
        self.opis_4.grid(row=4, sticky=E)
        self.opis_5.grid(row=5, sticky=E)
        self.opis_6.grid(row=6, sticky=E)
        self.opis_7.grid(row=7, sticky=E)

        self.dane_1.grid(row=1, column=1)
        self.dane_2.grid(row=2, column=1)
        self.dane_3.grid(row=3, column=1)
        self.dane_4.grid(row=4, column=1)
        self.dane_5.grid(row=5, column=1)
        self.dane_6.grid(row=6, column=1)
        self.dane_7.grid(row=7, column=1)

        self.button5 = Button(self.zbrojenie_bg, text="Obliczenia", command=self.onclick)
        self.button5.grid(row=10, columnspan=2, pady=10)

    def option_menu(self, selection):
        self.eta_bet, self.lambda_bet, self.f_cd = slupy_functions.calculated_value_concrete(selection)
        print(self.eta_bet, self.lambda_bet, self.f_cd)


    def onclick(self):

        h = float(self.dane_1.get().replace(',', '.')) * 10 ** -2
        b = float(self.dane_2.get().replace(',', '.')) * 10 ** -2
        a1 = float(self.dane_3.get().replace(',', '.')) * 10 ** -3
        a2 = float(self.dane_4.get().replace(',', '.')) * 10 ** -3
        m_ed = float(self.dane_5.get().replace(',', '.'))
        n_ed = float(self.dane_6.get().replace(',', '.'))

        as1, as2 =slupy_symetryczne.main(h, b, a1, a2, m_ed, n_ed, self.eta_bet, self.lambda_bet, self.f_cd)

        self.wynik_1 = Label(self.zbrojenie_bg, text=f"A_s1 = {as1} [cm^2]")
        self.wynik_1.grid(row=8, sticky=E)
        self.wynik_2 = Label(self.zbrojenie_bg, text=f"A_s2 = {as2} [cm^2]")
        self.wynik_2.grid(row=9, sticky=E)





root = Tk()
root.title("Obliczanie zbrojenia")

menu_pack = menu(root)

root.mainloop()
