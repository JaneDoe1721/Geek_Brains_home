# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {'salary': 0, 'bonus': 0}

    def __init__(self, name: str, surname: str, position: str, salary, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income['salary'] = salary
        self._income['bonus'] = bonus


class Position(Worker):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_full_name(self):
        print(f'Полное имя, фамилия сотрудника: {self.name} {self.surname}')

    def get_total_income(self):
        result = self._income['salary'] + self._income['bonus']
        print(f'Зарплата со всеми премиальными: {result} руб')


security = Position(name='Ivan', surname='Pupkin', position='security', salary=20000, bonus=5000)

print(security.position)
security.get_full_name()
security.get_total_income()
