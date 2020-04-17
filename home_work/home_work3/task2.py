# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.


def info(name, surname, date, city, email, tel):
    '''

    :param name: str
    :param surname: str
    :param date: int
    :param city: str
    :param email: str
    :param tel: int
    :return:
    '''

    run = (f'Имя:{name}, Фамилия:{surname}, Год рождения:{date}, Родной город:{city}, Email:{email}, Телефон:{tel}')
    return run


result = info(name='ilya', surname='burc', date=12, city='City', email='ilyabit', tel=5889595)
print(result)
