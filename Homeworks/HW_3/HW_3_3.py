items = {'Мультитул': 500, 
         'Одеяло': 500, 
         'Котелок': 1000, 
         'Еда': 2500, 
         'Вода': 1000, 
         'Спички': 100, 
         'Палатка': 3000, 
         'Мешок': 2000, 
         }
bag = 10000
result = []
for elements in items:
    if bag > items[elements]:
        result.append(elements)
        bag = bag - int(items[elements])
    else: break
print(result)