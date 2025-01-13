# 1
a = int(input('Введите число: '))
i = 1
while i <= a:
    print(i)
    i += 1

# 2
a = int(input('Введите первое число: '))
i = int(input('Введите первое число: '))
if a > i:
    print('Большее число:', a)
elif i > a:
    print('Большее число:', i)
