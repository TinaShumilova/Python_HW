# Домашнее задание №1 упражнение №2
TEXT = f"Введите длинну стороны треугольника "
NOT_EXIST = "Tреугольника с такими сторонами не существует!"
a = int(input(TEXT + "№1: "))
b = int(input(TEXT + "№2: "))
c = int(input(TEXT + "№3: "))

check1 = a + b
check2 = a + c
check3 = b + c

if (a > 0 and b > 0 and c > 0):
    if (check1 < c or check2 < b or check3 < a):
        print(NOT_EXIST)
    else:
        if (a == b and b == c and c == a):
            print("Треугольник равносторонний")
        elif (a == b or b == c or c == a):
            print("Треугольник равнобедренный")
        else:
            print("Треугольник разносторонний")
else:
    print(NOT_EXIST)