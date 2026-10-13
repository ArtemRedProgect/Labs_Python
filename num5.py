a, b = int(input("Введите первое число: ")), int(input("Введите второе число: "))
print(f"Сумма = {a + b}")
print(f"Разность = {a - b}")
print(f"Умножение = {a * b}")
if b != 0:
    print(f"Деление = {a / b}")
    print(f"Остаток = {a % b}")
else:
    print("Деление = 0")
    print("Остаток = 0")
print(f"Возведение в степень = {a ** b}")