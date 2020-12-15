
from data_service import get_movement_products,get_directorys,show_movement_product,show_directory


temp_revolving_bill = {
    "warehouse_number" : 0,
    "name_product" : "",
    "remainder_start" : 0,
    "profit" : 0,
    "excess" : 0,
    "remainder_end" : 0
}

def revolving_bill():


    def get_name_product_by_code(code):
        for directory in directorys:
            if directory[0] == code:
                return directory[1]
        return "Товар не найден"


    revolving_list = []

    products = get_movement_products()
    directorys = get_directorys()

    for product in products:

        temp = temp_revolving_bill.copy()

        temp["warehouse_number"] = product[0]
        temp["name_product"] = get_name_product_by_code(product[1])
        temp["remainder_start"] = round(float(product[2]), 1)
        temp["profit"] = round(float(product[3]), 1)
        temp["excess"] = round(float(product[4]), 1)
        temp["remainder_end"] = round(float(temp["remainder_start"]) + float(temp["profit"]) + float(temp["excess"]), 1)

        revolving_list.append(temp)

    return revolving_list
