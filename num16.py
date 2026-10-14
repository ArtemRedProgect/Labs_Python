def flatten_list(lst):
    i = 0
    while i < len(lst):
        if isinstance(lst[i], list):
            flatten_list(lst[i])
            lst[i:i+1] = lst[i]
        else:
            i += 1
print("Пример ввода: [1, 2, 3, [4], 5, [6, [7, [], 8, [9]]]] ")
stroka_a = input("Введите значения списка: ")
list_a = eval(stroka_a)
flatten_list(list_a)
print(f"Плоский список: {list_a}")