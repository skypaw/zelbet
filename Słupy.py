# http://www.se.put.poznan.pl/zkz/pracownicy/jacekscigallo/projekty/EC2_6.pdf
import numpy as np

print("Projektowanie zbrojenia symetrycznego\n")

fyd = float(input("Obliczeniowa granica plastyczności stali [MPa]: "))
Es = float(input("Granica sprężystości stali [GPa]: ")) * float(10 ** 3)

# Wartości które nie powinny być stałe tylko zależne  od klasy betonu, mam do tego tabelę ale nie wiem jak wkleić na razie
lambda1 = float(0.8)
eta1 = float(1)
fcd = float(17.9)

# Wartości stałe

Epsilon_cu3 = float(0.0035)
Epsilon_c3 = float(0.00175)

print(fyd)
print(str(Es) + " MPa")

# Właściwości geometryczne

a1 = float(input("Wartość otuliny a1 [mm]: ")) * float(10 ** -3)
a2 = float(input("Wartość otuliny a2 [mm]: ")) * float(10 ** -3)
h = float(input("Wysokość przekroju [cm]: ")) * float(10 ** -2)
b = float(input("Szerokość przekroju [cm]: ")) * float(10 ** -2)

d = h - a1  # trzeba zaokrąglić  do 3 liczy po przecinku, ale tez jeszcze nie wiem jak

print(str(d) + "  <- Wysokość użyteczna przekroju [m]")

# Obliczanie mimośrodów

M_ed = float(input("Wielkość momentu w przekroju: "))
N_ed = float(input("Wielkość siły normalnej w przekroju: "))

e = abs(M_ed / N_ed)

e_s1: float = float(e + 0.5 * h - a1)
e_s2 = float(e - 0.5 * h + a2)

print(e_s1)

# Rozpoczęcie obliczeń


x_lim = (Epsilon_cu3 * d) / (Epsilon_cu3 + fyd / Es)

Epsilon_yd = float(fyd / Es)

x_min_minus_yd = (Epsilon_cu3 * a2) / (Epsilon_cu3 + fyd / Es)
x_min_yd = (Epsilon_cu3 * a2) / (Epsilon_cu3 - fyd / Es)
x_0 = (1 - Epsilon_c3 / Epsilon_cu3) * h
x_max_yd = (Epsilon_yd * x_0 - Epsilon_c3 * a2) / (Epsilon_yd + Epsilon_c3)

print(x_lim)

x = float(1) / lambda1 * N_ed * 10 ** -3 / (eta1 * fcd * b)

print(x)

# Pierwszy  warunek

if x <= x_lim:
    sigma_s1 = fyd

    if x < x_min_yd:
        A = lambda1 * (fyd - Epsilon_cu3 * Es)
        B = -2 * (fyd * d - Epsilon_cu3 * Es * a2 * (1 + 0.5 * lambda1))
        C = 2 * ((N_ed * 10 ** -3 * (fyd * e_s1 - Epsilon_cu3 * Es * e_s2) / (lambda1 * eta1 * fcd * b)) - (
                Epsilon_cu3 * Es * a2 ** 2))
        D = ((2 * N_ed * 10 ** -3 * Epsilon_cu3 * Es * a2 * e_s2) / (lambda1 * eta1 * fcd * b))

        print(A)
        print(B)
        print(C)
        print(D)

        solution = [A, B, C, D]
        np.roots(solution)

        print(min([n for n in np.roots(solution) if n > 0]))
        x = min([n for n in np.roots(solution) if n > 0])

        if x <= x_min_minus_yd:
            sigma_s2 = -fyd

            x = 1 / (2 * lambda1) * ((d + a2) - np.sqrt((d + a2) ** 2 - (4 * N_ed * (e_s1 + e_s2)) / (eta1 * fcd * b)))
        else:
            sigma_s2 = Epsilon_cu3 * (x - a2) / x * Es


    else:
        sigma_s2 = fyd


else:
    sigma_s2 = fyd
    sigma_s1 = fyd


print(sigma_s2)

As_1 = (N_ed * 10 ** -3 * e_s2 + eta1 * fcd * b * lambda1 * x * (0.5 * lambda1 * x - a2)) / (sigma_s1 * (d - a2))*10**4 #10^4 - konwersja z m2 na cm2
print(str(As_1) + " [cm^2]")

As_2 = (N_ed * 10 ** -3 * e_s1 - eta1 * fcd * b * lambda1 * x * (d - 0.5 * lambda1 * x)) / (sigma_s2 * (d - a2))*10**4
print(str(As_2) + " [cm^2]")
