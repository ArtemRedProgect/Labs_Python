money = int(input("Введите сумму:"))

cup100 = money // 100
money %= 100

cup50 = money // 50
money %= 50

cup10 = money // 10
money %= 10

cup5 = money // 5
money %=5

cup2 = money // 2
money %= 2

cup1 = money // 1
print(f"Требуется купюр - 100 рублей: {cup100} 50 рублей: {cup50} 10 рублей: {cup10} 5 рублей: {cup5} 2 рубля: {cup2} 1 рубль: {cup1}")