# Задача 3. Удаление части
import random

n = int(input('Введите длину списка случайных чисел: '))

list_n = [random.randint(0, 100) for _ in range(n)]
b = random.randint(0, n)
a = random.randint(0, b)

print('list_n =', list_n)
print('a =', a)
print('b =', b)

print('part a =', list_n[:a])
print('part b =', list_n[b:])
list_n = list_n[:a] + list_n[a:]
print('New list_n = ', list_n)
