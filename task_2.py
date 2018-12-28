def find_missing(in_list, n):
    if in_list[-1] != n:
        in_list.append(n)
    complete_set = set(range(in_list[0], in_list[-1] + 1))
    miss_list = list(complete_set - set(in_list))
    if miss_list[-1] != n:
        miss_list.append(n)
    return miss_list


# testArr1 = [1, 5, 7, 8, 9, 12, 14]
# print(find_missing(testArr1, 22))
