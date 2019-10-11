# coding=utf-8

from tkinter import *
import slupy_symetryczne
import slupy_niesymetryczne
import slupy_diagnostyka
import slupy_functions


class Menu:
    def __init__(self, master):
        container = Frame(master, bg="#003366")
        container.pack()

        menu_bg = Label(container, bg="#003366", fg="white", pady=15)
        countings_bg = Frame(container)

        self.button1 = Button(menu_bg, text="Zbrojenie symetryczne", command=lambda: self.onclick(1, countings_bg),
                              width=20)
        self.button2 = Button(menu_bg, text="Zbrojenie niesymetryczne", command=lambda: self.onclick(2, countings_bg),
                              width=20)
        self.button3 = Button(menu_bg, text="Diagnostyka", command=lambda: countings_bg.pack_forget(), width=20)

        menu_bg.pack(side=LEFT, fill=Y)

        self.button1.pack()
        self.button2.pack()
        self.button3.pack()

    def onclick(self, args, countings_bg):
        if args == 1:
            countings_bg.pack()
            SymmetricReinforcement(countings_bg)

        if args == 2:
            countings_bg.pack()
            AsymmetricReinforcement(countings_bg)


class SymmetricReinforcement:
    def __init__(self, master):
        self.desc_1 = Label(master, text="Wysokość przekroju h [cm]")
        self.desc_2 = Label(master, text="Szerokość przekroju b [cm]")
        self.desc_3 = Label(master, text="Odległość a1 [mm]")
        self.desc_4 = Label(master, text="Odległość a2 [mm]")
        self.desc_5 = Label(master, text="Obliczeniowa wartość momentu zginającego [kNm]")
        self.desc_6 = Label(master, text="Obliczeniowa wartość siły normalnej [kN]")
        self.desc_7 = Label(master, text="Wybór betonu")

        self.data_1 = Entry(master, width=6)
        self.data_2 = Entry(master, width=6)
        self.data_3 = Entry(master, width=6)
        self.data_4 = Entry(master, width=6)
        self.data_5 = Entry(master, width=6)
        self.data_6 = Entry(master, width=6)

        var = StringVar()
        var.set("Klasa")

        self.data_7 = OptionMenu(master, var, "C12/15", "C16/20", "C20/25", "C25/30", "C30/37", "C35/45",
                                 "C40/50", "C45/55", "C50/60",
                                 "C55/67", "C60/75", "C70/85", "C80/95", "C90/105", command=self.option_menu)
        self.data_7.config(width=10)

        self.desc_1.grid(row=1, sticky=E)
        self.desc_2.grid(row=2, sticky=E)
        self.desc_3.grid(row=3, sticky=E)
        self.desc_4.grid(row=4, sticky=E)
        self.desc_5.grid(row=5, sticky=E)
        self.desc_6.grid(row=6, sticky=E)
        self.desc_7.grid(row=7, sticky=E)

        self.data_1.grid(row=1, column=1)
        self.data_2.grid(row=2, column=1)
        self.data_3.grid(row=3, column=1)
        self.data_4.grid(row=4, column=1)
        self.data_5.grid(row=5, column=1)
        self.data_6.grid(row=6, column=1)
        self.data_7.grid(row=7, column=1, stick="ew")

        self.button5 = Button(master, text="Obliczenia", command=self.onclick)
        self.button5.grid(row=9, columnspan=2, pady=10)

        as1, as2 = [0, 0]
        self.eta_bet, self.lambda_bet, self.f_cd, self.f_ctm = [0, 0, 0, 0]

        self.result_1 = Label(master)
        self.result_1.config(text=f"A_s1 = {as1} [cm^2]")
        self.result_1.grid(row=12, sticky=E)

        self.result_2 = Label(master)
        self.result_2.config(text=f"A_s2 = {as2} [cm^2]")
        self.result_2.grid(row=13, sticky=E)

    def option_menu(self, selection):
        self.eta_bet, self.lambda_bet, self.f_cd, self.f_ctm = slupy_functions.calculated_value_concrete(selection)
        print(self.eta_bet, self.lambda_bet, self.f_cd)

    def onclick(self):
        h = float(self.data_1.get().replace(',', '.')) * 10 ** -2
        b = float(self.data_2.get().replace(',', '.')) * 10 ** -2
        a1 = float(self.data_3.get().replace(',', '.')) * 10 ** -3
        a2 = float(self.data_4.get().replace(',', '.')) * 10 ** -3
        m_ed = float(self.data_5.get().replace(',', '.'))
        n_ed = float(self.data_6.get().replace(',', '.'))

        as1, as2 = slupy_symetryczne.main(h, b, a1, a2, m_ed, n_ed, self.eta_bet, self.lambda_bet, self.f_cd)

        as1 = round(as1, 2)
        as2 = round(as2, 2)

        self.result_1.config(text=f"A_s1 = {as1} [cm^2]")
        self.result_2.config(text=f"A_s2 = {as2} [cm^2]")


class AsymmetricReinforcement:
    def __init__(self, master):
        self.desc_1 = Label(master, text="Wysokość przekroju h [cm]")
        self.desc_2 = Label(master, text="Szerokość przekroju b [cm]")
        self.desc_3 = Label(master, text="Odległość a1 [mm]")
        self.desc_4 = Label(master, text="Odległość a2 [mm]")
        self.desc_5 = Label(master, text="Obliczeniowa wartość momentu zginającego [kNm]")
        self.desc_6 = Label(master, text="Obliczeniowa wartość siły normalnej [kN]")
        self.desc_7 = Label(master, text="Wybór betonu")

        self.data_1 = Entry(master, width=6)
        self.data_2 = Entry(master, width=6)
        self.data_3 = Entry(master, width=6)
        self.data_4 = Entry(master, width=6)
        self.data_5 = Entry(master, width=6)
        self.data_6 = Entry(master, width=6)

        var = StringVar()
        var.set("Klasa")

        self.data_7 = OptionMenu(master, var, "C12/15", "C16/20", "C20/25", "C25/30", "C30/37", "C35/45",
                                 "C40/50", "C45/55", "C50/60",
                                 "C55/67", "C60/75", "C70/85", "C80/95", "C90/105", command=self.option_menu)
        self.data_7.config(width=10)

        self.desc_1.grid(row=1, sticky=E)
        self.desc_2.grid(row=2, sticky=E)
        self.desc_3.grid(row=3, sticky=E)
        self.desc_4.grid(row=4, sticky=E)
        self.desc_5.grid(row=5, sticky=E)
        self.desc_6.grid(row=6, sticky=E)
        self.desc_7.grid(row=7, sticky=E)

        self.data_1.grid(row=1, column=1)
        self.data_2.grid(row=2, column=1)
        self.data_3.grid(row=3, column=1)
        self.data_4.grid(row=4, column=1)
        self.data_5.grid(row=5, column=1)
        self.data_6.grid(row=6, column=1)
        self.data_7.grid(row=7, column=1, stick="ew")

        self.button5 = Button(master, text="Obliczenia", command=self.onclick)
        self.button5.grid(row=9, columnspan=2, pady=10)

        as1, as2 = [0, 0]
        self.eta_bet, self.lambda_bet, self.f_cd, self.f_ctm = [0, 0, 0, 0]

        self.result_1 = Label(master)
        self.result_1.config(text=f"A_s1 = {as1} [cm^2]")
        self.result_1.grid(row=12, sticky=E)

        self.result_2 = Label(master)
        self.result_2.config(text=f"A_s2 = {as2} [cm^2]")
        self.result_2.grid(row=13, sticky=E)

    def option_menu(self, selection):
        self.eta_bet, self.lambda_bet, self.f_cd, self.f_ctm = slupy_functions.calculated_value_concrete(selection)
        print(self.eta_bet, self.lambda_bet, self.f_cd)

    def onclick(self):
        h = float(self.data_1.get().replace(',', '.')) * 10 ** -2
        b = float(self.data_2.get().replace(',', '.')) * 10 ** -2
        a1 = float(self.data_3.get().replace(',', '.')) * 10 ** -3
        a2 = float(self.data_4.get().replace(',', '.')) * 10 ** -3
        m_ed = float(self.data_5.get().replace(',', '.'))
        n_ed = float(self.data_6.get().replace(',', '.'))

        as1, as2 = slupy_niesymetryczne.main(h, b, a1, a2, m_ed, n_ed, self.eta_bet, self.lambda_bet, self.f_cd)

        as1 = round(as1, 2)
        as2 = round(as2, 2)
        self.result_1.config(text=f"A_s1 = {as1} [cm^2]")
        self.result_2.config(text=f"A_s2 = {as2} [cm^2]")


root = Tk()
root.title("Obliczanie zbrojenia")

Menu(root)
root.mainloop()
