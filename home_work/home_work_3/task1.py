# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def new_number(x, y):
    '''
    :param x: int
    :param y: int
    :return: int
    '''
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        print("Происходит деление на ноль")


result = new_number(5, 2)
print(result)
