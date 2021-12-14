# Задача 1. Анализ цен

import random

original_prices = [random.randint(-20, 40) for _ in range(10)]
new_prices = [x if x > 0 else 0 for x in original_prices]

print("Мы потеряли: ",  -1 * (sum(original_prices) - sum(new_prices)))
