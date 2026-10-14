stroka1 = input("Введите первый список чисел: ")
stroka2 = input("Введите второй список чисел: ")

numbers1 = stroka1.split()
numbers2 = stroka2.split()

common = set(numbers1) & set(numbers2)
print("Общие элементы: ")
for num in common:
    print(num, end = " ")
print()

only1 = set(numbers1) - set(numbers2)
print("Уникальные элементы из 1: ")
for num in only1:
    print(num, end = " ")
print()

print("Уникальные элементы из 2: ")
only2 = set(numbers2) - set(numbers1)
for num in only2:
    print(num, end = " ")
print()

notcommon = set(numbers1) ^ set(numbers2)
print("Числа которых нет в обоих: ")
for num in notcommon:
    print(num, end = " ")