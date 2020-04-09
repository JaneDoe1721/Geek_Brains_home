# задание номер 1

print('Сейчас будет небольшой опрос')

name = input('Как вас зовут?\n')
age = input('Укажите сколько вам лет\n')
city = input('Введите город, в которов проживаете\n')
strength = input('Какя численность населения вашего города?\n')

print(f'{name}, {age}, {city}, {strength}')

# задание номер 2

time = input('Укажите время в секундах\n')

time = int(time)
hour = time // 3600
minute = (time - hour * 3600) // 60
second = time % 60

print(f'Время {hour:>02}:{minute}:{second}')

# задание номер 3

number = input('Введите число\n')
n = number
nn = n + n
nnn = nn + n
sum = int(n) + int(nn) + int(nnn)

print(sum)

# задание номер 4

number = input('Введите целое положительное число\n')
number = int(number)
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

proceeds = input("Введите значение выручки($):\n")
cost = input("Введите значения расходов($):\n")
proceeds = int(proceeds)
cost = int(cost)

if proceeds > cost:
    print('Фирма работает в прибыль!')
    profit = proceeds - cost
    profitability = profit / proceeds * 100
    print(f'Рентабильность выручки состовляет: {profitability:.3f} %')
    employee = input('Сообщите численность сотрудников фирмы:\n')
    employee = int(employee)
    proceeds_employee = profit / employee
    print(f'Прибыль фирмы в расчете на одного сотрудника: {proceeds_employee:.3f} $')

else:
    print('Фирма работает в убыток!')

# задание номер 6

a = 3
b = 5
percent = a * 0.1
distance = a + percent
days = ''
i = 1
print(f'{i}-й день: {a} км')

while True:
    if distance < b:
        i += 1
        days = f'{i}-й день'
        print(f'{days}: {distance:.2f} км')
        distance += percent
    elif distance > b:
        print(f'На {days} спортсмен достиг результата - не менее {b} км!')
        break