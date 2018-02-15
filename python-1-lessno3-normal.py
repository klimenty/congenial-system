# # Задание - 1
# # Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# # вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# # Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# # столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# # После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# # Есть условие, не отображать людей получающих более зарплату 500000, как именно
# #  выполнить условие решать вам, можете не писать в файл
# # можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
# #  если скажем эти файлы потом придется передавать.
# # Так же при выводе имя должно быть полностью в верхнем регистре!
# # Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.
#
name_input = ['Василий Васильевич', 'Иван Иванов', 'Алексей Алексеевич']
salary_input = [20000, 100000, 550000]
def salary_less_than_500000():
    name = []
    salary = []
    i = 0
    for value in salary_input:
        if value <= 500000:
            salary.append(salary_input[i])
            name.append(name_input[i])
            i += 1
        else:
            i += 1
    employers_salary = dict(zip(name, salary))
    return employers_salary

emp_list = []
emp_dict = salary_less_than_500000()
for key, value in emp_dict.items():
    emp_list.append('{} - {}'.format(key, value))

with open('file.txt', 'w', encoding='utf=8') as file:
    for item in emp_list:
        file.write('{}\n'.format(item))

with open('file.txt', 'r', encoding='utf=8') as file:
    file_srting = file.read()
    file_srting = file_srting.split('\n')

for value in file_srting:
    if len(value) > 1:
        value_temp = value.split(' - ')
        emp_name = value_temp[0]
        emp_name = emp_name.upper()
        emp_salary = int(float(value_temp[1]) * 0.87)
        print('{} - {}'.format(emp_name, emp_salary))
    else:
        continue
