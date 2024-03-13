import math

# Общее количество кнопок
total_buttons = 10

# Количество кнопок, которые нужно нажать одновременно
required_buttons = 3

# Количество благоприятных исходов (количество сочетаний)
favorable_outcomes = math.comb(total_buttons, required_buttons)

# Общее количество возможных исходов (общее количество сочетаний)
total_outcomes = math.comb(total_buttons, required_buttons)

# Вероятность открытия двери с первой попытки
probability_first_attempt = favorable_outcomes / total_outcomes

print("Вероятность открытия двери с первой попытки:", probability_first_attempt,"%")
