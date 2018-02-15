# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"
#
# def user():
#     name = input('Введите имя:')
#     age = int(input('Введите возраст:'))
#     city = input('Введите место жительства:')
#     result_string = '{}, {} год(а), проживает в городе {}'.format(
#         name, age, city)
#     return result_string
# print(user())

# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них
#
# def max_input_number():
#     input_numbers = []
#     while len(input_numbers) < 3:
#         input_numbers.append(int(input('Введите число:')))
#     max_number = max(input_numbers)
#     return max_number
# print(max_input_number())

# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов
#
# def input_string():
#     input_strings = []
#     while 'end' not in input_strings:
#         input_strings.append(input('Введите строку. '
#                                    'Для завершения введите "end":'))
#     input_strings.remove('end')
#     max_string = max(input_strings, key=len)
#     return max_string
# print(input_string())