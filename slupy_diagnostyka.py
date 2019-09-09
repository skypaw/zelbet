# coding=utf-8
# http://www.se.put.poznan.pl/zkz/pracownicy/jacekscigallo/projekty/EC2_7.pdf


from slupy_functions import *


def main(h, b, a1, a2, m_ed, n_ed, a_s1, a_s2):
    def abc_diagnostyka(e_s2_func, a2_func, lambda_bet_func, plus_minus_1, f_yd_func, a_s_1_2, e_s_1_2,
                        epsilon_cu3_func,
                        es_func, a_s_2_1, e_s_2_1, eta_bet_func, f_cd_func, b_func, a2_d):  # 2_1 when x < xlim
        a_function = (2 * (e_s2_func - a2_func)) / lambda_bet_func
        b_function = (plus_minus_1 * 2 * (
                f_yd_func * a_s_1_2 * e_s_1_2 + plus_minus_1 * epsilon_cu3_func * es_func * a_s_2_1 * e_s_2_1)) / (
                             lambda_bet_func ** 2 * eta_bet_func * f_cd_func * b_func)
        c_function = (-2 * epsilon_cu3_func * es_func * a_s_2_1 * e_s_2_1 * a2_d) / (
                lambda_bet_func ** 2 * eta_bet_func * f_cd_func * b_func)

        return a_function, b_function, c_function

    def sigma(epsilon_cu3_func, d_func, x_func, es_func, f_yd_func, a2_func):
        sigma_s1_func = epsilon_cu3_func * (d_func - x_func) / x_func * es_func

        if sigma_s1_func >= f_yd_func:
            sigma_s1_func = f_yd_func

        sigma_s2_func = epsilon_cu3_func * (x_func - a2_func) / x_func * es_func

        if sigma_s2_func <= -f_yd_func:
            sigma_s2_func = -f_yd_func

        if sigma_s2_func >= f_yd_func:
            sigma_s2_func = f_yd_func

        return sigma_s1_func, sigma_s2_func

    def sigma_2(epsilon_c3_func, d_func, x_func, es_func, f_yd_func, a2_func, x_0_func):
        sigma_s1_func = epsilon_c3_func * (d_func - x_func) / (x_func - x_0_func) * es_func
        if sigma_s1_func <= -f_yd_func:
            sigma_s1_func = -f_yd_func

        sigma_s2_func = epsilon_c3_func * (x_func - a2_func) / (x_func - x_0_func) * es_func
        if sigma_s2_func >= f_yd_func:
            sigma_s2_func = f_yd_func

        return sigma_s1_func, sigma_s2_func

    print("Projektowanie zbrojenia symetrycznego\n")  # symmetrical reinforcment

    # to do: add table with concrete strengh, to choose which we wan-t to use, yet idk how

    lambda_bet = float(0.8)  # not a const, basicallv it deepends of kind of concrete
    eta_bet = float(1)  # like line above
    f_cd = float(18)  # const concrete C25/30

    # const

    epsilon_cu3 = const_parameters[0]
    epsilon_c3 = const_parameters[1]
    f_yd = const_parameters[2]
    es = const_parameters[3]

    print(f"Obliczeniowa granica plastyczności stali {f_yd} [MPa]")
    print(f"Moduł Younga {es} [MPa]")

    # calculations

    x_lim, epsilon_yd, x_min_minus_yd, x_min_yd, x_0, x_max_yd, d = start_parameters(epsilon_cu3, epsilon_c3,
                                                                                     f_yd, es, a2, a1, h)

    print(f"Wysokość użyteczna przekroju [m] {d}")
    print(f"x_lim {x_lim}")
    print(f"x_min_minus_yd {x_min_minus_yd}")
    print(f"x_min_yd {x_min_yd}")
    print(f"x_0 {x_0}")
    print(f"x_max_yd {x_max_yd}")

    # eccentricity min

    emin = (epsilon_c3 * es * (a_s2 * (0.5 * h - a2) - a_s1 * (0.5 * h - a1))) / (
            eta_bet * f_cd * b * h + epsilon_c3 * es * (a_s1 + a_s2))

    # eccentricity

    e, e_s1, e_s2 = eccentricity(m_ed, n_ed, h, a1, a2)

    if e <= emin:
        a_s1_1 = a_s1
        a_s2_1 = a_s2
        a_s1 = a_s2_1
        a_s2 = a_s1_1

    print(f"Mimośród e = {e} [m]")
    print(f"Mimośród e_s1 = {e_s1} [m]")
    print(f"Mimośród e_s2 = {e_s2} [m]")

    x = 1 / lambda_bet * (-(e_s2 - a2) + np.sqrt(
        (e_s2 - a2) ** 2 + (2 * f_yd * (a_s1 * e_s1 - a_s2 * e_s2)) / (eta_bet * f_cd * b)))
    print(f"x {x}")

    if x <= x_lim:
        if x < x_min_yd:
            A, B, C = abc_diagnostyka(e_s2, a2, lambda_bet, -1, f_yd, a_s1, e_s1, epsilon_cu3, es, a_s2, e_s2, eta_bet,
                                      f_cd, b, a2)
            print(f"A {A}")
            print(f"B {B}")
            print(f"C {C}")

            x, results = x_solution(1, A, B, C)

            print(f"x = {x}")
            print(f"results = {results}")

            if x <= x_min_minus_yd:
                x = 1 / lambda_bet * (
                        -(e_s2 - a2) + np.sqrt((e_s2 - a2) ** 2 + (2 * f_yd * (a_s1 * e_s1 + a_s2 * e_s2)) / (
                        eta_bet * f_cd * b)))  # this and line 77 to function, difference with one minus  - between as1 and as2

        sigma_s1, sigma_s2 = sigma(epsilon_cu3, d, x, es, f_yd, a2)

        print(f"sigma_s1 {sigma_s1}")
        print(f"sigma_s2 {sigma_s2}")

    else:
        A, B, C = abc_diagnostyka(e_s2, a2, lambda_bet, 1, f_yd, a_s2, e_s2, epsilon_cu3, es, a_s1, e_s1, eta_bet, f_cd,
                                  b,
                                  d)
        print(f"A {A}")
        print(f"B {B}")
        print(f"C {C}")

        x, results = x_solution(1, A, B, C)

        print(f"x = {x}")
        print(f"results = {results}")

        if x > h:
            A = -x_0 + (2 * (e_s2 - a2)) / lambda_bet
            B = 2 * ((f_yd * a_s2 * e_s2 + epsilon_c3 * es * a_s1 * e_s1) / (lambda_bet ** 2 * eta_bet * f_cd * b) - (
                    e_s2 - a2) / lambda_bet * x_0)
            C = (-2 * (f_yd * a_s2 * e_s2 * x_0 + epsilon_c3 * es * a_s1 * e_s1 * d)) / (
                    lambda_bet ** 2 * eta_bet * f_cd * b)

            print(f"A {A}")
            print(f"B {B}")
            print(f"C {C}")

            x, results = x_solution(1, A, B, C)

            print(f"results = {results}")
            print(f"x = {x}")

            if x > h / lambda_bet:
                x = (eta_bet * f_cd * b * h * e * x_0 + epsilon_c3 * es * (a_s1 * e_s1 * d + a_s2 * e_s2 * a2)) / (
                        eta_bet * f_cd * b * h * e + epsilon_c3 + es * (a_s1 * e_s1 + a_s2 * e_s2))

                if x <= x_max_yd:
                    x = ((
                                 eta_bet * f_cd * b * h * e + f_yd * e_s2 * a_s2) * x_0 + epsilon_c3 * es * a_s1 * e_s1 * d) / (
                                eta_bet * f_cd * b * h * e + f_yd * a_s2 * e_s2 + epsilon_c3 * es * a_s1 * e_s1)
                    sigma_s1, sigma_s2 = sigma_2(epsilon_c3, d, x, es, f_yd, a2, x_0)
                    print(f"sigma_s1 {sigma_s1}")
                    print(f"sigma_s2 {sigma_s2}")
                else:

                    sigma_s1, sigma_s2 = sigma_2(epsilon_c3, d, x, es, f_yd, a2, x_0)
                    print(f"sigma_s1 {sigma_s1}")
                    print(f"sigma_s2 {sigma_s2}")

            else:
                sigma_s1, sigma_s2 = sigma_2(epsilon_c3, d, x, es, f_yd, a2, x_0)
                print(f"sigma_s1 {sigma_s1}")
                print(f"sigma_s2 {sigma_s2}")

        else:
            sigma_s1, sigma_s2 = sigma(epsilon_cu3, d, x, es, f_yd, a2)

            print(f"sigma_s1 {sigma_s1}")
            print(f"sigma_s2 {sigma_s2}")

        if x <= h / lambda_bet:
            x = x
        else:
            x = h / lambda_bet

    # final countings

    print(f"N_ed = {n_ed}")
    print(f"M_ed = {m_ed}")

    print(x)
    print(d)

    n_rd = (eta_bet * f_cd * b * lambda_bet * x - sigma_s1 * a_s1 + sigma_s2 * a_s2) * 10 ** 3
    m_rd = (eta_bet * f_cd * b * lambda_bet * x * (d - 0.5 * lambda_bet * x) + sigma_s2 * a_s2 * (
            d - a2) - n_ed * 10 ** -3 * (
                    0.5 * h - a1)) * 10 ** 3

    print(f"N_rd = {n_rd}")
    print(f"M_rd = {m_rd}")
    return m_rd, n_rd
