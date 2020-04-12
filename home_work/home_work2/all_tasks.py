
# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

new_list = [1, 2.2, 'str', False, True, None]

# repeat = 0
# while repeat < 5:
#     element = input("Заполните список элементами с различными типами\n")
#     repeat += 1
#     if element.isdigit():
#         element = int(element)
#         new_list.append(element)
#     elif element is 'None':
#         element = (element)
#         new_list.append(element)
#     # строка
#     elif element.isalpha():
#         element = str(element)
#         new_list.append(element)
#     # десятичная
#     elif element.isdecimal():
#         element = float(element)
#         new_list.append(element)

for itm in new_list:
    print(type(itm))






# 2) Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

emty_list = []

itm = 1
while itm < 7:
    input_list = input(f'Вы ввели значения списка {itm} раз(a)\n')
    itm += 1
    emty_list.append(input_list)

print(f'Так выглядит список после записи {emty_list}')

# while itm > len(emty_list):
#     itm = 0
#     emty_list.insert(itm, emty_list[itm + 1])
#     emty_list.pop(itm + 2)
#     itm += 2

emty_list.insert(0, emty_list[1])
emty_list.pop(2)
emty_list.insert(2, emty_list[3])
emty_list.pop(4)
emty_list.insert(4, emty_list[5])
emty_list.pop(6)

print(f'А так после обмена значений {emty_list}')







# 3) Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

while True:
    month = input('Введите месяц в виде целого числа\n')
    if month.isdigit():
        month = int(month)
        break
    else:
        print('Введите число!')

seasons = {
    1: 'зима',
    2: 'зима',
    3: 'весна',
    4: 'весна',
    5: 'весна',
    6: 'лето',
    7: 'лето',
    8: 'лето',
    9: 'осень',
    10: 'осень',
    11: 'осень',
    12: 'зима',
    # 'зима': [12, 1, 2],
    # 'весна': [3, 4, 5],
    # 'лето': [6, 7, 8],
    # 'осень': [9, 10, 11],
}


print(seasons.get(month))



# 4)Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

line = input('Введите строку из нескольких слов, разделенных пробелами\n')

result = line.split(' ')
result = list(result)

for itm, number in enumerate(result, 1):
    print(itm, number[:10])





# 5) Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

my_list = [7, 5, 3, 3, 2]
print(my_list)

while True:
    number = input('Введите новый элемент рейтинга\n')
    if number.isdigit():
        number = int(number)
        break
    else:
        print('Введите число')

for itm in my_list:
    if itm == number:
        idx = my_list.index(itm)
        my_list.insert(idx, number)
        break
    elif itm < number:
        my_list.insert(0, number)
        break
    elif itm != number:
        my_list.append(number)
        break

my_list.sort(reverse=True)
print(my_list)



# 6) *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
#     (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#     (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#     (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь,
# в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
#     “название”: [“компьютер”, “принтер”, “сканер”],
#     “цена”: [20000, 6000, 2000],
#     “количество”: [5, 2, 7],
#     “ед”: [“шт.”]
# }

goods = (1, {
    'название': '',
    'цена': '',
    'количество': '',
    'ед': '',
})


print(goods)
for keys in goods[1]:
    new = input('Заполните данный словарь значениями\n')
    if new.isdigit():
        new = int(new)
    elif new.isdecimal():
        new = float(new)
    goods[1][keys] = new


goods_1 = (2, {
    'название': '',
    'цена': '',
    'количество': '',
    'ед': '',
})


print(goods_1)
for keys in goods_1[1]:
    new = input('Заполните следующий похожий словарь \n')
    if new.isdigit():
        new = int(new)
    elif new.isdecimal():
        new = float(new)
    goods_1[1][keys] = new


goods_2 = (3, {
    'название': '',
    'цена': '',
    'количество': '',
    'ед': '',
})


print(goods_2)
for keys in goods_2[1]:
    new = input('Заполните и еще один похожий словарь \n')
    if new.isdigit():
        new = int(new)
    elif new.isdecimal():
        new = float(new)
    goods_2[1][keys] = new


print(f'{goods}\n{goods_1}\n{goods_2}\n')

analytics = {}

analytics.update(goods[1])

for keys in analytics:
    analytics[keys] = []

for keys in goods[1]:
    result = goods[1].get(keys)
    analytics[keys].append(result)

for keys in goods_1[1]:
    result = goods_1[1].get(keys)
    analytics[keys].append(result)

for keys in goods_2[1]:
    result = goods_2[1].get(keys)
    analytics[keys].append(result)

print(analytics)

