# coding=utf-8
# based on http://www.se.put.poznan.pl/zkz/pracownicy/jacekscigallo/projekty/EC2_8.pdf
from slupy.slupy_functions import *


def main(h, b, a1, a2, m_ed, n_ed, eta_bet, lambda_bet, f_cd):
    epsilon_cu3 = const_parameters[0]
    epsilon_c3 = const_parameters[1]
    f_yd = const_parameters[2]
    es = const_parameters[3]

    # dimensions
    if m_ed == 0:
        m_ed = 0.01

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
    print(f"x_min_yd {x_min_yd}")
    print(f"x_lim {x_lim}")

    x = x_lim
    sigma_s2 = epsilon_cu3 * (x - a2) / x * es
    if sigma_s2 > f_yd:
        sigma_s2 = f_yd
        print(f'sigma_s2 {sigma_s2}')

    as2 = (n_ed * 10 ** -3 * e_s1 - eta_bet * f_cd * b * lambda_bet * x * (d - 0.5 * lambda_bet * x)) / (
            sigma_s2 * (d - a2))
    print(f'as2 {as2}')

    as_min = round(max((0.10 * n_ed * 10 ** -3) / f_yd, (0.002 * b * 10 ** 2 * h * 10 ** 2) * 10 ** -4),
                   6)  # TODO to slupy_functions

    as2_min = 0.5 * as_min
    print(f'as2_min = {as2_min}')

    if as2 < as2_min:
        as2 = as2_min

        x = 1 / lambda_bet * (d - np.sqrt(
            d ** 2 - (2 * (n_ed * 10 ** -3 * e_s1 - sigma_s2 * as2 ** (d - a2))) / (eta_bet * f_cd * b)))
        print(f'x = {x}')

        if x < x_min_yd:
            ms2 = round(epsilon_cu3 * es * as2_min * (d - a2), 6)
            print(f'ms2 = {ms2}')

            A = round(-2 * d / lambda_bet, 6)
            B = round((2 * (n_ed * 10 ** -3 * e_s1 - ms2)) / (lambda_bet ** 2 * eta_bet * f_cd * b), 6)
            C = round((2 * a2 * ms2) / (lambda_bet ** 2 * eta_bet * f_cd * b), 6)

            print(f"A = {A}")
            print(f"B = {B}")
            print(f"C = {C}")

            result = x_solution(1, A, B, C)
            print(result)
            x = x_func_sol_g(result, 0)
            print(f'x = {x}')

            if x <= x_min_minus_yd:
                sigma_s2 = -f_yd
                print(f'sigma_s2 {sigma_s2}')

                x = 1 / lambda_bet * (d - np.sqrt(
                    d ** 2 - (2 * (n_ed * 10 ** -3 * e_s1 + f_yd * as2 * (d - a2))) / (eta_bet * f_cd * b)))
                print(f'x {x}')

                if x <= 0:
                    x = 0
                    print(f'x = {x}')
                    as1 = (n_ed * 10 ** -3 * e_s2) / (f_yd * (d - a2)) * 10 ** 4
                    as2 = (n_ed * 10 ** -3 * e_s1) / (-f_yd * (d - a2)) * 10 ** 4

                    print(as1)
                    print(as2)
                    return as1, as2

            else:
                sigma_s2 = epsilon_cu3 * (x - a2) / x * es
                print(f'sigma_s2 {sigma_s2}')

        else:
            sigma_s2 = f_yd
            print(f'sigma_s2 {sigma_s2}')

    else:
        as1 = (sigma_s2 * as2 + eta_bet * f_cd * b * lambda_bet * x + n_ed * 10 ** -3) / f_yd * 10 ** 4
        as2 = as2 * 10 ** 4

        print(as1)
        print(as2)
        return as1, as2

    as1 = (sigma_s2 * as2 + eta_bet * f_cd * b * lambda_bet * x + n_ed * 10 ** -3) / f_yd * 10 ** 4
    as2 = as2 * 10 ** 4

    print(as1)
    print(as2)
    return as1, as2
