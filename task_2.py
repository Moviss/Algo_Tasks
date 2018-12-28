def my_list_checker(my_list, n):
    miss_my_list = []
    # for index, element in enumerate(my_list):
    #     if element != index + 1:
    #         miss_count = element - (index+1)
    #         i = 0
    #         missed_number = index+1
    #         while i <= miss_count:
    #             miss_my_list.append(missed_number)
    #             i +=1
    #             missed_number += 1

    # j = 0
    # miss_my_list = []
    # for el in my_list:
    #     if el != j + 1:
    #         j = i
    #         while j < el:
    #             miss_my_list.append(j)
    #             j += 1
    # i = 1
    # for number in my_list:
    #     print(i)
    #     if number != i:
    #         j = my_list[i-1]
    #         while j <= my_list[i] - (i + 1):
    #             j += 1
    #             miss_my_list.append(j)
    #             i += 1
    # return miss_my_list

    miss_list = [None] * (n - len(my_list))
    prev_number = my_list[0]
    new_list = ['Start']
    i = 0
    while i < n:
        print('Iteracja nr: {}'.format(i))
        if my_list[i] == i+1:
            new_list.append(i+1)
            i += 1
        else:
            new_list.append(None)
            i += 1
    return new_list

testArr1 = [1, 5, 7, 8, 9, 10]
print(my_list_checker(testArr1, 10))
