'''
Задание 2
Допустим, какая-то программа возвращает результат своей работы в таком виде:

результат операции: 42

результат операции: 514

результат работы программы: 9

С помощью срезов и метода index получите из каждой строки с результатом число,
прибавьте к полученному числу 10, результат сложения распечатайте.
'''

RESALT_1 = "результат операции: 42"
RESALT_2 = "результат операции: 514"
RESALT_3 = "результат работы программы: 9"

print(int(RESALT_1[RESALT_1.index(":") + 2:]) + 10)  # Выводим результат

print(int(RESALT_2[RESALT_2.index(":") + 2:]) + 10)  # Выводим результат

print(int(RESALT_3[RESALT_3.index(":") + 2:]) + 10)  # Выводим результат
