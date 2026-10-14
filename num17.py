import json
def merge_dicts(dict_a, dict_b):
    for key, value_b in dict_b.items():
        if key in dict_a:
            value_a = dict_a[key]
            if isinstance(value_a, dict) and isinstance(value_b, dict):
                merge_dicts(value_a, value_b)

            elif isinstance(value_a, list) and isinstance(value_b, list):
                for item in value_b:
                    value_a.append(item)

            elif isinstance(value_a, set) and isinstance(value_b, set):
                for item in value_b:
                    value_a.add(item)

            elif isinstance(value_a, tuple) and isinstance(value_b, tuple):
                elements = list(value_a)
                for item in value_b:
                    elements.append(item)
                dict_a[key] = tuple(elements)

            else:
                dict_a[key] = value_b
        else:
            dict_a[key] = value_b

print('Формат ввода: {"a": 1, "b": {"c": 2}} ')
stroka_a = input("Введите первый словарь: ")
stroka_b = input("Введите второй словарь: ")

dict_a = json.loads(stroka_a)
dict_b = json.loads(stroka_b)

print(f"Словарь А: {dict_a}")
print(f"Словарь Б: {dict_b}")

merge_dicts(dict_a, dict_b)
print(f"Измененный Словарь А: {dict_a}")