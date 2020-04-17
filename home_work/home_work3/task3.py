# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    """

    :param a: int
    :param b: int
    :param c: int
    :return: int
    """
    list = []
    list.append(a)
    list.append(b)
    list.append(c)
    result = min(a, b, c)
    list.remove(result)
    total = sum(list)

    return total


print(my_func(0, 1, 6))
