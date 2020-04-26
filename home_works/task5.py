# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:
    title = ''

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def draw(self):
        print(f'{self.title} : Можно рисовать, но используеться для записей')


class Pencil(Stationery):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def draw(self):
        print(f'{self.title} : Используеться для рисования')


class Handle(Stationery):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def draw(self):
        print(f'{self.title} : Используеться для рисования, но аккуратно')


pen = Pen('pen')
pen.draw()

pencil = Pencil('pencil')
pencil.draw()

handle = Handle('handle')
handle.draw()

pen_1 = Stationery('pen_1')
pen_1.draw()