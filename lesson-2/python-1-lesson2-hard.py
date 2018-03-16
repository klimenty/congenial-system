# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.
#
#equation = 'y = -12x + 11111140.2121'
#x = float(2.5)
#
#lst1 = equation.split(' ')
#kx = lst1[2]
#k = float(kx[:-1])
#b = float(lst1[4])
#kx = k * x
#y = kx + b
#
#print('y = ' + str(y))

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)
#
# date = str(input('Пожалуйста, введите дату в формате dd.mm.yyyy:'))
# day, month, year = date.split('.')
# day_31 = [1, 3, 5, 7, 8, 10, 12]
# day_30 = [2, 4, 6, 9, 12]
#
# if (int(day) in range(1, 32) and int(month) in day_31) or \
#         (int(day) in range(1, 31) and int(month) in day_30)\
#         and int(month) in range(1, 13) and int(year) in range(1, 10000)
#     if len(day) == 2 and len(month) == 2 and len(year) == 4:
#         print(str(day) + '.' + str(month) + '.' + str(year))
#     else:
#         print('Дата должна иметь вид dd.mm.yyyy. Например: 01.01.0001.')
# else:
#     print('Задана неверная дата.')
# Да, это копипаст из normal
#
# Задание-3
#
input_room_number = int(input('Пожалуйса, введите номер комнаты:'))
level = [[]]
room = []
for level_number in level:
    room.append(count(level) ** count(level))
    if level_number == input_room_number:
        print(input_room_number)
    else:


