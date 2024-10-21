'''
Задание №3
Возьмем задание из пятого занятия.

Допустим, какая-то программа возвращает результат своей работы в таком виде:

результат операции: 42

результат операции: 54

результат работы программы: 209

результат: 2

Нужно сделать всё то же самое, но уже способ - на ваше усмотрение 
(можно с помощью срезов и метода index, а можно с помощью split ). 
Получите из каждой строки с результатом число, прибавьте к полученному числу 10, 
результат сложения распечатайте. Главное отличие - выполните всё с использованием функций. 
Нужно сделать так, чтобы строк кода стало как можно меньше, и не было повторений одного и того же.
'''
    
# RESALT_1 = "результат операции: 42"
# RESALT_2 = "результат операции: 54"
# RESALT_3 = "результат работы программы: 209"
# RESALT_4 = "результат: 2"

# print(int(RESALT_1[RESALT_1.index(":") + 2:]) + 10)  # Выводим результат
# print(int(RESALT_2[RESALT_2.index(":") + 2:]) + 10)  # Выводим результат
# print(int(RESALT_3[RESALT_3.index(":") + 2:]) + 10)  # Выводим результат
# print(int(RESALT_4[RESALT_4.index(":") + 2:]) + 10)  # Выводим результат

def operation_results(result_string):
    return int(result_string[result_string.index(":") + 2:]) + 10

results = [
    "результат операции: 42",
    "результат операции: 54",
    "результат работы программы: 209",
    "результат: 2"
]

for result in results:
    print(operation_results(result))
