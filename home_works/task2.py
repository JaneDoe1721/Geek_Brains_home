# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Dress(ABC):

    def __init__(self, size: int, height: int):
        self.size = size
        self.height = height


    @abstractmethod
    def fabric_on_coat(self, size: int) -> float:
        pass

    @abstractmethod
    def fabric_for_costume(self, height: int) -> float:
        pass

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size):
        if size < 40:
            self.__size = 40
        elif size > 62:
            self.__size = 62
        else:
            self.__size = size


class Coat(Dress):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def fabric_on_coat(self, *args, **kwargs) -> float:
        result = self.size / 6.5 + 0.5
        return result

    def fabric_for_costume(self, height: int) -> float:
        pass


class Costume(Dress):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def fabric_on_coat(self, size: int) -> float:
        pass

    @property
    def fabric_for_costume(self, *args, **kwargs) -> float:
        return (2 * self.height + 0.3) / 100


c = Coat(48, 176)
print(f'Ткани на пальто: {c.fabric_on_coat:.3f}')
cost = Costume(48, 176)
print(f'Ткани на костюм: {cost.fabric_for_costume:.3f}')
result = c.fabric_on_coat + cost.fabric_for_costume
print(f'Общее колличество ткани: {result:.3f} метров')
