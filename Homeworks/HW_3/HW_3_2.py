text = "Словари в Python предназначены для создания пары ключ-значение, доступ к которым осуществляется мгновенно. \
        Что если пришлось итерироваться вокруг словаря? При этом нас волнует порядок, при котором появляются \
        элементы. Тогда первое, что приходит на ум — это сортировать словарь. Итак, в этой статье мы расскажем, как \
        сортировать словарь в Python по ключу и значению. В Python 3.7 словарь упорядочен. Это означает, что при \
        каждом добавлении элемента, он вставляется в конец. Причем, как пишет реализующий это человек, такой механизм \
        на 50% использует меньше памяти и в 2 раза быстрее происходит итерирование [2].При этом если обновить значение, \
        то ключ останется на том же месте".split()

for i in range(len(text)):
    if text[i].istitle():
        text[i] = text[i].lower()
    if "." in text[i]: 
        text[i] = text[i].replace(".", "")
    if "," in text[i]: 
        text[i] = text[i].replace(".", "")

temp_dict = dict()
for item in text:
    key = temp_dict.setdefault(item, text.count(item))


values = temp_dict.values()
sorted_values = list(sorted(values, reverse=True))

result = {}
top = 10

for value in sorted_values:
        for element in temp_dict.keys():
            if temp_dict[element] == value:
                if element not in result:
                    result[element] = temp_dict[element]
                    top -= 1
                    break
        if top <= 0: break
            
print(result)