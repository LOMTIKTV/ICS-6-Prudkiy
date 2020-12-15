import os
from process_data import revolving_bill
from data_service import get_movement_products, get_directorys, show_movement_product, show_directory


MAIN_MENU = \
"""
~~~~~~~~~~~  Обробка оборотної відомості ~~~~~~~~~~~

1 - Вивід оборотної відомості
2 - Запис оборотної відомості в файл
3 - Вивід руху товарів
4 - вивід довідника товарів
0 - завершення роботи
------------------------------------------------------
"""

TITLE = "Оборотна відомість"

HEADER = \
"""
================================================================================================================================
|  Номер складу  |    Назва товара    |   Залишок на початок місяця   |   Прибуток  |  Вибуток  |   Залишок на кінець місяця   |
================================================================================================================================
"""

FOOTER = \
'''
================================================================================================================================
'''

STOP_MESSAGE = '\nДля продовження натисніть <Enter>'

def showRevolvingBill():
    revolvings = revolving_bill()

    print(TITLE)
    print(HEADER)

    for revolving in revolvings:
        print(
        f"{revolving['warehouse_number']:21}",
        f"{revolving['name_product']:25}",
        f"{revolving['remainder_start']:>13}",
        f"{revolving['profit']:>21}",
        f"{revolving['excess']:>17}",
        f"{revolving['remainder_end']:>22}"

        )
    print(FOOTER)

def saveRevolvingBill(revolvings):
    with open("RevolvingBill.txt", "w") as file:
        for revolving in revolvings:
            line = \
                str(revolving['warehouse_number'])   + ';' + \
                revolving['name_product']    + ';' + \
                str(revolving['remainder_start'])  + ';' + \
                str(revolving['profit'])   + ';' + \
                str(revolving['excess'])   + ';' + \
                str(revolving['remainder_end'])    + '\n'

            file.write(line)
        print("Сохранение прошло успешно.")

while True:

    os.system("cls")
    print(MAIN_MENU)
    command = input("Введіть номер команди: ")

    # Обработка команд пользователя
    if command == "0":
        os.system("cls")
        print("\nПрограма завершила роботу.")
        exit(0)
    elif command == "1":
        os.system("mode 160,30")
        os.system("cls")
        showRevolvingBill()
        input('\n' + STOP_MESSAGE)
    elif command == "2":
        os.system("cls")
        revolvings = revolving_bill()
        saveRevolvingBill(revolvings)
        input(STOP_MESSAGE)
    elif command == "3":
        os.system("mode 140,30")
        show_movement_product(get_movement_products())
        input(STOP_MESSAGE)
    elif command == "4":
        os.system("mode 50,25")
        show_directory(get_directorys())
        input(STOP_MESSAGE)

    # В случае некорректно заданного значения выводим ошибку и завершаем процесс работы.
    else:
        os.system("cls")
        input("\nНекоректний номер команди, для продовження натисніть <Enter>")
