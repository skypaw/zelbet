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
                          (epsilon_yd_func + epsilon_c3_func), 4)

    return x_lim_func, epsilon_yd_func, x_min_minus_yd_func, x_min_yd_func, x_0_func, x_max_yd_func, d_func


def eccentricity(m_ed_func, n_ed_func, h_func, a1_func, a2_func):
    e_func = round(abs(m_ed_func / n_ed_func), 4)

    e_s1_func = round(float(e_func + 0.5 * h_func - a1_func), 4)
    e_s2_func = round(float(e_func - 0.5 * h_func + a2_func), 4)

    return e_func, e_s1_func, e_s2_func
