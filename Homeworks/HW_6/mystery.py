__all__ = ["guess_mystery", "keep_mystery"]

def guess_mystery(s: str, ans: list, chan: int) -> int:
    print(f"Отгадайте загадку: {s}")
    for i in range(chan):
        answer = input("Ответ: ")
        if answer in ans:
            return i + 1
    return 0

def keep_mystery():
    all_mysteries = {
        "Зимой и летом одним цветом": ["Ель", "ель", "елка", "ёлка", "Елка", "Ёлка", "Сосна", "сосна"],
        "У конца два кольца": ["Ножницы", "Резалки"],
        "Мчится печка впереди, тащит избы позади.": ['Поезд', 'паровоз']
    }
    chances = int(input("За сколько раз отгадаешь загадку? "))
    for key in all_mysteries:
        guess_mystery(key, all_mysteries[key], chances)

if __name__ == '__main__':
    keep_mystery()