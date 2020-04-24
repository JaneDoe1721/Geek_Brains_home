# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

try:
    with open('collaborator', 'r') as out_file:
        result = []
        for itm in out_file:
            name, salary = itm.split(' ')
            salary = int(salary)
            if salary < 20000:
                print(name)
            result.append(salary)
except IOError:
    print('Ошибка ввода-вывода')

average_salary = sum(result) / len(result)
print(f'средняя зарплата равна: {average_salary}')
