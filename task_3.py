from decimal import *


def number_generator():
    number_list = []
    i = Decimal(2)
    while i <= Decimal(5.5):
        number_list.append(i)
        i += Decimal(0.5)
    return print(number_list)

# number_generator()
