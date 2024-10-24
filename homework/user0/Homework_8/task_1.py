'''
Задание 1
Напишите программу. Есть две переменные, salary и bonus.
Salary - int, bonus - bool. Спросите у пользователя salary.
А bonus пусть назначается рандомом.

Если bonus - true, то к salary должен быть добавлен рандомный бонус.

Примеры результатов:

10000, True - '$10255'
25000, False - '$25000'
600, True - '$3785'

'''

import random

salary = int(input('Введите зарплату: '))
bonus = random.choice([True, False])

if bonus:
    bonus_percentage = random.randint(1, 20)
    bonus_amount = salary * (bonus_percentage / 100)
    total_salary = int(salary + bonus_amount)
else:
    total_salary = salary

print(f'{salary}, {bonus} - \'${total_salary}\'')
