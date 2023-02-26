# Домашнее задание №1 упражнение №3
MIN = 0
MAX = 100_000

num = int(input(f"Введите число от {MIN} до {MAX}: "))

divider = 2
count = 0

if (num >= MIN and num <= 100_000):
    for i in range(divider, num - 1):
        if (num% i == 0):
            count += 1
    if (count <= 0):
        print("Число является простым")
    else:
        print("Число является составным")
else:
    print("Введённое число не входит в заданный диапазон")