import math

# Количество испытаний (лампочек)
n = 5000

# Вероятность перегорания одной лампочки
p = 0.0004

# Лямбда для распределения Пуассона
lambda_value = n * p

# Вероятность того, что ни одна лампочка не перегорит в первый день
probability_none_burn_out = math.exp(-lambda_value)

print("Вероятность того, что ни одна лампочка не перегорит в первый день:", probability_none_burn_out)

# Вероятность того, что перегорят ровно две лампочки
k = 2
probability_two_burn_out = (lambda_value ** k) * math.exp(-lambda_value) / math.factorial(k)

print("Вероятность того, что перегорят ровно две лампочки:", probability_two_burn_out)
