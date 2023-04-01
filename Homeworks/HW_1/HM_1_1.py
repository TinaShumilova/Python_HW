# Домашнее задание №1 упражнение №1

print("Задание №8 с семинара")
rows = int(input("Задайте колличество рядов в ёлке: "))
count = 1
step = " "
step2 = 1
star = "*" 
print(step)
while (rows > 0):
    three = step * (rows - count) + star * step2
    print(three)
    rows -= 1
    step2 += 2

# 1 Задание №9
print("Задание №9 с семинара")
factor = 2
number = 2
while (number < 10):
    if (factor <= 10):
        print(f"{number}x{factor} = {number * factor}")
        factor +=1
    else:
        print(" ")
        factor = 2
        number += 1
        continue

