# Python_HW
## Homework 1
1. Решить задачи, которые не успели решить на семинаре.
------------------------------------------
- Задание №8

    Нарисовать в консоли ёлку спросив у пользователя количество рядов.
- Задание №9

    Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
------------------------------------------

2. Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным. Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

## Homework 2

1. Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. Функцию hex используйте для проверки своего результата.
2. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

## Homework 3
1. Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.
2. В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.
3. Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.

## Homework 4

1. Напишите функцию для транспонирования матрицы
2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ - значение переданного аргумента, а значение - имя аргумента. Если ключ не хешируем, используйте его строковое представление.

## Homework 5
1. Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
2. Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int, премия str с указанием процентов вида “10.25%”. В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии
3. Создайте функцию генератор чисел Фибоначчи (см. Википедию)

## Homework 6

1. Добавьте в модуль с загадками функцию, которая хранит словарь списков. Ключ словаря - загадка, значение - список с отгадками. Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.

2. Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999]. Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь. Проверку года на високосность вынести в отдельную защищённую функцию.

3. Создайте пакет с всеми модулями, которые вы создали за время занятия. Добавьте в init пакета имена модулей внутри дандер all. В модулях создайте дандер all и укажите только те функции, которые могут верно работать за пределами модуля.

## Homework 7

1. Напишите функцию группового переименования файлов. Она должна:
    - принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
    - принимать параметр количество цифр в порядковом номере.
    - принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
    - принимать параметр расширение конечного файла.
    - принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
2. Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.

## Homework 8
1. Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
    -   Для дочерних объектов указывайте родительскую директорию. 
    -   Для каждого объекта укажите файл это или директория.
    -   Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.

2. Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.


## Homework 9
1. Напишите следующие функции:
    - Нахождение корней квадратного уравнения
    - Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
    - Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
    - Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
2. Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса

## Homework 10
1. Доработаем задачи 5. Создайте класс-фабрику. Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа. Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
2. Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация данных), которые вы уже решали. Превратите функции в методы класса, а параметры в свойства. Задачи должны решаться через вызов методов экземпляра.

## Homework 11
1. Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.
2. Создайте класс Матрица. Добавьте методы для:
    - вывода на печать,
    - сравнения,
    - сложения,
    - *умножения матриц

## Homework 12
Создайте класс студента.
 - Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
 - Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
 - Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
 - Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых. 

## Homework 13

Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях. Напишите к ним классы исключения с выводом подробной информации.
Поднимайте исключения внутри основного кода. Например нельзя создавать прямоугольник со сторонами отрицательной длины.

