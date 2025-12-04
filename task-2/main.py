import json
with open('dump.json', 'r', encoding='utf-8') as file: #открываем файл и считваем его
    data = json.load(file) 
num = input("Номер квалификаци ").strip() #запрашаем у пользователя номер квалификации
found = False #переменая для проверки найдености квалификации
for i in data:
    model = i.get("model")
    fields = i.get("fields", {}) #присваеваем значение ключей переменным
    #проверка на совпадение номера
    if fields.get("code") != num:
        continue
    #Если нашли, то
    if not found:
        print("=============== Найдено ===============")
        found = True

    if model == "data.specialty": #если специальность, то выводим ее
        print(f"{num} >> Специальность  \"{fields.get('title')}\", \"{fields.get('c_type')}\"")

    elif model == "data.skill": #если квалификация, то выводим ее
        print(f"{num} >> Квалификация \"{fields.get('title')}\"")
#Если ничего не найдено
if not found:
    print("=============== Не найдено ===============")