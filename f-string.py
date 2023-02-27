print(f'Hello,world')
name = 'John'
print(f'Hello, {name}. ')
temperature = 45
print(f'сейчас {temperature} градусов')
print(f'значение равно: {10 + 2}')
# Округление чисел с плавающей точкой
amount_due = 456789.0
monthly_payment = amount_due / 12.0
print(f'Ежемесячный платеж составляет {monthly_payment:.2f}')
# Вставка запятых в качестве разделителя
number = 23456789.123456
print(f'{number:,}')
# Форматирование числа с плавающей точкой в процентах
discount = 0.9
print(f'{discount:%}')
# А вот пример, который округляет выходное значение до О знаков после точки
discount = 0.5
print(f'{discount:.0%}')