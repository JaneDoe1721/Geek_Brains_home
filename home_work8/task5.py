# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.


class ComplexNumber:

    def __init__(self, number: complex):
        self.number = number

    def __add__(self, other):
        result = self.number + other.number
        return result

    def __mul__(self, other):
        result = self.number * other.number
        return result


a = ComplexNumber(1 + 2j)
b = ComplexNumber(2 + 3j)
c = a * b
print(c)
