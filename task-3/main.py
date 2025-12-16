import json

#Функция для загрузки данных из файла
def load_data(filename="flowers.json"):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

#Функция для сохранения данных в файл
def save_data(data, filename="flowers.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)

#Функция для вывода всех записей
def display_all_records(data):
    print("\n===== ВСЕ ЗАПИСИ =====")
    for i, item in enumerate(data):
        print(f"[{i}] id: {item['id']}, name: {item['name']}, "
              f"latin_name: {item['latin_name']}, "
              f"is_red_book_flower: {item['is_red_book_flower']}, "
              f"price: {item['price']}")

#Функция для поиска записи по id
def display_record_by_id(data):
    try:
        find_id = int(input("Введите id: "))
    except ValueError:
        print("Некорректный id.")
        return
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

#Функция для добавления записи
def add_record(data):
    try:
        new_id = int(input("id: "))
        new_name = input("Название: ")
        new_latin = input("Латинское название: ")
        new_redbook = input("Краснокнижный? (true/false): ").lower() == "true"
        new_price = float(input("Цена: "))
    except ValueError:
        print("Ошибка ввода данных!")
        return
    data.append({
        "id": new_id,
        "name": new_name,
        "latin_name": new_latin,
        "is_red_book_flower": new_redbook,
        "price": new_price
    })
    print("Запись добавлена.")

#Функция для удаления записи по id
def delete_record_by_id(data):
    try:
        del_id = int(input("Введите id для удаления: "))
    except ValueError:
        print("Некорректный id!")
        return
    removed = False
    for item in data:
        if item["id"] == del_id:
            data.remove(item)
            removed = True
            break
    if removed:
        print("Запись удалена.")
    else:
        print("Запись не найдена!")

#Основная функция для управления меню
def main():
    operations = 0  #Счётчик выполненных операций
    while True:
        print("\n======= МЕНЮ =======")
        print("1. Вывести все записи")
        print("2. Вывести запись по полю id")
        print("3. Добавить запись")
        print("4. Удалить запись по id")
        print("5. Выйти из программы")
        print("====================")
        choice = input("Выберите пункт меню: ").strip()

        data = load_data()  #Загружаем данные

        if choice == "1":
            display_all_records(data)
            operations += 1

        elif choice == "2":
            display_record_by_id(data)
            operations += 1

        elif choice == "3":
            add_record(data)
            save_data(data)
            operations += 1

        elif choice == "4":
            delete_record_by_id(data)
            save_data(data)
            operations += 1

        elif choice == "5":
            print("\n===================================")
            print("Вы завершили программу.")
            print(f"Количество операций: {operations}")
            print("===================================")
            break

        else:
            print("Неверный пункт меню!")

#Запуск программы
if __name__ == "__main__":
    main()


