# задание номер 1

print('Сейчас будет небольшой опрос')

name = input('Как вас зовут?\n')
age = input('Укажите сколько вам лет\n')
city = input('Введите город, в которов проживаете\n')
strength = input('Какя численность населения вашего города?\n')

print(f'{name}, {age}, {city}, {strength}')

# задание номер 2

while True:
    time = input('Укажите время в секундах\n')
    if time.isdigit():
        time = int(time)
        break
    else:
        print('Ошибка ввода, введите число!')

hour = time // 3600
minute = (time - hour * 3600) // 60
second = time % 60

print(f'Время {hour:>02}:{minute}:{second}')

# задание номер 3
while True:
    number = input('Введите число\n')
    if number.isdigit():
        number = int(number)
        break
    else:
        print('Вы ввели не число!')
n = number
nn = n + n
nnn = nn + n
sum = n + nn + nnn

print(sum)

# задание номер 4

while True:
    number = input('Введите целое положительное число\n')
    if number.isdigit():
        number = int(number)
        break
    else:
        print('Ошибка, нужно число!')


# находим последнюю цифру
maxi = number % 10
# избавляемся от последней цифры
number = number // 10

while number > 0:
    if number % 10 > maxi:
        maxi = number % 10
    number = number // 10
print(f'Максимальное число: {maxi}')

# задание номер 5
while True:
    proceeds = input("Введите значение выручки($):\n")
    cost = input("Введите значения расходов($):\n")
    if proceeds.isdigit() and cost.isdigit():
        proceeds = int(proceeds)
        cost = int(cost)
        break
    else:
        print('Введите число!')

if proceeds > cost:
    print('Фирма работает в прибыль!')
    profit = proceeds - cost
    profitability = profit / proceeds * 100
    print(f'Рентабильность выручки состовляет: {profitability:.3f} %')
    while True:
        employee = input('Сообщите численность сотрудников фирмы:\n')
        if employee.isdigit():
            employee = int(employee)
            break
        else:
            print('Введите число!')
    proceeds_employee = profit / employee
    print(f'Прибыль фирмы в расчете на одного сотрудника: {proceeds_employee:.3f} $')

else:
    print('Фирма работает в убыток!')


# задание номер 6

while True:
    user_a = input('Введите целое число результата в первый день:\n')
    user_b = input('Введите конечный результат:\n')
    if user_a.isdigit() and user_b.isdigit():
        user_a = int(user_a)
        user_b = int(user_b)
        break
    else:
        print('Ошибка ввода')


distance = user_a
days = ''
i = 1
print(f'{i}-й день: {user_a} км')

while True:
    if distance < user_b:
        distance *= 1.1
        i += 1
        days = f'{i}-й день'
        print(f'{days}: {distance:.2f} км')
    elif distance > user_b:
        print(f'На {days} спортсмен достиг результата - не менее {user_b} км!')
        break


