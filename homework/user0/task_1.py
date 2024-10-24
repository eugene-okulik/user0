'''
Обработка даты
Дана такая дата: "Jan 15, 2023 - 12:05:33"

Преобразуйте эту дату в питоновский формат, после этого:

1. Распечатайте полное название месяца из этой даты

2. Распечатайте дату в таком формате: "15.01.2023, 12:05"
'''
from datetime import datetime

MY_DATE = 'Jan 15, 2023 - 12:05:33'
DATE_FORMAT = "%b %d, %Y - %H:%M:%S"

python_date = datetime.strptime(MY_DATE, DATE_FORMAT)

print(python_date)
print(python_date.strftime('%B'))
print(python_date.strftime('%d.%m.%Y, %H:%M'))
