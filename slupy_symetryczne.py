# coding=utf-8
# http://www.se.put.poznan.pl/zkz/pracownicy/jacekscigallo/projekty/EC2_6.pdf
from slupy_functions import *


def main(h, b, a1, a2, m_ed, n_ed, eta_bet, lambda_bet, f_cd):
    print("Projektowanie zbrojenia symetrycznego\n")  # symmetrical reinforcment

    # to do: add table with concrete strengh, to choose which we wan-t to use, yet idk how

    epsilon_cu3 = const_parameters[0]
    epsilon_c3 = const_parameters[1]
    f_yd = const_parameters[2]
    es = const_parameters[3]

    # dimensions

    print(h)
    print(b)
    print(a1)
    print(a2)
    print(m_ed)
    print(n_ed)
    print(lambda_bet)
    print(eta_bet)
    print(f_cd)

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

    x = round(1 / lambda_bet * n_ed * 10 ** -3 / (eta_bet * f_cd * b), 4)

    print(f"x {x}")

    if x <= x_lim:
        sigma_s1 = f_yd

        if x < x_min_yd:
            A = round(lambda_bet * (f_yd - epsilon_cu3 * es), 4)
            B = round(-2 * (f_yd * d - epsilon_cu3 * es * a2 * (1 + 0.5 * lambda_bet)), 4)
            C = round(
                2 * (((n_ed * 10 ** -3 * (f_yd * e_s1 - epsilon_cu3 * es * e_s2)) / (lambda_bet * eta_bet * f_cd * b))
                     - (epsilon_cu3 * es * a2 ** 2)), 4)
            D = round(((2 * n_ed * 10 ** -3 * epsilon_cu3 * es * a2 * e_s2) / (lambda_bet * eta_bet * f_cd * b)), 4)

            print(f"A = {A}")
            print(f"B = {B}")
            print(f"C = {C}")
            print(f"D = {D}")

            x, result = x_solution(A, B, C, D)
            print(f"x {x}")
            print(result)

            if x <= x_min_minus_yd:
                sigma_s2 = -f_yd

                x = round(1 / (2 * lambda_bet) * (
                        (d + a2) - np.sqrt((d + a2) ** 2 -
                                           (4 * n_ed * 10 ** -3 * (e_s1 + e_s2)) / (eta_bet * f_cd * b))), 4)

                print(f"x {x}")
            else:
                sigma_s2 = round(epsilon_cu3 * (x - a2) / x * es, 4)

        else:
            sigma_s2 = f_yd

    else:
        sigma_s2 = f_yd
        A = round(lambda_bet * (f_yd + epsilon_cu3 * es), 4)
        B = round(-2 * (f_yd * a2 + epsilon_cu3 * es * d * (1 + 0.5 * lambda_bet)), 4)
        C = round(2 * ((n_ed * 10 ** -3 * (f_yd * e_s2 + epsilon_cu3 * es * e_s1) / (lambda_bet * eta_bet * f_cd * b)) -
                       (epsilon_cu3 * es * d ** 2)), 4)
        D = round(-((2 * n_ed * 10 ** -3 * epsilon_cu3 * es * d * e_s1) / (lambda_bet * eta_bet * f_cd * b)), 4)
        print(f"A = {A}")
        print(f"B = {B}")
        print(f"C = {C}")
        print(f"D = {D}")

        x, result = x_solution(A, B, C, D)
        print(result)
        print(f"x {x}")

        if x > h:
            A = round(lambda_bet * (f_yd + epsilon_c3 * es), 4)
            B = round(-2 * (f_yd * (a2 + 0.5 * lambda_bet * x_0) + epsilon_c3 * es * d * (1 + 0.5 * lambda_bet)), 4)
            C = round(2 * ((n_ed * 10 ** -3 * (f_yd * e_s2 + epsilon_c3 * es * e_s1)) / (
                    lambda_bet * eta_bet * f_cd * b) + epsilon_c3 * es * d ** 2 + f_yd * a2 * x_0), 4)
            D = round(-((2 * n_ed * 10 ** -3) / (lambda_bet * eta_bet * f_cd * b) *
                        (epsilon_c3 * es * d * e_s1 + f_yd * x_0 * e_s2)), 4)

            print(f"A = {A}")
            print(f"B = {B}")
            print(f"C = {C}")
            print(f"D = {D}")

            x, result = x_solution(A, B, C, D)
            print(result)
            print(f"x {x}")

            if x > h / lambda_bet:
                F1 = round(n_ed * 10 ** -3 * e_s1 - eta_bet * f_cd * b * h * (0.5 * h - a1), 4)
                F2 = round(n_ed * 10 ** -3 * e_s2 - eta_bet * f_cd * b * h * (0.5 * h - a2), 4)

                x = round((epsilon_c3 * es * d * F1 + f_yd * x_0 * F2) / (epsilon_c3 * es * F1 + f_yd * F2), 4)
                print(f"x {x}")

                if h / lambda_bet <= x <= x_max_yd:
                    sigma_s1 = round(epsilon_c3 * (d - x) / (x - x_0) * es, 4)

                else:
                    F1 = round(n_ed * 10 ** -3 * (e_s1 * d + e_s2 * a2) + eta_bet * f_cd * b * h * 0.5 * (
                            (a1 - a2) * (d + a2) - (d - a2) ** 2), 4)
                    F2 = round(n_ed * 10 ** -3 * (e_s1 + e_s2) + eta_bet * f_cd * b * h * (a1 - a2), 4)

                    x = round(F1 / F2, 4)
                    print(f"x {x}")

                    sigma_s1 = round(epsilon_c3 * (d - x) / (x - x_0) * es, 4)
                    sigma_s2 = round(epsilon_c3 * (x - a2) / (x - x_0) * es, 4)

            else:
                sigma_s1 = round(epsilon_c3 * (d - x) / (x - x_0) * es, 4)

            if x <= h / lambda_bet:
                x = x
                print(f"x {x}")
            else:
                x = h / lambda_bet
                print(f"x {x}")

        else:
            sigma_s1 = round(epsilon_cu3 * (d - x) / x * es, 4)

    print(f"Sigma s1 = {sigma_s1}")
    print(f"Sigma s2 = {sigma_s2}")

    as_1 = round((n_ed * 10 ** -3 * e_s2 + eta_bet * f_cd * b * lambda_bet * x * (0.5 * lambda_bet * x - a2)) / (
            sigma_s1 * (d - a2)) * 10 ** 4, 4)  # 10^4 - converion z m2 na cm2
    print(as_1)
    as_1 = np.real(as_1)
    print(f"As1 = {as_1} [cm^2]")

    as_2 = np.real(round((n_ed * 10 ** -3 * e_s1 - eta_bet * f_cd * b * lambda_bet * x * (d - 0.5 * lambda_bet * x)) / (
            sigma_s2 * (d - a2)) * 10 ** 4, 4))
    print(as_2)
    as_1 = np.real(as_2)
    print(f"As2 = {as_2} [cm^2]")  # As1 & As2 should be similar
    return as_1, as_2
