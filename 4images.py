### Print images with for ###

## fig 1)
# n = 5
#          i   space    *
#     *    0       4    1
#    **    1       3    2
#   ***    2       2    3
#  ****    3       1    4
# *****    4       0    5

## fig 2)
# *        0       4    1
# **       1       3    2
# ***      2       2    3
# ****     3       1    4
# *****    4       0    5


## fig 3)
# *   *
#  * *
#   *
#  * *
# *   *

# fig 1
# n = int(input("Vendosni nje numer integer n: "))
# for i in range(n):
#     for j in range(n):
#         if i >= n - j - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print("\n", end="")


# fig 2
# n = int(input("Vendosni nje numer integer n: "))
# for i in range(n):
#     for j in range(n):
#         if i >= j:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print("\n", end="")


# fig 3
# n = int(input("Vendosni nje numer integer n: "))
# for i in range(n):
#     for j in range(n):
#         if i == n - j - 1 or i == j:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print("\n", end="")


### Ushtrimi ###
# string_1 = "0011110101001111111111100001100000000111101"
# list_of_ones = string_1.split("0")
# list_of_zeros = string_1.split("1")
# max_length_zeros = 0
# max_length_ones = 0
# for el in list_of_zeros:
#     if len(el) > max_length_zeros:
#         max_length_zeros = len(el)
# for el in list_of_ones:
#     if len(el) > max_length_ones:
#         max_length_ones = len(el)

# print(f"Ones: {max_length_ones}")
# print(f"Zeros: {max_length_zeros}")