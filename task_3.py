from decimal import Decimal


def number_generator():
    number_list = []
    i = Decimal(2)
    while i <= Decimal(5.5):
        number_list.append(i)
        i += Decimal(0.5)
    return number_list


# print(number_generator())
