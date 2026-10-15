def flatten_list(lst):
    i = 0
    while i < len(lst):
        if isinstance(lst[i], list):
            flatten_list(lst[i])
            lst[i:i+1] = lst[i]
        else:
            i += 1
def unique_elements(lst):
    flatten_list(lst)
    result = []
    for x in lst:
        found = False
        for y in result:
            if x == y:
                found = True
                break
        if not found:
            result.append(x)
    return result


print("Пример списка: [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2 ,3]]]]")
list_a = eval(input("Введите список: "))

print(f"Уникальные элементы списка: {unique_elements(list_a)}")