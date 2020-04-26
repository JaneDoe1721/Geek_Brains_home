# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда)
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


class Car:
    speed = 50
    color = 'grey'
    name = ''
    is_police = False

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость : {self.speed}')


class TownCar(Car):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def show_speed(self):
        if self.speed > 60:
            print(f'{self.speed} Превышение скорости! Сбавте скорость до 60')


class WorkCar(Car):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def show_speed(self):
        if self.speed >= 40:
            print(f'{self.speed} Превышение скорости! Сбавте скорость до 40')


class PoliceCar(Car):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class SportCar(Car):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


ferari = SportCar(speed=300, color='red', name='Ferari', is_police=False)
print(f'SportCar : {ferari.name}, {ferari.color}, {ferari.speed} км/ч, {ferari.is_police}')
ferari.go()
ferari.turn('направо')
ferari.turn('налево')
ferari.show_speed()


ford = PoliceCar(name='Ford', color='grey', speed=150, is_police=True)
print(f'PoliceCar : {ford.name}, {ford.color}, {ford.speed} км/ч, {ford.is_police}')
ford.go()
ford.turn('налево')
ford.stop()
ford.show_speed()

kamaz = WorkCar(name='Kamaz', color='black', speed=40, is_police=False)
print(f'WorkCar : {kamaz.name}, {kamaz.color}, {kamaz.speed} км/ч, {kamaz.is_police}')
kamaz.go()
kamaz.stop()
kamaz.show_speed()

bus = TownCar(name='Bus', color='Yellow', speed=70, is_police=False)
print(f'TownCar : {bus.name}, {bus.color}, {bus.speed} км/ч, {bus.is_police}')
bus.go()
bus.turn('направо')
bus.turn('налево')
bus.turn('направо')
bus.turn('направо')
bus.stop()
bus.show_speed()