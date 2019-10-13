# coding=utf-8
from tkinter import *
from slupy import slupy_functions, slupy_diagnostyka, slupy_symetryczne, slupy_niesymetryczne


class Menu:
    def __init__(self, master):
        container = Frame(master, bg="#003366")
        container.pack()

        menu_bg = Label(container, bg="#003366", fg="white", pady=15)
        calculations_bg_symmetrical = Frame(container)
        calculations_bg_asymmetrical = Frame(container)
        calculations_bg_diagnostic = Frame(container)

        self.button1 = Button(menu_bg, text="Zbrojenie symetryczne",
                              command=lambda: self.onclick(1, calculations_bg_symmetrical, calculations_bg_asymmetrical,
                                                           calculations_bg_diagnostic),
                              width=20)
        self.button2 = Button(menu_bg, text="Zbrojenie niesymetryczne",
                              command=lambda: self.onclick(2, calculations_bg_symmetrical, calculations_bg_asymmetrical,
                                                           calculations_bg_diagnostic),
                              width=20)
        self.button3 = Button(menu_bg, text="Diagnostyka",
                              command=lambda: self.onclick(3, calculations_bg_symmetrical, calculations_bg_asymmetrical,
                                                           calculations_bg_diagnostic),
                              width=20)

        menu_bg.pack(side=LEFT, fill=Y)

        self.button1.pack()
        self.button2.pack()
        self.button3.pack()

    def onclick(self, args, calculations_bg_symmetrical, calculations_bg_asymmetrical, calculations_bg_diagnostic):
        if args == 1:
            calculations_bg_asymmetrical.forget()
            calculations_bg_diagnostic.forget()

            calculations_bg_symmetrical.pack()
            SymmetricReinforcement(calculations_bg_symmetrical)

        if args == 2:
            calculations_bg_symmetrical.forget()
            calculations_bg_diagnostic.forget()

            calculations_bg_asymmetrical.pack()
            AsymmetricReinforcement(calculations_bg_asymmetrical)

        if args == 3:
            calculations_bg_asymmetrical.forget()
            calculations_bg_symmetrical.forget()

            calculations_bg_diagnostic.pack()
            DiagnosticReinforcement(calculations_bg_diagnostic)


class SymmetricReinforcement:
    def __init__(self, master):
        self.desc_0 = Label(master, text="Zbrojenie symetryczne")
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

        self.desc_0.grid(row=1, columnspan=2, pady=10)
        self.desc_1.grid(row=2, sticky=E)
        self.desc_2.grid(row=3, sticky=E)
        self.desc_3.grid(row=4, sticky=E)
        self.desc_4.grid(row=5, sticky=E)
        self.desc_5.grid(row=6, sticky=E)
        self.desc_6.grid(row=7, sticky=E)
        self.desc_7.grid(row=8, sticky=E)

        self.data_1.grid(row=2, column=1)
        self.data_2.grid(row=3, column=1)
        self.data_3.grid(row=4, column=1)
        self.data_4.grid(row=5, column=1)
        self.data_5.grid(row=6, column=1)
        self.data_6.grid(row=7, column=1)
        self.data_7.grid(row=8, column=1, stick="ew")

        self.button5 = Button(master, text="Obliczenia", command=self.onclick)
        self.button5.grid(row=10, columnspan=2, pady=10)

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
        self.desc_0 = Label(master, text="Zbrojenie niesymetryczne")
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

        self.desc_0.grid(row=1, columnspan=2, pady=10)
        self.desc_1.grid(row=2, sticky=E)
        self.desc_2.grid(row=3, sticky=E)
        self.desc_3.grid(row=4, sticky=E)
        self.desc_4.grid(row=5, sticky=E)
        self.desc_5.grid(row=6, sticky=E)
        self.desc_6.grid(row=7, sticky=E)
        self.desc_7.grid(row=8, sticky=E)

        self.data_1.grid(row=2, column=1)
        self.data_2.grid(row=3, column=1)
        self.data_3.grid(row=4, column=1)
        self.data_4.grid(row=5, column=1)
        self.data_5.grid(row=6, column=1)
        self.data_6.grid(row=7, column=1)
        self.data_7.grid(row=8, column=1, stick="ew")

        self.button5 = Button(master, text="Obliczenia", command=self.onclick)
        self.button5.grid(row=10, columnspan=2, pady=10)

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


class DiagnosticReinforcement:
    def __init__(self, master):
        self.desc_0 = Label(master, text="Diagnostyka zbrojenia")
        self.desc_1 = Label(master, text="Wysokość przekroju h [cm]")
        self.desc_2 = Label(master, text="Szerokość przekroju b [cm]")
        self.desc_3 = Label(master, text="Odległość a1 [mm]")
        self.desc_4 = Label(master, text="Odległość a2 [mm]")
        self.desc_5 = Label(master, text="Obliczeniowa wartość momentu zginającego [kNm]")
        self.desc_6 = Label(master, text="Obliczeniowa wartość siły normalnej [kN]")
        self.desc_7 = Label(master, text="Pole zbrojenia As1 [cm^2]")
        self.desc_8 = Label(master, text="Pole zbrojenia As2 [cm^2]")
        self.desc_9 = Label(master, text="Wybór betonu")

        self.data_1 = Entry(master, width=6)
        self.data_2 = Entry(master, width=6)
        self.data_3 = Entry(master, width=6)
        self.data_4 = Entry(master, width=6)
        self.data_5 = Entry(master, width=6)
        self.data_6 = Entry(master, width=6)
        self.data_7 = Entry(master, width=6)
        self.data_8 = Entry(master, width=6)

        var = StringVar()
        var.set("Klasa")

        self.data_9 = OptionMenu(master, var, "C12/15", "C16/20", "C20/25", "C25/30", "C30/37", "C35/45",
                                 "C40/50", "C45/55", "C50/60",
                                 "C55/67", "C60/75", "C70/85", "C80/95", "C90/105", command=self.option_menu)
        self.data_9.config(width=10)

        self.desc_0.grid(row=1, columnspan=2, pady=10)
        self.desc_1.grid(row=2, sticky=E)
        self.desc_2.grid(row=3, sticky=E)
        self.desc_3.grid(row=4, sticky=E)
        self.desc_4.grid(row=5, sticky=E)
        self.desc_5.grid(row=6, sticky=E)
        self.desc_6.grid(row=7, sticky=E)
        self.desc_7.grid(row=8, sticky=E)
        self.desc_8.grid(row=9, sticky=E)
        self.desc_9.grid(row=10, sticky=E)

        self.data_1.grid(row=2, column=1)
        self.data_2.grid(row=3, column=1)
        self.data_3.grid(row=4, column=1)
        self.data_4.grid(row=5, column=1)
        self.data_5.grid(row=6, column=1)
        self.data_6.grid(row=7, column=1)
        self.data_7.grid(row=8, column=1)
        self.data_8.grid(row=9, column=1)
        self.data_9.grid(row=10, column=1, stick="ew")

        self.button5 = Button(master, text="Obliczenia", command=self.onclick)
        self.button5.grid(row=12, columnspan=2, pady=10)
        m_rd, n_rd = [0, 0]
        self.eta_bet, self.lambda_bet, self.f_cd, self.f_ctm = [0, 0, 0, 0]

        self.result_1 = Label(master)
        self.result_1.config(text=f"M_rd = {m_rd} [kNm]")
        self.result_1.grid(row=14, sticky=E)

        self.result_2 = Label(master)
        self.result_2.config(text=f"N_rd = {n_rd} [kN]")
        self.result_2.grid(row=15, sticky=E)

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
        as_1 = float(self.data_7.get().replace(',', '.')) * 10 ** -4
        as_2 = float(self.data_8.get().replace(',', '.')) * 10 ** -4

        m_rd, n_rd = slupy_diagnostyka.main(h, b, a1, a2, m_ed, n_ed, as_1, as_2,
                                            self.eta_bet, self.lambda_bet, self.f_cd)

        m_rd = round(m_rd, 2)
        n_rd = round(n_rd, 2)
        self.result_1.config(text=f"M_rd = {m_rd} [kNm]")
        self.result_2.config(text=f"N_rd = {n_rd} [kN]")


root = Tk()
root.title("Obliczanie zbrojenia")

Menu(root)
root.mainloop()
