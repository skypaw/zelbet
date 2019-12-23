# coding=utf-8
# based on http://www.se.put.poznan.pl/zkz/pracownicy/jacekscigallo/projekty/EC2_9.pdf
from slupy.global_functions import *
import numpy as np


def main(h, b, a1, a2, m_ed, n_ed_minus, eta_bet, lambda_bet, f_cd):
    print("Projektowanie zbrojenia symetrycznego\n")  # symmetrical reinforcment

    epsilon_cu3 = const_parameters[0]
    epsilon_c3 = const_parameters[1]
    f_yd = const_parameters[2]
    es = const_parameters[3]

    # dimensions
    if m_ed == 0:
        m_ed = 0.01

    n_ed = abs(n_ed_minus)

    print(h)
    print(b)
    print(a1)
    print(a2)
    print(m_ed)
    print(n_ed)
    print(lambda_bet)
    print(eta_bet)
    print(f_cd)

    e, e_s1, e_s2 = eccentricity_extension(m_ed, n_ed, h, a1, a2)

    print(f"Mimośród e = {e} [m]")
    print(f"Mimośród e_s1 = {e_s1} [m]")
    print(f"Mimośród e_s2 = {e_s2} [m]")

    # calculations

    x_lim, epsilon_yd, x_min_minus_yd, x_min_yd, x_0, x_max_yd, d = start_parameters(epsilon_cu3, epsilon_c3,
                                                                                     f_yd, es, a2, a1, h)

    print(f"x_min_minus_yd {x_min_minus_yd}")

    sigma_s1 = f_yd
    sigma_s2 = sigma_s1

    A = lambda_bet * (f_yd - epsilon_cu3 * es)

    B = -2 * (f_yd * d - epsilon_cu3 * es * a2 * (1 + 0.5 * lambda_bet))

    C = 2 * ((n_ed * 10 ** -3 * (f_yd * e_s1 - epsilon_cu3 * es * e_s2)) / (
            lambda_bet * eta_bet * f_cd * b) - epsilon_cu3 * es * a2 ** 2)

    D = (2 * n_ed * 10 ** -3 * epsilon_cu3 * es * a2 * e_s2) / (lambda_bet * eta_bet * f_cd * b)

    print(f"A = {A}")
    print(f"B = {B}")
    print(f"C = {C}")
    print(f"D = {D}")

    result = x_solution(A, B, C, D)
    print(result)
    x = x_func_sol_g(result, 0)
    print(f'x = {x}')

    if x <= x_min_minus_yd:
        sigma_s2 = -f_yd
        print(f'sigma_s2 {sigma_s2}')

        x = 1 / (2 * lambda_bet) * (
                (d + a2) - np.sqrt((d + a2) ** 2 - (4 * n_ed * 10 ** -3 * (e_s1 + e_s2)) / (eta_bet * f_cd * b)))
        print(f'x = {x}')

        if x <= 0:
            x = 0
            print(f'x = {x}')

    else:
        sigma_s2 = epsilon_cu3 * (x - a2) / x * es
        print(f'sigma_s2 {sigma_s2}')

    as1 = np.real((n_ed * 10 ** -3 * e_s2 + eta_bet * f_cd * b * lambda_bet * x * (0.5 * lambda_bet * x - a2)) / (
            sigma_s1 * (d - a2)) * 10 ** 4)
    as2 = np.real((n_ed * 10 ** -3 * e_s1 - eta_bet * f_cd * b * lambda_bet * x * (d - 0.5 * lambda_bet * x)) / (
            sigma_s2 * (d - a2)) * 10 ** 4)

    print(f'as1 = {as1}')
    print(f'as2 = {as2}')

    return as1, as2

