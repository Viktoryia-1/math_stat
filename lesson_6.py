import scipy.stats
import numpy as np
import pandas as pd
# Даны значения величины заработной платы заемщиков банка (zp)
# и значения их поведенческого кредитного скоринга (ks):
# zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],
# ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].
# Найдите ковариацию этих двух величин с помощью элементарных действий,
# а затем с помощью функции cov из numpy
# Полученные значения должны быть равны.
# Найдите коэффициент корреляции Пирсона с помощью ковариации и
# среднеквадратичных отклонений двух признаков,
# а затем с использованием функций из библиотек numpy и pandas.

# формулы
n = 10
zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
x_i = sum(zp)
y_i = sum(ks)
x_i_sqrt = sum([i**2 for i in zp])
y_i_sqrt = sum([i**2 for i in ks])

xy = zp * ks
xy_med = sum(xy)

count_cov = 10 * xy_med - x_i * y_i

count_corr = count_cov / (((n * x_i_sqrt - x_i**2)**0.5) * ((n * y_i_sqrt - y_i**2)**0.5))
print(f"Корреляция между зарплатой и значением скоринга равна {round(count_corr, 5)}")

# numpy
cov_matrix = np.cov(zp, ks)
corr_matrix = np.corrcoef(zp, ks)
print(cov_matrix)
print(corr_matrix)

# pandas
data = pd.DataFrame({"zp": [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],
                     "ks": [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]})
print(data.cov())
print(data.corr())


# Измерены значения IQ выборки студентов,
# обучающихся в местных технических вузах:
# 131, 125, 115, 122, 131, 115, 107, 99, 125, 111.
# Известно, что в генеральной совокупности IQ распределен нормально.
# Найдите доверительный интервал для математического ожидания с
# надежностью 0.95.

iq = [131, 125, 115, 122, 131, 115, 107, 99, 125, 111]
n = 10
y = 0.95
x_med = sum(iq) / n
d = (sum([el ** 2 - x_med ** 2 for el in iq])) / n
d_correct = (d * 10) / 9
s_correct = d_correct ** 0.5
t = scipy.stats.t.ppf(y, n - 1)

delta = (t * s_correct) / 10 ** 0.5

print(f"Доверительный интервал: {round(x_med - delta, 3)}, {round(x_med + delta, 3)}")

# Известно, что рост футболистов в сборной распределен нормально
# с дисперсией генеральной совокупности, равной 25 кв.см.
# Объем выборки равен 27,
# среднее выборочное составляет 174.2.
# Найдите доверительный интервал для математического
# ожидания с надежностью 0.95.

d_2 = 25
n_2 = 27
x_med_2 = 174.2
y_2 = 0.95

l_value = y_2 / 2
x_2 = np.arange(0, 5, 0.01)
laplase_value = scipy.stats.norm.cdf(x_2) - 0.5

list_of_index = []
for el in list(laplase_value.copy()):
    if round(el, 4) == l_value:
        index = list_of_index.append(list(laplase_value).index(el))

index = round(sum(list_of_index) / len(list_of_index))
laplase_argument = list(x_2)[index]

delta_2 = (laplase_argument * d_2 ** 0.5) / n_2 ** 0.5

print(f"Доверительный интервал: {round(x_med_2 - delta_2, 3)},"
      f" {round(x_med_2 + delta_2)}")


