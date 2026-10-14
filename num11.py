year = int(input("Введите возвраст заемщика: "))
money = int(input("Доход заемщика: "))
size_credit = int(input("Введите размер кредита"))
srok_credit = int(input("На сколько месяцев берется кредит: "))
credit_story = int(input("Кредитная история: отличная - 0, хорошая - 1, удовлетворительная - 2, плохая - 3"))
members = int(input("Есть ли поручатели: 1 - да, 0 - нет"))
zalog = int(input("Есть ли залог: 1 - да, 0 - нет"))

m = size_credit / money
if year >= 60 or m >= 0.6 or credit_story == 3:
    print("Риск критический")
    risk = 3
elif year >= 45 or  m >= 0.5 or credit_story == 2:
    if members == 0 or zalog == 0:
        print("Риск высокий")
        risk = 2
    else:
        print("Риск средний")
        risk = 1
else:
    print("Риск низкий")
    risk = 0

if srok_credit >= 60 or risk >= 2:
    print("Рекомендуемая процентная ставка: 17.3%")
    stavka = 3
elif srok_credit >= 45 or risk == 2:
    print("Рекомендуемая процентная ставка: 14.52%")
    stavka = 2
elif srok_credit >= 25 or risk == 1:
    print("Рекомендуемая процентная ставка: 10.67%")
    stavka = 1
else:
    print("Стандартная процентная ставка: 6.69%")
    stavka = 0

if risk == 3:
    print("Отказать в кредите")
if risk == 2:
    if stavka <= 2:
        print("Одобрить кредит")
    else:
        print("Отказать в кредите")
if risk <= 1:
    print("Одобрить кредит")