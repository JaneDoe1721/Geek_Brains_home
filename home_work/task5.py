# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
try:
    with open('numbers.txt', 'w') as out_file:
        set_of_numbers = ['1 ', '2 ', '3 ', '5 ', '6 ', '7 ', '8 ', '3 ', '9']
        out_file.writelines(set_of_numbers)

except IOError:
    print('Ошибка ввода-вывода')

try:
    with open('numbers.txt', 'r') as out_file:
        result = out_file.readlines()
        split_num = result[0].split(' ')
        finally_list = []
        for itm in split_num:
            finally_list.append(int(itm))

        print(f'Сумма: {sum(finally_list)}')

except IOError:
    print('Ошибка ввода-вывода')
