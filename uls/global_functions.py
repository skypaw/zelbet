# coding=utf-8

import numpy as np

const_parameters = (434.78, 200000)


def epsilon_cu_3_c3(f_ck):
    if f_ck <= 50:
        epsilon_cu_3_func = 0.0035
        epsilon_c_3_func = 0.00175
    else:
        epsilon_cu_3_func = 2.6 + 35 * (0.01 * (90 - f_ck) ** 4) * 0.001
        epsilon_c_3_func = (1.75 + 0.01375 * (f_ck - 50)) * 0.001

    return epsilon_cu_3_func, epsilon_c_3_func


def x_solution(a_func, b_func, c_func, d_func):
    solution = [a_func, b_func, c_func, d_func]

    results = [np.roots(solution)]
    res = []
    for i in results[0]:

        if i.imag == 0.0:
            res.append(i)
    return res


def x_func_sol_g(res_func, x1):  # g = greater
    x_function = round(min([n for n in res_func if n > x1]), 6)
    return x_function


def x_func_sol_ge(res_func, x1):  # ge = greater equal
    x_function = round(min([n for n in res_func if n >= x1]), 6)
    return x_function


def start_parameters(epsilon_cu3_func, epsilon_c3_func, f_yd_func, es_func, a2_func, a1_func, h_func):
    d_func = round(h_func - a1_func, 6)
    x_lim_func = round((epsilon_cu3_func * d_func) / (epsilon_cu3_func + f_yd_func / es_func), 6)
    epsilon_yd_func = float(f_yd_func / es_func)

    x_min_minus_yd_func = round((epsilon_cu3_func * a2_func) / (epsilon_cu3_func + f_yd_func / es_func), 6)
    x_min_yd_func = round((epsilon_cu3_func * a2_func) / (epsilon_cu3_func - f_yd_func / es_func), 6)
    x_0_func = round((1 - epsilon_c3_func / epsilon_cu3_func) * h_func, 6)
    x_max_yd_func = round((epsilon_yd_func * x_0_func - epsilon_c3_func * a2_func) /
                          (epsilon_yd_func - epsilon_c3_func), 6)

    return x_lim_func, epsilon_yd_func, x_min_minus_yd_func, x_min_yd_func, x_0_func, x_max_yd_func, d_func


def eccentricity(m_ed_func, n_ed_func, h_func, a1_func, a2_func):  # eccentricity for compression
    e_func = round(abs(m_ed_func / n_ed_func), 6)

    e_s1_func = round(float(e_func + 0.5 * h_func - a1_func), 6)
    e_s2_func = round(float(e_func - 0.5 * h_func + a2_func), 6)

    return e_func, e_s1_func, e_s2_func


def eccentricity_extension(m_ed_func, n_ed_func, h_func, a1_func, a2_func):  # eccentricity for extension
    e_func = round(abs(m_ed_func / n_ed_func), 6)

    e_s1_func = round(float(e_func - 0.5 * h_func + a1_func), 6)
    e_s2_func = round(float(e_func + 0.5 * h_func - a2_func), 6)

    return e_func, e_s1_func, e_s2_func


concrete = [[12, 1.6],
            [16, 1.9],
            [20, 2.2],
            [25, 2.6],
            [30, 2.9],
            [35, 3.2],
            [40, 3.5],
            [45, 3.8],
            [50, 4.1],
            [55, 4.2],
            [60, 4.4],
            [70, 4.6],
            [80, 4.8],
            [90, 5.0]]

concrete_dic = {
    "C12/15": concrete[0],
    "C16/20": concrete[1],
    "C20/25": concrete[2],
    "C25/30": concrete[3],
    "C30/37": concrete[4],
    "C35/45": concrete[5],
    "C40/50": concrete[6],
    "C45/55": concrete[7],
    "C50/60": concrete[8],
    "C55/67": concrete[9],
    "C60/75": concrete[10],
    "C70/85": concrete[11],
    "C80/95": concrete[12],
    "C90/105": concrete[13]
}


def calculated_value_concrete(concrete_class):
    f_ck, f_ctm = concrete_dic.get(concrete_class)

    alphacc = 1.0  # one of factor to calculate fcd, according to EC 1992 -1 -1 recommended value is 1.0
    gammac = 1.4  # concrete factor for basic situation

    if f_ck < 50:
        lambda_bet = 0.8
    else:
        lambda_bet = round(0.8 - (f_ck - 50) / 400, 6)

    if f_ck < 50:
        eta_bet = 1.0
    else:
        eta_bet = round(1.0 - (f_ck - 50) / 200, 6)

    f_cd = round(alphacc * (f_ck / gammac), 6)

    return eta_bet, lambda_bet, f_cd, f_ctm, f_ck
