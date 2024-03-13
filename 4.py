import math

# Количество выигрышных билетов
winning_tickets = 2

# Общее количество билетов
total_tickets = 100

# Количество билетов, которые нужно приобрести
purchased_tickets = 2

# Количество благоприятных исходов (сочетаний из 2 выигрышных билетов)
favorable_outcomes = 1

# Общее количество исходов (общее количество сочетаний билетов)
total_outcomes = math.comb(total_tickets, purchased_tickets)

# Вероятность того, что оба приобретенных билета окажутся выигрышными
probability_both_winning = favorable_outcomes / total_outcomes

print("Вероятность того, что оба приобретенных билета окажутся выигрышными:", probability_both_winning)
