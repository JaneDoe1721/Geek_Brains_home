# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

new_list = [1, 2.2, 'str', False, True, None]


# попытка ввести значения через input, Проблема с проверками на типы bool n NoneType
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
