import math

# Количество окрашенных деталей
painted_details = 9

# Общее количество деталей
total_details = 15

# Количество деталей, которые нужно извлечь
drawn_details = 3

# Количество благоприятных исходов (сочетаний всех окрашенных деталей)
favorable_outcomes = math.comb(painted_details, drawn_details)

# Общее количество исходов (общее количество сочетаний деталей)
total_outcomes = math.comb(total_details, drawn_details)

# Вероятность того, что все извлеченные детали окрашены
probability_all_painted = favorable_outcomes / total_outcomes

print("Вероятность того, что все извлеченные детали окрашены:", probability_all_painted)
