# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().
from functools import reduce

list_of_number = [el for el in range(99, 1001) if not el & 1]
sum_numbers = reduce(lambda x, y: x * y, list_of_number)
print(sum_numbers)
