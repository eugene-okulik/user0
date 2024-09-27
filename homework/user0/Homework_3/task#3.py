# задание: Даны два числа. Найти среднее арифметическое и среднее геометрическое этих чисел

a = float (input ("Введите число a = "))
b = float (input ("Введите число b = "))

arithmetic_mean = (a + b) / 2
geometric_mean = (a * b) ** 0.5

print (f"Среднее арифметическое: {arithmetic_mean}")
print (f"Среднее геометрическое: {geometric_mean}") 
