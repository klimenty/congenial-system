name = str(input('Введите ваше имя'))
surname = str(input('Введите вашу фамилию'))
age = int(input('Введите ваш возраст'))
weight = int(input('Введите ваш вес'))
good = str('хорошее состояние.')
normal = str('следует заняться собой.')
bad = str('следует обратиться к врачу!')
other = str('у вас плохой день.')
status = name, surname, age, 'год, вес', weight

if age <= 30:
    if 50 <= weight <= 120:
        print(status, good)
    else:
        print(status, other)
elif age > 40:
    if weight < 50 or weight > 120:
        print(status, bad)
    else:
        print(status, other)
elif age > 30:
    if weight < 50 or weight > 120:
        print(status, normal)
    else:
        print(status, other)
else:
    print(status, other)