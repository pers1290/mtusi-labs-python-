# 1
def greet(name):
    print(f'Привет, {name}')


def square(number):
    return number ** 2


def max_of_two(x, y):
    if x > y:
        return x
    return y


# 2
def describe_person(name, age=30):
    print(f'Имя: {name}, возраст: {age}')


# 3
def is_prime(number):
    if number == 1:
        return False
    i1 = 2
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            i1 += 1
    if i1 == 2:
        return True
    return False


print(is_prime(11))
