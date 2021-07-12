# Провести дисперсионный анализ для определения того,
# есть ли различия среднего роста среди взрослых футболистов,
# хоккеистов и штангистов. Даны значения роста в трех группах
# случайно выбранных спортсменов:
# Футболисты: 173, 175, 180, 178, 177, 185, 183, 182.
# Хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180.
# Штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170.
# alpha = 0.05.
import numpy as np
from scipy import stats
footballers = np.array([173, 175, 180, 178, 177, 185, 183, 182])
hockeyplayers = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
weightlifters = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])
all_weights = np.concatenate([footballers, hockeyplayers, weightlifters])
n = len(footballers) + len(hockeyplayers) + len(weightlifters)
print(n)

med_footballers = np.mean(footballers)
med_hockeyplayers = np.mean(hockeyplayers)
med_weightlifters = np.mean(weightlifters)
all_med_weight = np.mean(all_weights)

s_2 = sum((footballers - all_med_weight) ** 2) + \
         sum((hockeyplayers - all_med_weight) ** 2) + \
         sum((weightlifters - all_med_weight) ** 2)
s_s_2 = sum((all_weights - all_med_weight) ** 2)
s_f = ((med_weightlifters - all_med_weight) ** 2) * len(weightlifters) + \
      ((med_hockeyplayers - all_med_weight) ** 2) * len(hockeyplayers) + \
      ((med_footballers - all_med_weight) ** 2) * len(footballers)
s_ost = np.sum((footballers - med_footballers) ** 2) \
        + np.sum((hockeyplayers - med_hockeyplayers) ** 2) \
        + np.sum((weightlifters - med_weightlifters) ** 2)
print(f"Сумма квадратов отклонений {round(s_2, 2)}")
print(f"сумма квадратов отклонений средних групповых значений"
      f" от общего среднего значения {round(s_f, 2)}")
print(f"остаточная сумма квадратов отклонений {round(s_ost, 2)}")


sigma_all = s_2 / (n - 1)
sigma_f = s_f / 2
sigma_ost = s_ost / (n - 3)
print(f"Общаа дисперсия{round(sigma_all, 2)}, факторная дисперсия {round(sigma_f, 2)},"
      f" остаточная дисперсия {round(sigma_ost, 2)}")
f_n = sigma_f / sigma_ost
print(f"F_наблюдаемое {round(f_n, 2)}")
# Если уровень значимости 0.05
f_crit = 3.38
# Если уровень значимости 0.01
f_crit_2 = 6.11
n_2 = s_f / s_2
print(f"Значение эта {round(n_2, 2)}")

print(stats.f_oneway(footballers, hockeyplayers, weightlifters))

print(f"Вывод: при уровне значимости 0.01 различие роста в данных группах \n"
      f"  статистически незначимо при уровне значимости 0.05 спорно,\n"
      f" т.к F_наблюдаемое больше чем F_критическое,но показатель эта равен 0.3")
