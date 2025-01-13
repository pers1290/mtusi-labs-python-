# 1
r = 2
with open('example.txt', 'r', encoding='utf8') as file:
    if r == 1:
        a = file.read()
        print(a)
    elif r == 2:
        for line in file:
            print(line)

# 2
user_text = input("Введите текст для записи в файл: ")
with open("user_input.txt", "a", encoding='utf8') as file:
    file.write(user_text)

# 3
try:
    file = open("user_input.txt", 'r', encoding='utf8')
except FileNotFoundError:
    print(f"файл ненайден")
else:
    c = file.read()
    print(c)
