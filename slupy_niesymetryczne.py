# coding=utf-8
# based on http://www.se.put.poznan.pl/zkz/pracownicy/jacekscigallo/projekty/EC2_5.pdf
from slupy_functions import *


def main(h, b, a1, a2, m_ed, n_ed, eta_bet, lambda_bet, f_cd):
    def x_niesymetryczny(lambda_bet_func, d_func, n_ed_func, e_s1_func, sigma_s2_func, as2_func, a2_func, eta_bet_func,
                         f_cd_func, b_func):
        x_func = round(1 / lambda_bet_func * (d_func - np.sqrt(
            d_func ** 2 - (2 * (n_ed_func * 10 ** -3 * e_s1_func - sigma_s2_func * as2_func * (d_func - a2_func))) /
            (eta_bet_func * f_cd_func * b_func))), 4)

        return x_func

    def sigma_func(epsilon_cu3_func, es_func, x_func, a2_func):
        sigma_s2_func = (epsilon_cu3_func * es_func) * (x_func - a2_func) / x_func
        return sigma_s2_func

    def abc_func(a2_d_func, a2_d_func_rev, lambda_bet_func, n_ed_func, es_func, m_s_function, eta_bet_func, f_cd_func,
                 b_func):
        a_function = -2 * a2_d_func / lambda_bet_func
        b_function = (2 * (n_ed_func * 10 ** -3 * es_func + m_s_function)) / (
                lambda_bet_func ** 2 * eta_bet_func * f_cd_func * b_func)
        c_function = (-2 * a2_d_func_rev * m_s_function) / (lambda_bet_func ** 2 * eta_bet_func * f_cd_func * b_func)
        return a_function, b_function, c_function

    def m_s_func(e_cu_cu3, es_func, as_1_2_min, d_func, a2_func):
        m_s = e_cu_cu3 * es_func * as_1_2_min * (d_func - a2_func)
        return m_s

    print("Projektowanie zbrojenia symetrycznego\n")  # asymmetrical reinforcement

    epsilon_cu3 = const_parameters[0]
    epsilon_c3 = const_parameters[1]
    f_yd = const_parameters[2]
    es = const_parameters[3]

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

    # eccentricity
    e, e_s1, e_s2 = eccentricity(m_ed, n_ed, h, a1, a2)

    print(f"Mimośród e = {e} [m]")
    print(f"Mimośród e_s1 = {e_s1} [m]")
    print(f"Mimośród e_s2 = {e_s2} [m]")

    # calculations

    x_lim, epsilon_yd, x_min_minus_yd, x_min_yd, x_0, x_max_yd, d = start_parameters(epsilon_cu3, epsilon_c3,
                                                                                     f_yd, es, a2, a1, h)

    print(f"Wysokość użyteczna przekroju [m] {d}")
    print(f"x_lim {x_lim}")
    print(f"x_min_minus_yd {x_min_minus_yd}")
    print(f"x_min_yd {x_min_yd}")
    print(f"x_0 {x_0}")
    print(f"x_max_yd {x_max_yd}")

    x = x_lim
    sigma_s2 = sigma_func(epsilon_cu3, es, x, a2)

    if sigma_s2 <= f_yd:
        sigma_s2 = sigma_s2
    else:
        sigma_s2 = f_yd

    as2 = (n_ed * 10 ** -3 * e_s1 - eta_bet * f_cd * b * lambda_bet * x * (d - 0.5 * lambda_bet * x)) / (
            sigma_s2 * (d - a2))

    as_min = round(max((0.10 * n_ed * 10 ** -3) / f_yd, (0.002 * b * 10 ** 2 * h * 10 ** 2) * 10 ** -4), 8)

    as2_min = 0.5 * as_min
    as1_min = 0.5 * as_min

    print(f"as2 = {as2}")
    print(f"as_min{as_min}")
    print(f"x {x}")
    print(f"sigma_s2 {sigma_s2}")

    if as2 <= as2_min:
        as2 = as2_min
        x = x_niesymetryczny(lambda_bet, d, n_ed, e_s1, sigma_s2, as2, a2, eta_bet, f_cd, b)

        if x < x_min_yd:
            m_s2 = m_s_func(epsilon_cu3, es, as2_min, d, a2)
            print(m_s2)

            A, B, C = abc_func(d, a2, lambda_bet, n_ed, e_s1, -m_s2, eta_bet, f_cd, b)
            print(A)
            print(B)
            print(C)

            result = x_solution(1, A, B, C)
            print(result)

            x = x_func_sol_g(result, 0)

            if x <= x_min_minus_yd:
                sigma_s2 = -f_yd
                x = x_niesymetryczny(lambda_bet, d, n_ed, e_s1, sigma_s2, as2, a2, eta_bet, f_cd, b)
            else:
                sigma_s2 = sigma_func(epsilon_cu3, es, x, a2)

        else:
            sigma_s2 = f_yd

        as1 = (sigma_s2 * as2 + eta_bet * f_cd * b * lambda_bet * x - n_ed * 10 ** -3) / f_yd * 10 ** 4
        as2 = as2 * 10 ** 4

        print(f"As1 = {as1}")
        print(f"As2 = {as2}")
        return as1, as2

    else:
        as1 = (sigma_s2 * as2 + eta_bet * f_cd * b * lambda_bet * x - n_ed * 10 ** -3) / f_yd
        if as1 < 0:
            as1 = as1_min
            m_s1 = m_s_func(epsilon_cu3, es, as1, d, a2)
            print(f"m_s1 {m_s1}")

            A, B, C = abc_func(a2, d, lambda_bet, n_ed, e_s2, m_s1, eta_bet, f_cd, b)
            print(A)
            print(B)
            print(C)

            result = x_solution(1, A, B, C)
            print(result)
            x = x_func_sol_g(result, x_lim)

            if x > h:
                m_s2 = m_s_func(epsilon_c3, es, as1, d, a2)
                print(f"ms2 {m_s2}")

                A = -(x_0 + (2 * a2) / lambda_bet)
                B = 2 * ((n_ed * 10 ** -3 * e_s2 + m_s2) / (lambda_bet ** 2 * eta_bet * f_cd * b) + (
                        (a2 / lambda_bet) * x_0))
                C = (-2 * (n_ed * 10 ** -3 * e_s2 * x_0 + d * m_s2)) / (lambda_bet ** 2 * eta_bet * f_cd * b)

                print(f"A {A}")
                print(f"B {B}")
                print(f"C {C}")

                result = x_solution(1, A, B, C)
                print(result)

                x = x_func_sol_g(result, h)
                print(f"x={x}")

                if x > (h / lambda_bet):
                    f1 = (-n_ed * 10 ** -3 * e_s2 - eta_bet * f_cd * b * h * (0.5 * h - a2)) * (
                            d - x_0)
                    f2 = (n_ed * 10 ** -3 * e_s1 - eta_bet * f_cd * b * h * (0.5 * h - a1)) * (x_0 - a2)
                    print(f"f1={f1}")
                    print(f"f2={f2}")

                    if f2 - f1 > 0:
                        x = (-f1 * a2 + f2 * d + np.sqrt(f1 * f2) * (d - a2)) / (f2 - f1)
                        print(f"x={x}")
                        if x >= x_max_yd:
                            x = x
                            print(f"x={x}")
                        else:
                            x = x_max_yd
                            print(f"x={x}")

                        sigma_s1 = epsilon_c3 * (d - x) / (x - x_0) * es
                        if sigma_s1 <= f_yd:
                            sigma_s1 = sigma_s1
                        else:
                            sigma_s1 = f_yd

                        sigma_s2 = epsilon_c3 * (x - a2) / (x - x_0) * es
                        if sigma_s2 <= f_yd:
                            sigma_s2 = sigma_s2
                        else:
                            sigma_s2 = f_yd

                        as1 = (n_ed * 10 ** -3 * e_s2 + eta_bet * f_cd * b * h * (0.5 * h - a2)) /(sigma_s1 * (d - a2)) * 10 ** 4
                        as2 = (n_ed * 10 ** -3 * e_s1 - eta_bet * f_cd * b * h * (0.5 * h - a1)) /(sigma_s2 * (d - a2)) * 10 ** 4

                        print(f"As1 = {as1}")
                        print(f"As2 = {as2}")
                        return as1, as2

                    else:
                        x = 10 ** 10

                        sigma_s1 = epsilon_c3 * (d - x) / (x - x_0) * es
                        if sigma_s1 <= f_yd:
                            sigma_s1 = sigma_s1
                        else:
                            sigma_s1 = f_yd

                        sigma_s2 = epsilon_c3 * (x - a2) / (x - x_0) * es
                        if sigma_s2 <= f_yd:
                            sigma_s2 = sigma_s2
                        else:
                            sigma_s2 = f_yd

                        as1 = (n_ed * 10 ** -3 * e_s2 + eta_bet * f_cd * b * h * (0.5 * h - a2)) / (
                                sigma_s1 * (d - a2)) * 10 ** 4
                        as2 = (n_ed * 10 ** -3 * e_s1 + eta_bet * f_cd * b * h * (0.5 * h - a1)) / (
                                sigma_s2 * (d - a2)) * 10 ** 4
                        print(f"As1 = {as1}")
                        print(f"As2 = {as2}")
                        return as1, as2

                else:
                    as2 = (n_ed * 10 ** -3 * e_s1 - eta_bet * f_cd * b * lambda_bet * x * (
                            d - 0.5 * lambda_bet * x)) / (
                                  f_yd * (d - a2)) * 10 ** 4
                    as1 = as1 * 10 ** 4
            else:
                as2 = (n_ed * 10 ** -3 * e_s1 - eta_bet * f_cd * b * lambda_bet * x * (d - 0.5 * lambda_bet * x)) / (
                        f_yd * (d - a2)) * 10 ** 4
                as1 = as1 * 10 ** 4
        else:
            as1 = as1 * 10 ** 4
            as2 = as2 * 10 ** 4

    print(f"As1 = {as1}")
    print(f"As2 = {as2}")
    return as1, as2


h = 0.6
b = 0.3
a1 = 0.05
a2 = 0.05
eta_bet = 1.0
lambda_bet = 0.8
f_cd = 21.43
f_ctm = 2.9

m_ed = 10
n_ed = 5

main(h, b, a1, a2, m_ed, n_ed, eta_bet, lambda_bet, f_cd)
