# 4)Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

line = input('Введите строку из нескольких слов, разделенных пробелами\n')

result = line.split(' ')
result = list(result)

for itm, number in enumerate(result, 1):
    print(itm, number[:10])