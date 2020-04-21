# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
from sys import argv

# def wages(production_hourse:int, rate_hour:int, the_prize:int):
#     return (production_hourse * rate_hour) + the_prize


script_name, production_hourse, rate_hour, the_prize = argv
print('Зарплата без премии', int(production_hourse) * int(rate_hour))
print('Зарплата с премией', (int(production_hourse) * int(rate_hour)) + int(the_prize))
