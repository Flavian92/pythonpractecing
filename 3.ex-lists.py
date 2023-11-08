
# L1 = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]

# result should be [10, 20, 30, 40, 50, 60, 70, 80, 90]

# new_list = []

# # resolution 1
# for i in range(len(L1)):
#     for j in range(len(L1[i])):
#         new_list.append(L1[i][j])

# # resolution 2
# for i in L1:
#     for j in i:
#         new_list.append(j)


# resolution 3
# L2 = [element for sublist in L1 for element in sublist]


# # resolution 4
# for el in L1:
#     new_list.extend(el)

# # menyra 4.2
# for el in L1:
#     new_list += el

# print(new_list)
