# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.

# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.
from abc import ABC, abstractmethod


class AnyError(Exception):

    def __init__(self, text):
        self.text = text


class Storage(ABC):
    _storage_places = 100
    free_place = 100
    occupied_place = 0
    heated = True

    def __init__(self, places: int, heated: bool):
        self.occupied_place = places
        self.heated = heated

    @classmethod
    def expansion(cls):
        return cls._storage_places + 50

    @staticmethod
    def stock_price():
        for_a_place = 5
        total = Storage._storage_places * for_a_place
        return f'Цена за все места на складе: {total}'

    @abstractmethod
    def reception(self):
        try:
            if isinstance(self.occupied_place, str):
                raise AnyError('Тут нужно число, а не строка!')
            if self.occupied_place >= self.free_place:
                raise AnyError('Недостаточно места на складе!')
        except AnyError as er:
            return er
        else:
            total = self.free_place - self.occupied_place
            return f'Поступило: {self.occupied_place}, Еще свободного места на складе: {total}'


class OfficeEquipment:
    price = 500
    connect = 'USB'
    material = 'plastic'
    _connection_speed = 100

    def __init__(self, price: int, name: str, connect: str, material: str):
        self.price = price
        self.connect = connect
        self.material = material
        self.name = name

    def work(self):
        if self.connect == 'USB':
            return self._connection_speed
        elif self.connect == 'Wi-Fi':
            return f'Коннект через Wi- Fi помедленнее: {self._connection_speed - 30}'


class Printer(OfficeEquipment, Storage):

    def __init__(self, places, heated, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Storage.__init__(self, places, heated)

    def delivery(self, places: int):
        if places <= self.occupied_place:
            total = self.occupied_place - places
            print(f'Передача товара в компанию со склада в подразделение для принтеров: {places}')
            return f'Осталось товара на складе: {total}'
        else:
            print('Недостаточно товара на складе')

    def reception(self):
        try:
            if isinstance(self.occupied_place, str):
                raise AnyError('Тут нужно число, а не строка!')
            if self.occupied_place >= self.free_place:
                raise AnyError('Недостаточно места на складе!')
        except AnyError as er:
            return er
        else:
            total = self.free_place - self.occupied_place
            return f'Поступило: {self.occupied_place}, Еще свободного места на складе Принтеров: {total}'


class Scanner(OfficeEquipment, Storage):

    def __init__(self, places, heated, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Storage.__init__(self, places, heated)

    def delivery(self, places: int):
        if places <= self.occupied_place:
            total = self.occupied_place - places
            print(f'Передача товара в компанию со склада в подразделение для сканнеров: {places}')
            return f'Осталось товара на складе: {total}'
        else:
            print('Недостаточно товара на складе')

    def reception(self):
        try:
            if isinstance(self.occupied_place, str):
                raise AnyError('Тут нужно число, а не строка!')
            if self.occupied_place >= self.free_place:
                raise AnyError('Недостаточно места на складе!')
        except AnyError as er:
            return er
        else:
            total = self.free_place - self.occupied_place
            return f'Поступило: {self.occupied_place}, Еще свободного места на складе сканнеров: {total}'

    @property
    def work(self):
        if self.connect == 'USB':
            return self._connection_speed
        elif self.connect == 'Wi-Fi':
            return f'Коннект через Wi- Fi помедленнее: {self._connection_speed - 30}'


class Xerox(OfficeEquipment, Storage):

    def __init__(self, places, heated, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Storage.__init__(self, places, heated)

    def delivery(self, places: int):
        if places <= self.occupied_place:
            total = self.occupied_place - places
            print(f'Передача товара в компанию со склада в подразделение для хсероксов: {places}')
            return f'Осталось товара на складе: {total}'
        else:
            print('Недостаточно товара на складе')

    def reception(self):
        try:
            if isinstance(self.occupied_place, str):
                raise AnyError('Тут нужно число, а не строка!')
            if self.occupied_place >= self.free_place:
                raise AnyError('Недостаточно места на складе!')
        except AnyError as er:
            return er
        else:
            total = self.free_place - self.occupied_place
            return f'Поступило: {self.occupied_place}, Еще свободного места на складе ксероксов: {total}'


p = Printer(name='printer', price=400, connect='USB', material='plastic', places=50, heated=True)
s = Scanner(name='scanner', price=500, connect='Wi-Fi', material='titanium', places=70, heated=True)
x = Xerox(price=300, connect='USB', material='metal', places=30, heated=False, name='xerox')
print(x.delivery(30))
print(p.reception())
print(p.__dict__)
print(s.__dict__)
print(x.__dict__)
print(s.work)
print(s.expansion())
