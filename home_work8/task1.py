# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц,
# год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


class Data:

    def __init__(self, data: str):
        self.data = data

    @classmethod
    def cls_numbers(cls, data):
        day, month, year = map(int, data.split('-'))
        return f'День: {day} - Месяц: {month} - Год: {year}'

    @staticmethod
    def validator(data):
        day, month, year = map(int, data.split('-'))
        return f'День соответствует условиям? {day > 0}, Месяц соответсвует условиям? {month <= 12 and month > 0}, Год соответсвует условиям? {year > 0}'


d = Data.cls_numbers('11-12-1993')
f = Data.validator('10-10-2010')
print(d)
print(f)
