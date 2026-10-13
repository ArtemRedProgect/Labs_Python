stroka1 = input("Введите строку: ")
reverse_stroka = stroka1[::-1]
if reverse_stroka.lower() == stroka1.lower():
    print("Строки одинаковые")
else:
    print("Строки разные")