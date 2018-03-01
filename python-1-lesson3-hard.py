# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.
#
# player = {'health': 100, 'damage': 50}
# enemy = {'health': 120, 'damage': 25, 'name': 'giant_rat'}
# player['name'] = input('Введите имя персонажа:')
#
#
# def attack(person1, person2):
#         person2['health'] -= person1['damage']
#
#
# attack(player, enemy)
# print(player, enemy)

# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.

player = {'health': 100, 'damage': 50, 'armor': 1.2}
enemy = {'health': 120, 'damage': 25, 'name': 'giant_rat', 'armor': 1.2}
player['name'] = input('Введите имя персонажа:')
characters_list = [player, enemy]


def damage_with_armor(damage, armor):
    return int(damage / armor)


def attack(person1, person2):
        person2['health'] -= damage_with_armor(person1['damage'],
                                               person2['armor'])


for character in characters_list:
    file_name = character.get('name') + '.txt'
    with open(file_name, 'w', encoding='UTF-8', ) as file:
        for key, item in character.items():
            file.write('{} - {}'.format(key, item) + '\n')

for character in characters_list:
    file_name = character.get('name') + '.txt'
    with open(file_name, 'r', encoding='UTF-8') as file:
    strings = list(file.readlines())
    for line in strings:
        character = dictline.split(' - ')
#
# attack(player, enemy)
print(player, enemy)
if damage_dealer == 'stop' or attacked_unit == 'stop':
    print('Итоги схватки. Игрок: {} Противник: {}'.format(player, enemy))
    break
elif damage_dealer == player.get('name') and attacked_unit == enemy.get('name'):
    person1 = player
    person2 = enemy
elif damage_dealer == enemy.get('name') and attacked_unit == player.get('name')

else:
        attack(damage_dealer, attacked_unit)
        continue
