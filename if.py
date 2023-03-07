y = 20
x = 53
if y == 20:
    x = 0
    print(x)

sales = 20000
commisionRate = None
if sales >= 10000:
    commisionRate = 0.2
    print(commisionRate)
    
BASE_HOURS = 40 #базовые часы в неделю
OT_MULTIPLIER = 1.5 #коэффициет сверурочного времени

#получаем отработанные часы и почасовую оплату труда
hours = float(input('Введите кол-во часов: '))
pay_rate = float(input('почасовую оплату труда: '))

# Рассчитать и показать заработную плату до удержаний.
if hours > BASE_HOURS:
    # получаем количество свехурочных
    overtime_hours = hours - BASE_HOURS
    # сверхурочно
    overtime_pay = overtime_hours + pay_rate + OT_MULTIPLIER
    # Зп до удержаний
    gross_pay = BASE_HOURS * pay_rate + overtime_pay
else:
    #  до удержаний и свехурочных
    gross_pay = hours * pay_rate
print(f'Зарабатная плата до удержаний составляет: ${gross_pay:,.2f}.')       