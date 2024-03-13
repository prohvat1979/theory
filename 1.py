import math

# Общее количество карт в колоде
total_cards = 52

# Количество карт каждой масти
cards_per_suit = total_cards // 4

# Количество карт, которые мы извлекаем
drawn_cards = 4

# a) Найти вероятность того, что все карты – крести
# Количество сочетаний 4 карт из 13 крестей
combinations_all_hearts = math.comb(cards_per_suit, drawn_cards)

# Вероятность того, что все карты – крести
probability_all_hearts = combinations_all_hearts / math.comb(total_cards, drawn_cards)

print("Вероятность того, что все карты – крести:", probability_all_hearts)

# b) Найти вероятность, что среди 4-х карт окажется хотя бы один туз
# Количество сочетаний 4 карт без тузов
combinations_without_ace = math.comb(total_cards - 4, drawn_cards)

# Вероятность того, что среди 4 карт не окажется ни одного туза
probability_no_ace = combinations_without_ace / math.comb(total_cards, drawn_cards)

# Вероятность того, что среди 4 карт окажется хотя бы один туз
probability_at_least_one_ace = 1 - probability_no_ace

print("Вероятность того, что среди 4-х карт окажется хотя бы один туз:", probability_at_least_one_ace)
