

def get_movement_products():
    # Считываем файл
    with open("./data/product.txt") as file:
        from_file = file.readlines()


    # Массив для данных
    array_result = []

    # Разбиваем строки из полученного файла в массив
    for line in from_file:
        line = line[:-2]
        line_list = line.split(';')
        array_result.append(line_list)

    # Выводим отформатированный файл
    return array_result

def get_directorys():
    # Считываем файл
    with open("./data/directory.txt") as file:
        from_file = file.readlines()


    # Массив для данных
    array_result = []

    # Разбиваем строки из полученного файла в массив
    for line in from_file:
        line = line[:-1]
        line_list = line.split(';')
        array_result.append(line_list)

    # Выводим отформатированный файл
    return array_result


def show_movement_product(products):

    product_from = input("С какого склада?\n")
    product_to = input("По какой склада?\n")

    for product in products:
        if product_from < product[0] < product_to:
            print("Номер складу: {:9} | Код товару: {:9} |  Залишок на початок місяця: {:12} | Прибуток: {:12} | Вибуток: {:12}".format(product[0], product[1], product[2], product[3], product[4]))

def show_directory(directorys):

    directory_from = input("С какого товара?\n")
    directory_to = input("По какой товар?\n")

    for directory in directorys:
        if directory_from < directory[0] < directory_to:
            print("Код товару: {:9} | Назва товару: {:9}".format(directory[0], directory[1]))
