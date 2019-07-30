import numpy as np

from slupy_functions import x_solution
from slupy_functions import start_parameters
from slupy_functions import const_parameters

print("Projektowanie zbrojenia symetrycznego\n")  # symmetrical reinforcment

f_yd = float(input("Obliczeniowa granica plastyczności stali [MPa]: "))
es = float(input("Granica sprężystości stali [GPa]: ")) * 10 ** 3

# to do: add table with concrete strengh, to choose which we wan-t to use, yet idk how

lambda_bet = float(0.8)
eta_bet = float(1)
f_cd = float(17.9)  # const concrete C25/30

# const

epsilon_cu3 = const_parameters[0]
epsilon_c3 = const_parameters[1]

print(f"Obliczeniowa granica plastyczności stali {f_yd} [MPa]")
print(f"Moduł Younga {es} [MPa]")

# dimensions

a1 = float(input("Wartość otuliny a1 [mm]: ")) * 10 ** -3
a2 = float(input("Wartość otuliny a2 [mm]: ")) * 10 ** -3
h = float(input("Wysokość przekroju [cm]: ")) * 10 ** -2
b = float(input("Szerokość przekroju [cm]: ")) * 10 ** -2

d = round(h - a1, 4)

print(f"Wysokość użyteczna przekroju [m] {d}")

# eccentricity

m_ed = float(input("Wielkość momentu w przekroju: "))
n_ed = float(input("Wielkość siły normalnej w przekroju: "))

e, e_s1, e_s2 = eccentricity(m_ed, n_ed, h, a1, a2)

print(f"Mimośród e = {e} [m]")
print(f"Mimośród e_s1 = {e_s1} [m]")
print(f"Mimośród e_s2 = {e_s2} [m]")

# calculations

x_lim, epsilon_yd, x_min_minus_yd, x_min_yd, x_0, x_max_yd = start_parameters(epsilon_cu3, epsilon_c3,
                                                                              f_yd, es, a2, h, d)

print(f"x_lim {x_lim}")
print(f"x_min_minus_yd {x_min_minus_yd}")
print(f"x_min_yd {x_min_yd}")
print(f"x_0 {x_0}")
print(f"x_max_yd {x_max_yd}")