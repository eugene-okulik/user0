'''
задание: Даны числа x и y, получите x - y / 1 + xy
'''

x = float(input("Введите число x = "))
y = float(input("Введите число y = "))

expression = x - y / (1 + x * y)

print(f"Результат: {expression}")
