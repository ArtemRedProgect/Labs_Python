discount = 0
dop_discount = 0
sum = int(input("Укажите сумму покупки: "))
year = int(input("Сколько лет покупателю: "))
birhday = input("День рождения покупателя сегодня? да/нет: ")
vip = input("VIP? да/нет: ")
if sum > 1000:
    discount = 10
if year >= 63:
    dop_discount += 5
if birhday == "да":
    dop_discount += 5
if vip == "да":
    discount = 15
total_discount = discount + dop_discount
if total_discount > 25:
    total_discount = 25
print(f"Общая скидка: {total_discount}, Дополнительная скидка: {dop_discount}")