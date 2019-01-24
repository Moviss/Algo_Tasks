def find_missing(in_list, n):
    miss_list = []
    if in_list[0] > 1:
        miss_list = list(range(1, in_list[0]))
    if in_list[-1] != n:
        in_list.append(n)
    complete_set = set(range(in_list[0], in_list[-1] + 1))
    miss_list = miss_list + list(complete_set - set(in_list))
    if miss_list[-1] != n:
        miss_list.append(n)
    return miss_list


# testArr1 = [3, 5, 7, 8, 9, 12, 14]
# testArr2 = [1, 5, 8, 67]
# print(find_missing(testArr1, 22))
# print(find_missing(testArr2, 88))
