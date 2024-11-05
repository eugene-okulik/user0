"""
Задание №3
Напишите программу: Есть функция которая делает одну из арифметических операций
с переданными ей числами (числа и операция передаются в аргументы функции).
Функция выглядит примерно так:

def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif .....

Программа спрашивает у пользователя 2 числа (вне функции)

Создайте декоратор, который декорирует функцию calc
и управляет тем какая операция будет произведена:

если числа равны, то функция calc вызывается с операцией сложения этих чисел
если первое больше второго, то происходит вычитание второго из певрого
если второе больше первого - деление первого на второе
если одно из чисел отрицательное - умножение
"""
# Декоратор для управления операцией
def operation_controller(func):
    '''
    Декоратор operation_controller: Принимает функцию calc и оборачивает её в функцию wrapper.
    '''
    def wrapper(first, second, operation=None):
        # Управляем операцией в зависимости от условий
        if first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        elif second > first:
            operation = '/'
        if first < 0 or second < 0:
            operation = '*'
        # Вызываем исходную функцию с выбранной операцией
        return func(first, second, operation)
    return wrapper

# Декорированная функция для выполнения арифметических операций
@operation_controller
def calc(first, second, operation):
    '''
    Функция calc: Выполняет выбранную арифметическую операцию.
    '''
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        # Проверка на деление на ноль
        if second != 0:
            return first / second
        else:
            return "Ошибка: деление на ноль!"
    else:
        return "Неизвестная операция"

# Основная программа
try:
    first_number = float(input("Введите первое число: "))
    second_number = float(input("Введите второе число: "))
    # Вызываем функцию без указания операции (она будет выбрана декоратором)
    result = calc(first_number, second_number)
    print("Результат:", result)
except ValueError:
    print("Ошибка: необходимо ввести числовое значение.")
