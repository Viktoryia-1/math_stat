# Даны значения зарплат из выборки выпускников:
# 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30,
# 24, 57, 55, 70, 75, 65, 84, 90, 150. Посчитать
# (желательно без использования статистических методов наподобие std, var, mean)
# среднее арифметическое, среднее квадратичное отклонение, смещенную
# и несмещенную оценки дисперсий для данной выборки.
from lesson_2_task1_4 import combination
import pandas as pd
workers = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17,
           30, 24, 57, 55, 70, 75, 65, 84, 90, 150]

# Среднее арифметическое
x_ = sum(workers) / len(workers)
print(f"Среднее арифметическое: {round(x_, 2)}")


# смещенная дисперсия
x2 = sum([el **2 for el in workers])
d = x2/len(workers) - x_**2
print(f"Cмещенная дисперсия (рассчет по определению) {round(d, 2)} ")

# или
d_2 = sum([(el - x_)**2 for el in workers]) / len(workers)
print(f"Cмещенная дисперсия (рассчет по формуле) {round(d_2, 2)} ")


# несмещенная дисперсия
d_n = (len(workers)/( len(workers) - 1)) * d
print(f"Несмещенная дисперсия {round(d_n, 2)}")

# Среднее квадратичное отклонение


def medium(data):
    x_2 = (sum([(el - x_) ** 2 for el in data]) / len(workers)) ** 0.5
    return x_2


q = medium(workers)
print(f"Среднее квадратичное отклонение (рассчет по формуле) {round(q, 2)}  ")
# или
print(f"Среднее квадратичное отклонение (корень из дисперсии) {round(d ** 0.5, 2)}")

# Проверка
workers = pd.DataFrame(workers)
print(workers.mean(), workers.std(ddof=0), workers.var(ddof=0), workers.var(ddof=1))
# В первом ящике находится 8 мячей, из которых 5 - белые.
# Во втором ящике - 12 мячей, из которых 5 белых.
# Из первого ящика вытаскивают случайным образом два мяча, из второго - 4.
# Какова вероятность того, что 3 мяча белые?

p_1 = (combination(5, 2) * combination(3, 0) / combination(8, 2)) * (combination(5, 1) * combination(7, 3) / combination(12, 4))
p_2 = (combination(5, 1) * combination(3, 1) / combination(8, 2)) * (combination(5, 2) * combination(7, 2) / combination(12, 4))
p_3 = (combination(5, 0) * combination(3, 2) / combination(8, 2)) * (combination(5, 3) * combination(3, 1) / combination(12, 4))
print(f"Вероятность трех белых мячей {round(p_1 + p_2 + p_3, 2)}")