# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

# def my_func(x, y):
#     '''
#
#     :param x: float
#     :param y: int
#     :return: float
#     '''
#     result = x ** y
#     return result
#
#
# total = my_func(-3.2, -2)
# print(round(total, 3))

from functools import reduce


def my_func(x: float, y: int):
    result = 1
    for _ in range(abs(y)):
        result *= x
    return result if y >= 0 else 1 / result



# немного програйминг извращений
# никогда так не делайте lambda созданы не для этого это читаеться ужасно, и вообще зачем?
my_func2 = lambda x, y: reduce(
    lambda a, b: a * b,
    [x for _ in range(abs(y)) or [1]]
) if y > 0 else 1 / reduce(
    lambda a, b: a * b, [x for _ in range(abs(y))] or [1]
)



if __name__ == '__main__':
    assert my_func(2, 2) == 2 ** 2, 'my_func(2, 2)'
    assert my_func(3, 3) == 3 ** 3, 'my_func(3, 3)'
    assert my_func(3, -5) == 3 ** -5, 'my_func(3, -5)'
    assert my_func(3, 0) == 3 ** 0, 'my_func(3, 0)'

    assert my_func2(2, 2) == 2 ** 2, 'my_func(2, 2)'
    assert my_func2(3, 3) == 3 ** 3, 'my_func(3, 3)'
    assert my_func2(3, -5) == 3 ** -5, 'my_func(3, -5)'
    assert my_func2(3, 0) == 3 ** 0, 'my_func(3, 0)'

    print(my_func(2, -2))