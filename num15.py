products = [
    {"name": "Ноутбук", "price": 5000, "nums": 10},
    {"name": "Планшет", "price": 2300, "nums": 12},
    {"name": "Телефон", "price": 1300, "nums": 14},
    {"name": "Повербак", "price": 720, "nums": 9}
]

total = 0
for product in products:
    total += product["price"] * product["nums"]
print(f"Общая выручка: {total}")

max_total = 0
best = ""
for product in products:
    current = product["price"] * product["nums"]
    if max_total < current:
        max_total = current
        best = product["name"]
print(f"Самый прибыльный товар: {best}")
print(f"Выручка по данному товару: {max_total}")

unique_names = set()
for product in products:
    unique_names.add(product["name"])
print(f"Количество уникальных наименований: {len(unique_names)}")