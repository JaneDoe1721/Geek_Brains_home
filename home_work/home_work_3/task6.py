# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

def int_func(str):
    """

    :param str: str
    :return: str
    """
    result = str.title()
    return result


print(int_func(input('Введите слово в нижнем регистре\n')))


def new(str):
    """

    :param str: str
    :return: str
    """
    result = str.split(' ')
    new_list = []
    for itm in result:
        total = int_func(itm)
        new_list.append(total)
    new_string = ' '.join(new_list)
    return new_string


print(new(input('Введите строку в нижнем регистре разделенную пробелами\n')))
