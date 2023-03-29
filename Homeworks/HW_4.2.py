def dictunary(a=2, b=3):
    dictun = {
        f'{a}': id(a),
        f'{b}': id(b)
    }

    return dictun
a = 2
b = 3
temp = dictunary(a, b)
print(temp)