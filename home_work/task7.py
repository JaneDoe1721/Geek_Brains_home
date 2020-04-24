# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
#
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
#
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
#
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
#
# Пример json-объекта:
#
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.
import re
import json

number = sum(1 for line in open('firms.txt', 'r'))

Pattern = re.compile(r'-?\d+')

with open('firms.txt', 'r') as File:
    profit = []
    loss = []

    for i in range(number):
        lst = [int(x) for x in re.findall(Pattern, File.readline())]
        result = lst[0] - lst[1]
        if result < 0:
            loss.append(result)
        else:
            profit.append(result)

with open('firms.txt', 'r') as out_file:
    firms = []
    for line in out_file:
        subject, numb = line.split(':')
        firms.append(subject)

average = [sum(profit) / len(profit)]
average_profit = ['average profit']

content = dict(zip(firms, profit))
content_average = dict(zip(average_profit, average))

summary_list = []

summary_list.append(content)
summary_list.append(content_average)

with open('summary_list.json', 'w') as f:
    json.dump(summary_list, f)
