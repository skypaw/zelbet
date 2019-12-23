# coding=utf-8
# based on http://www.se.put.poznan.pl/zkz/pracownicy/jacekscigallo/projekty/EC2_10.pdf


from uls.global_functions import *


def main(h, b, a1, a2, m_ed, n_ed_minus, a_s1, a_s2, eta_bet, lambda_bet, f_cd):
    epsilon_cu3 = const_parameters[0]
    epsilon_c3 = const_parameters[1]
    f_yd = const_parameters[2]
    es = const_parameters[3]

    if m_ed == 0:
        m_ed = 0.01

    n_ed = abs(n_ed_minus)

    x_lim, epsilon_yd, x_min_minus_yd, x_min_yd, x_0, x_max_yd, d = start_parameters(epsilon_cu3, epsilon_c3,
                                                                                     f_yd, es, a2, a1, h)

    print(f"Wysokość użyteczna przekroju [m] {d}")
    print(f"x_lim {x_lim}")
    print(f"x_min_minus_yd {x_min_minus_yd}")
    print(f"x_min_yd {x_min_yd}")
    print(f"x_0 {x_0}")
    print(f"x_max_yd {x_max_yd}")

    # eccentricity min

    emin = (a_s1 * (0.5 * h - a1) - a_s2 * (0.5 * h - a2)) / (a_s1 + a_s2)

    print(h)
    print(b)
    print(a1)
    print(a2)
    print(m_ed)
    print(n_ed)
    print(lambda_bet)
    print(eta_bet)
    print(f_cd)
    print(f"e_min = {emin}")

    # eccentricity
    e, e_s1, e_s2 = eccentricity_extension(m_ed, n_ed, h, a1, a2)

    print(f"e = {e}")

    if e < emin:
        a_s1_1 = a_s1
        a_s2_1 = a_s2
        a_s1 = a_s2_1
        a_s2 = a_s1_1

    print(f"a_s1 {a_s1}")
    print(f"a_s2 {a_s2}")

    x = 1 / lambda_bet * ((e_s2 + a2) - np.sqrt(
        (e_s2 + a2) ** 2 - (2 * f_yd * (a_s1 * e_s1 - a_s2 * e_s2)) / (eta_bet * f_cd * b)))

    print(f'x = {x}')

    if x < x_min_yd:
        A = (-2 * (e_s2 + a2)) / lambda_bet
        B = (2 * (a_s1 * f_yd * e_s1 - a_s2 * epsilon_cu3 * es * e_s2)) / (
                lambda_bet ** 2 * eta_bet * f_cd * b)
        C = (2 * a_s2 * epsilon_cu3 * es * e_s2 * a2) / (lambda_bet ** 2 * eta_bet * f_cd * b)

        result = x_solution(1, A, B, C)
        print(result)
        x = x_func_sol_g(result, 0)
        print(f'x = {x}')

        if x < x_min_minus_yd:
            x = 1 / lambda_bet * ((e_s2 + a2) - np.sqrt(
                (e_s2 + a2) ** 2 - (2 * f_yd * (a_s1 * e_s1 + a_s2 * e_s2)) / (
                        eta_bet * f_cd * b)))
            print(f'x = {x}')

    if x > 0:
        sigma_s1 = epsilon_cu3 * (d - x) / x * es
        print(sigma_s1)

        if sigma_s1 > f_yd:
            sigma_s1 = f_yd

        sigma_s2 = epsilon_cu3 * (x - a2) / x * es
        print(sigma_s2)
        if sigma_s2 > f_yd:
            sigma_s2 = f_yd

        if sigma_s2 < -f_yd:
            sigma_s2 = -f_yd

    else:
        x = 0
        sigma_s1 = f_yd
        sigma_s2 = -f_yd

    print(sigma_s1)
    print(sigma_s2)

    n_rd = (-eta_bet * f_cd * b * lambda_bet * x + sigma_s1 * a_s1 - sigma_s2 * a_s2) * 10 ** 3
    m_rd = (eta_bet * f_cd * b * lambda_bet * x * (d - 0.5 * lambda_bet * x) + sigma_s2 * a_s2 * (
                d - a2) + n_ed * 10 ** -3 * (0.5 * h - a1)) * 10 ** 3

    print(n_rd)
    print(m_rd)
    return n_rd, m_rd
