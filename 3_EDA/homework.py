# 1. Даны значения зарплат из выборки выпускников: 
# 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150. 
# Посчитать (желательно без использования статистических методов наподобие std, var, mean) 
# среднее арифметическое, среднее квадратичное отклонение, смещенную и несмещенную оценки дисперсий для данной выборки.

import numpy as np
import math

x = np.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150])
n = len(x)
print(n) # 20

x.sort()
print(x) # [17  24  25  30  33  45  55  57  65  65  70  75  75  77  80  84  89  90 100 150]

average = sum(x) / n
print(f'Среднее арифметическое: ', average) #  65,3
print(f'Среднее арифметическое: ', np.mean(x)) # 65,3

variance_1 = sum([(i - average)**2 for i in x]) / n
print(f'Смещенная дисперсия: ', variance_1) #  950,11
print(f'Смещенная дисперсия: ', np.var(x)) # 950,11

variance_2 = sum([(i - average)**2 for i in x]) / (n - 1)
print(f'Несмещенная дисперсия: ', variance_2) # 1000,12
print(f'Несмещенная дисперсия: ', np.var(x, ddof=1)) # 1000,12

deviation_1 = math.sqrt(variance_1)
print(f'Смещенное среднее квадратичное отклонение: ', deviation_1) #  30,82
print(f'Смещенное среднее квадратичное отклонение: ', np.std(x)) # 30,82

deviation_2 = math.sqrt(variance_2)
print(f'Несмещенное среднее квадратичное отклонение: ', deviation_2) # 31,62
print(f'Несмещенное среднее квадратичное отклонение: ', np.std(x, ddof=1)) # 31,62

#############################################################################################

# 2. В первом ящике находится 8 мячей, из которых 5 - белые. Во втором ящике - 12 мячей, из которых 5 белых. 
# Из первого ящика вытаскивают случайным образом два мяча, из второго - 4. Какова вероятность того, что 3 мяча белые?

p1 = math.comb(5, 2) * math.comb(3, 0)  / math.comb(8, 2)
print(f'вероятность, что из первого ящика вытянули 2 белых мяча и 0 не белых: ', p1) # 0,357

p2 = math.comb(5, 1) * math.comb(3, 1) / math.comb(8, 2)
print(f'вероятность, что из первого ящика вытянули 1 белый мяч и 1 не белый: ', p2) # 0,536

p3 = math.comb(5, 0) * math.comb(3, 2) / math.comb(8, 2)
print(f'Вероятность, что из первого ящика вытянули 0 белых мячей и 2 не белых: ', p3) # 0,107

p4 = math.comb(5, 1) * math.comb(7, 3) / math.comb(12, 4)
print(f'Вероятность, что из второго ящика вытянули 1 белый мяч и 3 не белых: ', p4) # 0,354

p5 = math.comb(5, 2) * math.comb(7, 2) / math.comb(12, 4)
print(f'Вероятность, что из второго ящика вытянули 2 белых мяча и 2 не белых: ', p5) # 0,424

p6 = math.comb(5, 3) * math.comb(7, 1)/ math.comb(12, 4)
print(f'Вероятность, что из второго ящика вытянули 3 белых мяча и 1 не белый: ', p6) # 0,141

P = p1*p4 + p2*p5 + p3*p6
print(f'Вероятность, что вытянули 3 белых мяча: ', P) # 0,369

#############################################################################################

# 3. На соревновании по биатлону один из трех спортсменов стреляет и попадает в мишень. 
# Вероятность попадания для первого спортсмена равна 0.9, для второго — 0.8, для третьего — 0.6. 
# Найти вероятность того, что выстрел произведен: a). первым спортсменом б). вторым спортсменом в). третьим спортсменом.

# A - попадание
# B1 - первый выстрелил
# B2 - второй выстрелил
# B3 - третий выстрелил

# P(A) = P(B1)*P(A|B1) * P(B2)*P(A|B2) * P(B3)*P(A|B3)
# P(B1|A) = P(A|B1) * P(B1) / P(A)
# P(B2|A) = P(A|B2) * P(B2) / P(A)
# P(B3|A) = P(A|B3) * P(B3) / P(A)

P_A = (1/3 * 0.9) + (1/3 * 0.8) + (1/3 * 0.6)
P_B1 = (0.9 * 1/3) / P_A
P_B2 = (0.8 * 1/3) / P_A
P_B3 = (0.6 * 1/3) / P_A

# print(P_A) # P(A) = 0.767
print(f'Вероятность, что выстрел произведен первым спортсменом: ', P_B1) # 0,391
print(f'Вероятность, что выстрел произведен вторым спортсменом: ', P_B2) # 0,348
print(f'Вероятность, что выстрел произведен третьим спортсменом: ', P_B3) # 0,261

#############################################################################################

# 4. В университет на факультеты A и B поступило равное количество студентов, а на факультет C студентов поступило столько же, 
# сколько на A и B вместе. Вероятность того, что студент факультета A сдаст первую сессию, равна 0.8. 
# Для студента факультета B эта вероятность равна 0.7, а для студента факультета C - 0.9. 
# Студент сдал первую сессию. Какова вероятность, что он учится: a). на факультете A б). на факультете B в). на факультете C?

# А - сессия сдана
# B1 - студент с факультета А P(B1) = 0,25
# B2 - студент с факультета B P(B2) = 0,25 
# B3 - студент с факультета C P(B3) = 0,5 

# P(A) = P(B1)*P(A|B1) + P(B2)*P(A|B2) + P(B3)*P(A|B3)
# P(B1|A) = P(A|B1) * P(B1) / P(A)
# P(B2|A) = P(A|B2) * P(B2) / P(A)
# P(B3|A) = P(A|B3) * P(B3) / P(A)

P_A = (0.25 * 0.8) + (0.25 * 0.7) + (0.5 * 0.9)
P_B1 = 0.8 * 0.25 / P_A
P_B2 = 0.7 * 0.25 / P_A
P_B3 = 0.9 * 0.5 / P_A

# print(P_A) # P(A) = 0,825
print(f'Вероятность, что сдавший сессию студент учится на факультете A: ', P_B1) # 0,242
print(f'Вероятность, что сдавший сессию студент учится на факультете B: ', P_B2) # 0,212
print(f'Вероятность, что сдавший сессию студент учится на факультете C: ', P_B3) # 0,545

#############################################################################################

# 5. Устройство состоит из трех деталей. Для первой детали вероятность выйти из строя в первый месяц равна 0.1, 
# для второй - 0.2, для третьей - 0.25. Какова вероятность того, что в первый месяц выйдут из строя: 
# а). все детали б). только две детали в). хотя бы одна деталь г). от одной до двух деталей?

# A - в первый месяц выйдут из строя все детали
# B - в первый месяц выйдут из строя только две детали
# C - в первый месяц выйдет из строя хотя бы одна деталь
# D - в первый месяц выйдут из строя от одной до двух деталей

P_A = 0.1 * 0.2 * 0.25
P_B = (0.9 * 0.2 * 0.25) + (0.1 * 0.8 * 0.25) + (0.1 * 0.2 * 0.75)
P_C = P_A + P_B + (0.9 * 0.8 * 0.25) + (0.1 * 0.8 * 0.75) + (0.9 * 0.2 * 0.75)
P_D = P_B + (0.9 * 0.8 * 0.25) + (0.1 * 0.8 * 0.75) + (0.9 * 0.2 * 0.75)

print(f'В первый месяц выйдут из строя все детали: ', P_A) # 0,005
print(f'В первый месяц выйдут из строя только две детали: ', P_B) # 0,08
print(f'В первый месяц выйдет из строя хотя бы одна деталь: ', P_C) # 0,46
print(f'В первый месяц выйдут из строя от одной до двух деталей: ', P_D) # 0,455