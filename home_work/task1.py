# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

str_list = []
for itm in range(3):
    str_list.append(input("Введите данные\n"))
    str_list.append('\n')

with open('new_file.txt', 'w') as out_file:
    out_file.writelines(str_list)

