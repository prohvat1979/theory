# Импорт библиотеки для вычисления комбинаторики
import math

# Вероятность того, что все мячи белые
probability_all_white = (math.comb(7, 2) / math.comb(10, 2)) * (math.comb(9, 2) / math.comb(11, 2))

# Вероятность того, что ровно два мяча белые
# Для первого случая: 2 белых мяча из первого ящика и 2 небелых мяча из второго ящика
probability_two_white_case1 = (math.comb(7, 2) / math.comb(10, 2)) * (math.comb(2, 2) / math.comb(11, 2))
# Для второго случая: 2 небелых мяча из первого ящика и 2 белых мяча из второго ящика
probability_two_white_case2 = (math.comb(3, 2) / math.comb(10, 2)) * (math.comb(9, 2) / math.comb(11, 2))
probability_two_white = probability_two_white_case1 + probability_two_white_case2

# Вероятность того, что хотя бы один мяч белый
probability_at_least_one_white = 1 - ((math.comb(3, 2) / math.comb(10, 2)) * (math.comb(2, 2) / math.comb(11, 2)))

print("Вероятность того, что все мячи белые:", probability_all_white)
print("Вероятность того, что ровно два мяча белые:", probability_two_white)
print("Вероятность того, что хотя бы один мяч белый:", probability_at_least_one_white)
