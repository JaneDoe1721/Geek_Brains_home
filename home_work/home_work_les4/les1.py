#
# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
from sys import argv

_, production_hour, rate_hour, the_prize = argv

try:
    print('Зарплата без премии', int(production_hour) * int(rate_hour))
    print('Зарплата с премией', (int(production_hour) * int(rate_hour)) + int(the_prize))
except ValueError as e:
    print('Ошибка')
    print(e)
