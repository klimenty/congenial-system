# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

# import random
# lst = [random.randint(0, 100)**2 for _ in range (10)]
# print(lst)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
#
# fruits_list1 = ['apple', 'banana', 'orange']
# fruits_list2 = ['banana', 'apple', 'kiwi']
# fruits = [fruit for fruit in fruits_list1 if fruit in fruits_list2]
# print(fruits)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

# import random
# random_numbers_list = [random.randint(-100, 100) for _ in range(50)]
# final_numbers_list = [number for number in random_numbers_list
#                       if number % 3 == 0 and number >= 0 and number % 4 != 0]
# print(final_numbers_list)
