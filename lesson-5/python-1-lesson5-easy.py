# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
# import os


# def make_dir():
#     '''Make directory with name dir_name in script location directory'''
#     if not dir_name:
#         print('Необходимо указать имя директории')
#         return
#     dir_path = os.path.join(os.getcwd(), dir_name)
#     try:
#         os.mkdir(dir_path)
#         print('Директория {} успешно создана.'.format(dir_name))
#     except FileExistsError:
#         print('Директория {} уже существует.'.format(dir_name))


# def remove_dir():
#     '''Remove directory with name dir_name in script location directory'''
#     if not dir_name:
#         print('Необходимо указать имя директории')
#         return
#     dir_path = os.path.join(os.getcwd(), dir_name)
#     try:
#         os.rmdir(dir_path)
#         print('Директория {} успешно удалена.'.format(dir_name))
#     except FileNotFoundError:
#         print('Директория {} не найдена.'.format(dir_name))
#
#
# dir_number = 1

# while dir_number < 10:
#     '''Make dir_1-dir_9 directories'''
#     dir_name = 'dir_{}'.format(dir_number)
#     make_dir()
#     dir_number += 1

# while dir_number < 10:
#     '''Remove dir_1-dir_9 directories'''
#     dir_name = 'dir_{}'.format(dir_number)
#     remove_dir()
#     dir_number += 1

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
# import os
#
# print(os.listdir())


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import sys


def copy_source_file():
    '''Copy file'''
    filename = sys.argv[0]
    with open(filename, 'r', encoding='UTF-8') as file:
        strings = list(file.readlines())
    filename = filename.partition('.')
    with open('{}_copy{}{}'.format(filename[0], filename[1], filename[2]), 'w',
                                   encoding='UTF-8') as file:
        for lines in strings:
            file.write('{}'.format(lines))