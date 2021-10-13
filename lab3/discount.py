import random
import os


def write_to_file(url):
    file = open(url, 'w')
    quantity_of_goods = random.randint(5, 10)
    for i in random.sample(range(0, 100), quantity_of_goods):
        file.write(str(i) + " ")
    file.write("\n" + str(random.randint(0, 100)))


def open_and_read_file(url):
    price_data = []
    with open(url) as file:
        for line in file:
            price_data.extend([int(item)for item in line.split()])
    return price_data


def discount_search(my_list: list):
    discount = my_list.pop(-1)
    my_list.sort()
    whole_price = 0.0
    for i in my_list:
        whole_price += i

    discount_products = len(my_list)/3
    goods_with_discount = len(my_list) - 1
    goods_without_discount = int(len(my_list) - discount_products - 1)
    price: float = 0.0

    while goods_with_discount >= len(my_list) - discount_products:
        price += (1 - float(discount/100)) * my_list[goods_with_discount]
        goods_with_discount -= 1

    while goods_without_discount >= 0:
        price += my_list[goods_without_discount]
        goods_without_discount -= 1

    return whole_price, price, discount


if __name__ == '__main__':
    my_file = "file.txt"
    write_to_file(my_file)
    data = open_and_read_file(my_file)
    print(discount_search(data))

    command = "python -m unittest test.TestDiscount"
    os.system(command)