# Задача-1
#
# list_1 = [1, 9, 6, 7, 45, 15, 84, 265, 983, 6873, 87, 73, 432, 862, 76324, 2,
#          -5, 8, 9, -25, 25, 4]
# list_2 = []
# for number in list_1:
#    number = number ** 0.5
#    if number % 1 == 0:
#        list_2.append(number)
#    else:
#        break
#
# print(list_2)

# Задача-2
#date = str(input('Пожалуйста, введите дату в формате dd.mm.yyyy:'))
#days = {"1": "первое", "2": "второе", "3": "третье", "4": "четвертое",
#        "5": "пятое", "6": "шестое", "7": "седьмое", "8": "восьмое",
#        "9": "девятое", "10": "десятое"}
# Дальше заполнять словарь дней было лень
#months = {"1": "января", "2": "февраля", "3": "марта", "4": "апреля",
#          "5": "мая", "6": "июня", "7": "июля", "8": "августа",
#          "9": "сентября", "10": "октября", "11": "ноября", "12": "декабря"}
#day, month, yyyy = date.split('.')
#
#if int(day) in range(1, 32) and int(month) in range(1, 13)\
#        and int(yyyy) in range(1, 9999):
#    print(days[day] + ' ' + months[month] + ' ' + yyyy + ' года')
#else:
#    print('Задана неверная дата.')

# Задача-3
#
# import random
# i = 0
# n = random.randint(1, 20)
# list = []
#
# while i <= n:
#    list.append(random.randint(-100, 100))
#    i += 1
# print(list)

# Задача-4

#lst = [1, 2, 4, 5, 6, 2, 5, 2]
#lst2 = list(set(lst))
#lst3 = []
#
#for x in lst:
#    if lst.count(x) == 1:
#        lst3.append(x)
#    else:
#        continue
#
#print(lst2)
#print(lst3)
