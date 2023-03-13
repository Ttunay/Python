MIN_SALARY = 30000
MIN_YEARS = 2

salary = float(input('Введите ваш годовой доход'))
years_on_job = int(input('Введите количество лет' + 'рабочий стаж ' ))

if salary >= MIN_SALARY and years_on_job >= MIN_YEARS:
    print('Welcome')
else:
    print('poka')
    

speed = float(input('скорость'))

if speed >= 0 and speed <= 200:
    print('Welcome')
else:
    print('Wanted')