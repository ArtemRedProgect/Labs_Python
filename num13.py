stroka = input("Введите список чисел: ")
numbers = [float(x) if "." in x else int(x) for x in stroka.split()]

print("Уникальные числа: ")
for number in numbers:
    if numbers.count(number) == 1:
        print(number)

print("Повторяющееся числа: ")
for number in set(numbers):
    if numbers.count(number) > 1:
        print(number)

print("Четные числа: ")
for number in numbers:
    if isinstance(number, int) and number % 2 == 0:
        print(number)

print("Нечетные числа: ")
for number in numbers:
    if isinstance(number, int) and number % 2 != 0:
        print(number)

print("Отрицательные числа: ")
for number in numbers:
    if number < 0:
        print(number)

print("Числа с плавающей точкой: ")
for number in numbers:
    if isinstance(number, float):
        print(number)

sum5 = 0
for number in numbers:
    if number % 5 == 0:
        sum5 += number
print("Сумма чисел кратных 5: ", sum5)

max_number = max(numbers)
min_number = min(numbers)
print("Самое большое число: ", max_number)
print("Самое маленькое число: ", min_number)