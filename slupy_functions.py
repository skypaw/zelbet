# coding=utf-8

import numpy as np

const_parameters = (0.0035, 0.00175, 435, 200000)


def x_solution(a_func, b_func, c_func, d_func):
    solution = [a_func, b_func, c_func, d_func]

    results = [np.roots(solution)]
    res = []
    for i in results[0]:
        if i.imag == 0.0:
            res.append(i)

    x_function = min([n for n in res if n > 0])
    return x_function, res


def start_parameters(epsilon_cu3_func, epsilon_c3_func, f_yd_func, es_func, a2_func, a1_func, h_func):
    d_func = round(h_func - a1_func, 4)
    x_lim_func = round((epsilon_cu3_func * d_func) / (epsilon_cu3_func + f_yd_func / es_func), 4)
    epsilon_yd_func = float(f_yd_func / es_func)

    x_min_minus_yd_func = round((epsilon_cu3_func * a2_func) / (epsilon_cu3_func + f_yd_func / es_func), 4)
    x_min_yd_func = round((epsilon_cu3_func * a2_func) / (epsilon_cu3_func - f_yd_func / es_func), 4)
    x_0_func = round((1 - epsilon_c3_func / epsilon_cu3_func) * h_func, 4)
    x_max_yd_func = round((epsilon_yd_func * x_0_func - epsilon_c3_func * a2_func) /
                          (epsilon_yd_func - epsilon_c3_func), 4)

    return x_lim_func, epsilon_yd_func, x_min_minus_yd_func, x_min_yd_func, x_0_func, x_max_yd_func, d_func


def eccentricity(m_ed_func, n_ed_func, h_func, a1_func, a2_func):
    e_func = round(abs(m_ed_func / n_ed_func), 4)

    e_s1_func = round(float(e_func + 0.5 * h_func - a1_func), 4)
    e_s2_func = round(float(e_func - 0.5 * h_func + a2_func), 4)

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

    alfacc = 1.0  # one of fractor to count fcd, according to EC 1992 -1 -1 recommended is 1.0
    gammac = 1.4  # concrete factor for  nomal situation todo addproperties menu where can change this whenever i want

    if f_ck < 50:
        lambda_bet = 0.8
    else:
        lambda_bet = round(0.8 - (f_ck - 50) / 400, 4)

    if f_ck < 50:
        eta_bet = 1.0
    else:
        eta_bet = round(1.0 - (f_ck - 50) / 200, 4)

    f_cd = round(alfacc * (f_ck / gammac), 2)

    return eta_bet, lambda_bet, f_cd, f_ctm
