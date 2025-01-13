# 1
import math
import datetime

c = int(input('Введите число: '))
print(f'квадрат числа = {int(math.sqrt(c))}')

print(f'Дата и время {datetime.datetime.now()}')

# 2
import my_module

a = int(input('Введи число: '))
c = my_module.f(a)
print(f'Квадрат числа: {c}')

# 3
from my_package import kub, str

a = int(input('Введи число: '))
z = kub.f(a)
print(f'куб: {z}')
b = input()
c = input()
x = str.f(b, c)
print(f'Новая строка: {x}')
