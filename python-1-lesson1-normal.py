#Задание-1
while True:
  number = int(input('Пожалуйста, введите число'))
  if 0 <= number <= 10:
      number = number ** 2
      print(number)
      break
  else:
      print('Число не отвечает заданным требованиям. Пожалуйста, введите число'
          ' от 0 до 10')


#Задание-2
a = int(input('Введите значение А'))
b = int(input('Введите значение B'))

a = a + b
b = a - b
a = a - b
print(a, b)