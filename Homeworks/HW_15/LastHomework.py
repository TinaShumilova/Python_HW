from MyExceptions import MyMinLengthError, MyTriangleError, CheckBagSize
import logging
import argparse

logging.basicConfig(
    filename="logfile.log", 
    encoding='utf-8', 
    format='{asctime} {levelname} {funcName}->{lineno}: {msg}',
    style='{',
    level=logging.INFO
    )


parser = argparse.ArgumentParser(description='My first argument parser')
parser.add_argument('numbers', metavar='N', type=int,
nargs='*', help='press some numbers')
args = parser.parse_args()
print(f'Получили экземпляр Namespace: {args = }')
print(f'У Namespace работает точечная нотация: {args.numbers =}')
print(f'Объекты внутри могут быть любыми: {args.numbers[1] = }')
logging.info(f'В скрипт передано: {args}')


class Triangle:

    def __init__(self, a: int, b: int, c: int) -> None:
        if a > 0:
            self.a = a
        else:
            raise MyMinLengthError(a, 0)
        if b > 0:
            self.b = b
        else:
            raise MyMinLengthError(b, 0)
        if c > 0:
            self.c = c
        else:
            raise MyMinLengthError(c, 0)
        
    def check_sides(self):

        check1 = self.a + self.b
        check2 = self.a + self.c
        check3 = self.b + self.c
        if (check1 < self.c or check2 < self.b or check3 < self.a):
            raise MyTriangleError(self.a, self.b, self.c)
        else:
            if (a == b and b == c and c == a):
                logging.info(f'"Треугольник со сторонами {a=}, {b=} и {c=} равносторонний"')
            elif (a == b or b == c or c == a):
                logging.info(f'"Треугольник со сторонами {a=}, {b=} и {c=} равнобедренный"')
            else:
                logging.info(f'"Треугольник со сторонами {a=}, {b=} и {c=} разносторонний"')

class Bag:

    def __init__(self, bag: int, items: dict) -> None:
        self.bag = bag
        self.items = items

    def check_item(self):
        for elements in self.items:
            if self.bag < self.items[elements]:
                raise CheckBagSize(self.bag, self.items[elements])
            else: logging.info(f"Предмет {elements} влезет в сумку")
        logging.info("Предметы проверены")
        

    def pack_bag(self):
        result = []
        for elements in self.items:
            if self.bag > self.items[elements]:
                result.append(elements)
                self.bag = self.bag - int(self.items[elements])
            else: break
        return result

if __name__ == "__main__":
    TEXT = f"Введите длинну стороны треугольника "
    try:
        a = args.numbers[0]
        b = args.numbers[1]
        c = args.numbers[2]
    except ValueError as v:
        logging.error(f"Нужно задать число: {v}")

    t1 = Triangle(a, b, c)
    t1.check_sides()

    items = {'Мультитул': 500, 
         'Одеяло': 500, 
         'Котелок': 1000, 
         'Еда': 2500, 
         'Вода': 1000, 
         'Спички': 100, 
         'Палатка': 3000, 
         'Мешок': 20000, 
         }
    bag = 10000

    b1 = Bag(bag, items)
    b1.check_item()
    logging.info(b1.pack_bag())
