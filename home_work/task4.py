# 4. Создать (не программно) текстовый файл со следующим содержимым:
#
# One — 1
#
# Two — 2
#
# Three — 3
#
# Four — 4
#
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

transfer = {
    'One ': 'Один',
    'Two ': 'Два',
    'Three ': 'Три',
    'Four ': 'Четыре',
    'Five ': 'Пять',
    'Six ': 'Шесть',
    'Seven ': 'Семь',
    'Eight ': 'Восемь',
    'Nine ': 'Девять',
    'Ten ': 'Десять',

}

with open('score.txt', 'r') as out_file:
    new_list = []
    for itm in out_file:
        result = number, score = itm.split('- ')
        new_list.append(result)

    for itm in new_list:
        england, numb = itm[0], itm[1]
        russian = transfer.get(england)
        itm.remove(england)
        itm.insert(0, russian)
        itm.insert(1, ' - ')

with open('rus_score.txt', 'w') as rus_file:
    for i in range(len(new_list)):
        rus_file.writelines(new_list[i])
