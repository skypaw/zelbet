# coding=utf-8
# based on http://www.se.put.poznan.pl/zkz/pracownicy/jacekscigallo/projekty/EC2_6.pdf
from slupy.global_functions import *


def main(h, b, a1, a2, m_ed, n_ed, eta_bet, lambda_bet, f_cd):
    print("Projektowanie zbrojenia symetrycznego\n")  # symmetrical reinforcment

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

    e, e_s1, e_s2 = eccentricity(m_ed, n_ed, h, a1, a2)

    print(f"Mimośród e = {e} [m]")
    print(f"Mimośród e_s1 = {e_s1} [m]")
    print(f"Mimośród e_s2 = {e_s2} [m]")

    # calculations

    x_lim, epsilon_yd, x_min_minus_yd, x_min_yd, x_0, x_max_yd, d = start_parameters(epsilon_cu3, epsilon_c3,
                                                                                     f_yd, es, a2, a1, h)

    print(f"d = {d}")
    print(f"Wysokość użyteczna przekroju [m] {d}")
    print(f"x_lim {x_lim}")
    print(f"x_min_minus_yd {x_min_minus_yd}")
    print(f"x_min_yd {x_min_yd}")
    print(f"x_0 {x_0}")
    print(f"x_max_yd {x_max_yd}")

    x = round(1 / lambda_bet * n_ed * 10 ** -3 / (eta_bet * f_cd * b), 6)

    print(f"x {x}")

    if x <= x_lim:
        sigma_s1 = f_yd
        print("x<=x_lim YES")

        if x < x_min_yd:
            print("x<x_min_yd YES")
            A = round(lambda_bet * (f_yd - epsilon_cu3 * es), 6)
            B = round(-2 * (f_yd * d - epsilon_cu3 * es * a2 * (1 + 0.5 * lambda_bet)), 6)
            C = round(
                2 * (((n_ed * 10 ** -3 * (f_yd * e_s1 - epsilon_cu3 * es * e_s2)) / (lambda_bet * eta_bet * f_cd * b))
                     - (epsilon_cu3 * es * a2 ** 2)), 6)
            D = round(((2 * n_ed * 10 ** -3 * epsilon_cu3 * es * a2 * e_s2) / (lambda_bet * eta_bet * f_cd * b)), 6)

            print(f"A = {A}")
            print(f"B = {B}")
            print(f"C = {C}")
            print(f"D = {D}")

            result = x_solution(A, B, C, D)
            print(result)
            x = x_func_sol_g(result, 0)
            print(f'x = {x}')

            if x <= x_min_minus_yd:
                print("x<=x_min_minus_yd YES")
                sigma_s2 = -f_yd

                x = round(1 / (2 * lambda_bet) * (
                        (d + a2) - np.sqrt((d + a2) ** 2 -
                                           (4 * n_ed * 10 ** -3 * (e_s1 + e_s2)) / (eta_bet * f_cd * b))), 6)

                print(f"x {x}")
            else:
                print("x<=x_min_minus_yd NO")
                sigma_s2 = round(epsilon_cu3 * (x - a2) / x * es, 6)

        else:
            print("x<x_min_yd NO")
            sigma_s2 = f_yd

    else:
        print("x<=x_lim NO")
        sigma_s2 = f_yd
        print(sigma_s2)
        A = round(lambda_bet * (f_yd + epsilon_cu3 * es), 6)
        B = round(-2 * (f_yd * a2 + epsilon_cu3 * es * d * (1 + 0.5 * lambda_bet)), 6)
        C = round(2 * ((n_ed * 10 ** -3 * (f_yd * e_s2 + epsilon_cu3 * es * e_s1) / (lambda_bet * eta_bet * f_cd * b)) +
                       (epsilon_cu3 * es * d ** 2)), 6)
        D = round(-((2 * n_ed * 10 ** -3 * epsilon_cu3 * es * d * e_s1) / (lambda_bet * eta_bet * f_cd * b)), 6)
        print(f"A = {A}")
        print(f"B = {B}")
        print(f"C = {C}")
        print(f"D = {D}")

        result = x_solution(A, B, C, D)
        print(result)

        x = x_func_sol_g(result, x_lim)
        print(f"x {x}")

        if x > h:
            print("x>h YES")
            A = round(lambda_bet * (f_yd + epsilon_c3 * es), 6)
            B = round(-2 * (f_yd * (a2 + 0.5 * lambda_bet * x_0) + epsilon_c3 * es * d * (1 + 0.5 * lambda_bet)), 6)
            C = round(2 * ((n_ed * 10 ** -3 * (f_yd * e_s2 + epsilon_c3 * es * e_s1)) / (
                    lambda_bet * eta_bet * f_cd * b) + epsilon_c3 * es * d ** 2 + f_yd * a2 * x_0), 6)
            D = round(-((2 * n_ed * 10 ** -3) / (lambda_bet * eta_bet * f_cd * b) *
                        (epsilon_c3 * es * d * e_s1 + f_yd * x_0 * e_s2)), 6)

            print(f"A = {A}")
            print(f"B = {B}")
            print(f"C = {C}")
            print(f"D = {D}")

            result = x_solution(A, B, C, D)
            print(result)

            x = x_func_sol_g(result, h)
            print(f"x {x}")

            if x > h / lambda_bet:
                print("x>h/lambda_bet YES")
                f1 = round(n_ed * 10 ** -3 * e_s1 - eta_bet * f_cd * b * h * (0.5 * h - a1), 6)
                f2 = round(n_ed * 10 ** -3 * e_s2 + eta_bet * f_cd * b * h * (0.5 * h - a2), 6)
                print(f"f1 {f1}")
                print(f"f2 {f2}")

                x = round((epsilon_c3 * es * d * f1 + f_yd * x_0 * f2) / (epsilon_c3 * es * f1 + f_yd * f2), 6)
                print(f"x {x}")

                if h / lambda_bet <= x <= x_max_yd:
                    print("h/lambda_bet<=x<=x_max_yd YES")
                    sigma_s1 = round(epsilon_c3 * (d - x) / (x - x_0) * es, 6)

                else:
                    print("h/lambda_bet<=x<=x_max_yd NO")
                    f1 = round(n_ed * 10 ** -3 * (e_s1 * d + e_s2 * a2) + eta_bet * f_cd * b * h * 0.5 * (
                            (a1 - a2) * (d + a2) - (d - a2) ** 2), 6)
                    f2 = round(n_ed * 10 ** -3 * (e_s1 + e_s2) + eta_bet * f_cd * b * h * (a1 - a2), 6)

                    print(f"f1={f1}")
                    print(f"f2={f2}")

                    x = round(f1 / f2, 6)
                    print(f"x {x}")

                    sigma_s1 = round(epsilon_c3 * (d - x) / (x - x_0) * es, 6)
                    sigma_s2 = round(epsilon_c3 * (x - a2) / (x - x_0) * es, 6)

            else:
                print("x>h/lambda_bet NO")
                sigma_s1 = round(epsilon_c3 * (d - x) / (x - x_0) * es, 6)

            if x <= h / lambda_bet:
                print("x<=h/lambda_bet YES")
                x = x
                print(f"x {x}")
            else:
                print("x<=h/lambda_bet NO")
                x = h / lambda_bet
                print(f"x {x}")

        else:
            print("x>h NO")
            sigma_s1 = round(epsilon_cu3 * (d - x) / x * es, 6)

    print(f"Sigma s1 = {sigma_s1}")
    print(f"Sigma s2 = {sigma_s2}")

    as_1 = round((n_ed * 10 ** -3 * e_s2 + eta_bet * f_cd * b * lambda_bet * x * (0.5 * lambda_bet * x - a2)) / (
            sigma_s1 * (d - a2)) * 10 ** 4, 6)  # 10^4 - converion z m2 na cm2
    print(as_1)
    as_1 = np.real(as_1)
    print(f"As1 = {as_1} [cm^2]")

    as_2 = round((n_ed * 10 ** -3 * e_s1 - eta_bet * f_cd * b * lambda_bet * x * (d - 0.5 * lambda_bet * x)) / (
            sigma_s2 * (d - a2)) * 10 ** 4, 6)
    print(as_2)
    as_2 = np.real(as_2)
    print(f"As2 = {as_2} [cm^2]")  # As1 & As2 should be similar
    return as_1, as_2
