# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.
import time


class TrafficLight:
    __color = ''

    def running(self, color):
        count = 0
        while True:
            if color == 'Red':
                self.__color = color
                print(f'Загорелся красный свет: {self.__color}')
                for i in range(1, 8):
                    time.sleep(1)
                    print(i)
                self.__color = 'Yellow'
                print(f'Загорелся желтый свет: {self.__color}')
                for i in range(1, 3):
                    time.sleep(1)
                    print(i)
                self.__color = 'Green'
                print(f"Загорелся зеленый свет: {self.__color}")
                for i in range(1, 6):
                    time.sleep(1)
                    print(i)
            elif color == 'Yellow' or 'Green':
                print('Ошибка, начало цикла с Red')
                break
            count += 1
            if count == 3:
                break


a = TrafficLight()
a.running('Red')
