
print("Доступные типы: длина, масса, время, температура, площадь, объем, скорость, память, давление, энергия")
type = input("Введите тип измерения: ").lower()

value = float(input("Введите числовое значение: "))
ishod = input("Введите исходную единицу: ").lower()
celevaya = input("Введите целевую единицу: ").lower()

base_value = 0.0
result = 0.0
is_valid = True

match type:
    case "длина":
        match ishod:
            case "м": base_value = value
            case "см": base_value = value / 100
            case "мм": base_value = value / 1000
            case "км": base_value = value * 1000
            case _: is_valid = False

        match celevaya:
            case "м": result = base_value
            case "см": result = base_value * 100
            case "мм": result = base_value * 1000
            case "км": result = base_value / 1000
            case _: is_valid = False

    case "масса":
        match ishod:
            case "г": base_value = value
            case "кг": base_value = value * 1000
            case "мг": base_value = value / 1000
            case _: is_valid = False

        match celevaya:
            case "г": result = base_value
            case "кг": result = base_value / 1000
            case "мг": result = base_value * 1000
            case _: is_valid = False

    case "время":
        match ishod:
            case "сек": base_value = value
            case "мин": base_value = value * 60
            case "час": base_value = value * 3600
            case _: is_valid = False

        match celevaya:
            case "сек": result = base_value
            case "мин": result = base_value / 60
            case "час": result = base_value / 3600
            case _: is_valid = False

    case "температура":
        match ishod:
            case "c": base_value = value
            case "f": base_value = (value - 32) * 5 / 9
            case _: is_valid = False

        match celevaya:
            case "c": result = base_value
            case "f": result = (base_value * 9 / 5) + 32
            case _: is_valid = False

    case "площадь":
        match ishod:
            case "кв.м": base_value = value
            case "ар": base_value = value * 100
            case "гектар": base_value = value * 10000
            case _: is_valid = False

        match celevaya:
            case "кв.м": result = base_value
            case "ар": result = base_value / 100
            case "гектар": result = base_value / 10000
            case _: is_valid = False

    case "объем":
        match ishod:
            case "л": base_value = value
            case "мл": base_value = value / 1000
            case _: is_valid = False

        match celevaya:
            case "л": result = base_value
            case "мл": result = base_value * 1000
            case _: is_valid = False

    case "скорость":
        match ishod:
            case "мс": base_value = value
            case "кмч": base_value = value / 3.6
            case _: is_valid = False

        match celevaya:
            case "мс": result = base_value
            case "кмч": result = base_value * 3.6
            case _: is_valid = False

    case "память":
        match ishod:
            case "б": base_value = value
            case "кб": base_value = value * 1024
            case "мб": base_value = value * 1024 * 1024
            case _: is_valid = False

        match celevaya:
            case "б": result = base_value
            case "кб": result = base_value / 1024
            case "мб": result = base_value / (1024 * 1024)
            case _: is_valid = False

    case "давление":
        match ishod:
            case "па": base_value = value
            case "атм": base_value = value * 101325
            case _: is_valid = False

        match celevaya:
            case "па": result = base_value
            case "атм": result = base_value / 101325
            case _: is_valid = False

    case "энергия":
        match ishod:
            case "дж": base_value = value
            case "калория": base_value = value * 4.184
            case _: is_valid = False

        match celevaya:
            case "дж": result = base_value
            case "калория": result = base_value / 4.184
            case _: is_valid = False

    case _:
        is_valid = False

if is_valid:
    print(f"Результат: {value} {ishod} = {result} {celevaya}")
else:
    print("Ошибка: Неверно указан тип измерения или единицы.")