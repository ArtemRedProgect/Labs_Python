minuts = int(input("Введите количество потраченных минут: "))
sms = int(input("Введите количество смс: "))
web = int(input("Введите количество потраченных мб: "))
limit_minuts = 60
limit_sms = 30
limit_web = 1000
tarif = 24.99
sum_minuts = 0
sum_sms = 0
sum_web = 0

if minuts > limit_minuts:
    sum_minuts = (minuts - limit_minuts) * 0.89
if sms > limit_sms:
    sum_sms = (sms - limit_sms) * 0.59
if web > limit_web:
    sum_web = (web - limit_web) * 0.79

komissya = ((tarif + sum_minuts + sum_sms + sum_web) / 100) * 2
result = komissya + tarif + sum_minuts + sum_sms + sum_web

print(f"Сумма по тарифу: {tarif:.2f}")
if sum_minuts != 0:
    print(f"Дополнительные минуты: {sum_minuts:.2f}")
if sum_sms != 0:
    print(f"Дополнительные смс: {sum_sms:.2f}")
if sum_web != 0:
    print(f"Дополнительный интернет: {sum_web:.2f}")

print(f"Налог (2%): {komissya:.2f}")
print(f"Итоговая стоимость: {result:.2f}")