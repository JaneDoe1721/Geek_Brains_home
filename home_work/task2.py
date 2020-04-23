# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('new.txt', 'r') as out_file:
    i = 0
    for line in out_file:
        new_list = line.split(' ')
        num = len(new_list)
        print(new_list)
        print(f'В данной строке, колличсетво слов: {num}')
        i += 1

print(f'\nКолличество строк: {i}')

