# Даны значения величины заработной платы заемщиков банка
# (zp) и значения их поведенческого кредитного скоринга
# (ks): zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],
# ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].
# Используя математические операции, посчитать коэффициенты линейной
# регрессии, приняв за X заработную плату (то есть, zp - признак),
# а за y - значения скорингового балла
# (то есть, ks - целевая переменная).
# Произвести расчет как с использованием intercept, так и без.
import numpy as np
zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
n = 10
# y = a + bx

b = (np.mean(zp * ks) - np.mean(zp) * np.mean(ks)) / (np.mean(zp ** 2) - np.mean(zp) ** 2)
print(f"Коэффициент b {round(b, 2)}")

a = np.mean(ks) - b * np.mean(zp)
print(f"Коэффицциент а {round(a, 2)}")

# y = 444.1 + 2.6x

r = b * (np.std(zp) / np.std(ks))
print(f"Коэффициент корреляции {round(r, 2)}")

r_2 = r ** 2
print(f"Коэффициент детерминации {round(r_2, 2)}")

ks_pred = a + b * zp
print(f"Значения кредитного скоринга, рассчитанные данной моделью {ks_pred}")

a_mean = 100 * np.mean(np.abs((ks - ks_pred) / ks))
# или
a_mean_2 = 100 * ((np.abs((ks - ks_pred) / ks)).sum() / n)
if a_mean <= 10:
    print(f"Теоретическая модель отражает реальные данные, ошибка {round(a_mean, 2)} %")
else:
    print(f"Теоретическая модель не отражает реальные данные, ошибка {round(a_mean, 2)} %")

# F - критерий Фишера
f_fact = (r_2 * (n - 2)) / (1 - r_2)
f_crit = 5.32
if f_fact > f_crit:
    print(f"уравнение регрессии статистически значимо")
else:
    print(f"уравнение регрессии статистически не значимо")

s_standart_mse = ((ks - ks_pred) ** 2).sum() / n
s_standart_rmse = np.sqrt(sum((ks - ks_pred) ** 2) / (n - 2))

print(f"Стандартная ошибка {round(s_standart_rmse, 2)},"
      f" средняя квадратичная ошибка {round(s_standart_mse,2)}")

# Для уровня значимости 0.05
t_crit = 2.3

m_a = s_standart_rmse * (((np.sqrt(sum(zp ** 2)))/ (np.std(zp) * n)))
m_b = s_standart_rmse /(np.std(zp) * np.sqrt(n))

print(f"Случайные ошибки: {round(m_a, 2)}, {round(m_b, 2)}")

t_a = a / m_a
t_b = b / m_b
if t_a and t_b > t_crit:
    print(f"Коэффициенты регрессии считаются значимым")
else:
    print(f"Коэффициенты регрессии не считаются значимым")

delta_a = t_crit * m_a
delta_b = t_crit * m_b

print(f"Доверительный интервал коэффициента а: {round(a - delta_a, 2)} , {round(a + delta_a, 2)}")
print(f"Доверительный интервал коэффициента b: {round(b - delta_b, 2)}, {round(b + delta_b, 2)} ")

#Матричный метод
zp_int = zp.reshape(10, 1)
ks_int = ks.reshape(10, 1)
zp_int = np.hstack([np.ones((10,1)), zp_int])
b_matrix_int = np.dot(np.linalg.inv(np.dot(zp_int.T, zp_int)), zp_int.T @ ks_int)
print(b_matrix_int)

# рассчет без  intercept:
# y = bx
zp = zp.reshape(10, 1)
ks = ks.reshape(10, 1)
b_matrix = np.dot(np.linalg.inv(np.dot(zp.T, zp)), zp.T @ ks)
print(b_matrix)
