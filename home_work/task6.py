# 6. Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
#
# Примеры строк файла:
#
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря:
#
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
import re

with open('objects.txt', 'r') as out_file:
    result = []
    for line in out_file:
        subject, numb = line.split(':')
        result.append(subject)

Pattern = re.compile(r'-?\d+')


def foo():
    with open('objects.txt', 'r') as File:
        lst = [int(x) for x in re.findall(Pattern, File.readline())]
        lst_2 = [int(x) for x in re.findall(Pattern, File.readline())]
        lst_3 = [int(x) for x in re.findall(Pattern, File.readline())]
        return sum(lst), sum(lst_2), sum(lst_3)


effect = foo()

content = dict(zip(result, effect))

print(content)
