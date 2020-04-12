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