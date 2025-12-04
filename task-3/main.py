import json
import os
#Имя файла
filename = "flowers.json"
#Если файла нет — создать пустой массив
if not os.path.exists(filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump([], f, ensure_ascii=False, indent=4)
#Счётчик выполненных операций
operations = 0
while True:
    print("\n======= МЕНЮ =======")
    print("1. Вывести все записи")
    print("2. Вывести запись по полю id")
    print("3. Добавить запись")
    print("4. Удалить запись по id")
    print("5. Выйти из программы")
    print("====================")
    choice = input("Выберите пункт меню: ").strip()

    #Загружаем файл
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    #1.Вывести все записи
    if choice == "1":
        print("\n===== ВСЕ ЗАПИСИ =====")
        for i, item in enumerate(data):
            print(f"[{i}] id: {item['id']}, name: {item['name']}, "
                  f"latin_name: {item['latin_name']}, "
                  f"is_red_book_flower: {item['is_red_book_flower']}, "
                  f"price: {item['price']}")
        operations += 1

    #2.Вывести запись по id
    elif choice == "2":
        try:
            find_id = int(input("Введите id: "))
        except:
            print("Некорректный id.")
            continue
        found = False
        for index, item in enumerate(data):
            if item["id"] == find_id:
                print("\n===== НАЙДЕНО =====")
                print(f"Позиция: {index}")
                print(f"id: {item['id']}")
                print(f"name: {item['name']}")
                print(f"latin_name: {item['latin_name']}")
                print(f"is_red_book_flower: {item['is_red_book_flower']}")
                print(f"price: {item['price']}")
                found = True
                break
        if not found:
            print("Запись не найдена!")
        operations += 1

    #3.Добавить запись
    elif choice == "3":
        try:
            new_id = int(input("id: "))
            new_name = input("Название: ")
            new_latin = input("Латинское название: ")
            new_redbook = input("Краснокнижный? (true/false): ").lower() == "true"
            new_price = float(input("Цена: "))
        except:
            print("Ошибка ввода данных!")
            continue
        data.append({
            "id": new_id,
            "name": new_name,
            "latin_name": new_latin,
            "is_red_book_flower": new_redbook,
            "price": new_price
        })
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print("Запись добавлена.")
        operations += 1


    #4.Удалить запись по id
    elif choice == "4":
        try:
            del_id = int(input("Введите id для удаления: "))
        except:
            print("Некорректный id!")
            continue
        removed = False
        for item in data:
            if item["id"] == del_id:
                data.remove(item)
                removed = True
                break
        if removed:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print("Запись удалена.")
        else:
            print("Запись не найдена!")
        operations += 1

    #5.Выход
    elif choice == "5":
        print("\n===================================")
        print("Вы завершили программу.")
        print("Количество операций:", operations)
        print("===================================")
        break
    else:
        print("Неверный пункт меню!")
