# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться
# с ошибкой.


class AnyError(Exception):

    def __init__(self, text):
        self.text = text


while True:
    number = input("Введите число: \n")

    try:
        number = int(number)
        if number == 0:
            raise AnyError("Деление на ноль запрещено!")
        result = 5 / number
    except ValueError:
        print("Надо ввести число!")
    except AnyError as er:
        print(er)
    else:
        print(result)
        break
