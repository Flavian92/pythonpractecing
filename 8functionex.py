# Ushtrimi 1: shkruani nje FUNKSION qe merr si parameter 2
# numra dhe gjen nese njeri prej tyre eshte i plotpjestueshem me tjetrin. Per shembull:
# nese funksioni merr si argument 5 dhe 10 ----> do printohet: 10 plotpjestohet me 5
# nese funksioni merr si argument 5 dhe 7 -----> do printohet: numrat nuk plotpjestohen
# nese funksioni merr si argument 8 dhe 4 -----> do printohet: 8 plotpjestohet me 4


# def func_1(nr_1, nr_2):
#     if nr_2 % nr_1 == 0:
#         print(f"{nr_2} plotpjsethoet me {nr_1}")
#     elif nr_1 % nr_2 == 0:
#         print(f"{nr_1} plotpjestohet me {nr_2}")
#     else:
#         print("Numrat nuk plotpjestohen.")


# a = int(input("Vendosni numrin e pare: "))
# b = int(input("Vendosni numrin e dyte: "))
# func_1(a, b)


### Ushtrmimi 2###
# Shkruani nje FUNKSION qe merr si parameter nje list me stringje dhe
# fshin te gjitha elementet e kesaj liste qe permbajn karaktere jo-numerike.
# Ne fund funksioni do kthej listen e perftuar.
# per shembull:

# nqs funksioni do perdoret duke i dhene si
# parameter listen ['abcd','a1','22','3','1%','12345','Hello'] atehere
# funksioni do kthej ['22', '3', '12345']

## KNOWLEDGE
# s1 = "123"
# print(s1.isnumeric()) -> True
# s2 = "123a"
# print(s2.isnumeric()) -> False


# def func_2(list_of_str):
#     lst = []
#     for el in list_of_str:
#         if el.isnumeric():
#             lst.append(el)
#     return lst


# result = func_2(["abcd", "a1", "22", "3", "1%", "12345", "Hello"])
# print(result)


### Ushtrimi 3 ###
# Shkruani nje FUNKSION qe merr si parametra dy string cfaredo dhe kthen nje string te ri
# i cili perbehet nga karakteret e ketyre dy string-ve ne menyre te alternuar.
# a) (supozojme se 2 strings kane gjatesi te njejte)
# b) (supozojme se 2 strings kane gjatesi te ndryshme)

# SHEMBULL:
# a)
# Ne qofte se stringjet jane : string_1 = "123"
# 			    string_2 = "ABC"
# Atehere ---> string_3 do te jete "1A2B3C"
# b)
# Ne qofte se stringjet jane : string_1 = "123456"
# 			    string_2 = "ABC"
# Atehere ---> string_3 do te jete "1A2B3C456"


# a)
# def alternate_1(str_1, str_2):
# result_str = ""
## menyra 1
# for i, j in zip(str_1, str_2):
#     result_str += i + j
# return result_str
## menyra 2
# i = 0
# while i < len(str_1):
#     result_str += (
#         str_1[i] + str_2[i]
#     )  # result_str = result_str + str_1[i] + str_2[i]
#     i += 1
# return result_str


# print(alternate_1("123", "ABC"))


# b)
# def alternate_2(str_1, str_2):
## menyra 1
# result_str = ""
# min_length = min(len(str_1), len(str_2))
# max_length = max(len(str_1), len(str_2))
# i = 0
# while i < min_length:
#     result_str += str_1[i] + str_2[i]
#     i += 1
# j = min_length
# while j < max_length:
#     if len(str_1) > len(str_2):
#         result_str += str_1[j]
#     else:
#         result_str += str_2[j]
#     j += 1
# return result_str

## menyra 2
#     result_str = ""
#     if len(str_1) > len(str_2):
#         max_string = str_1
#         min_string = str_2
#     else:
#         max_string = str_2
#         min_string = str_1
#     for i in range(len(min_string)):
#         result_str += str_1[i] + str_2[i]
#     result_str += max_string[len(min_string) :]
#     return result_str


# print(alternate_2("ABC", "123456"))


### Ushtrimi 4 ###
# Shkruani nje funksion qe merr nje numer arbitrar parametrash (numra float)
# dhe gjen mesataren e tyre.

# x = 10   # global variable


# def mesatare(*args):
#     print(x)    # known also inside functions
#     result = sum(args) / len(args)
#     return result


# result = mesatare(1, 2, 3)
# print(result)


### Ushtrimi 5 ###
# Shkruani nje funksion qe merr 2 strings si parameter dhe kthen True nese jane anagram
# te njeri tjetrit, perndryshe False
# shembull: "hello" dhe "loleh"  -> True
# shembull: "hello" dhe "heollll"  -> False


# def is_anagram(str_1, str_2):
#     if len(str_1) != len(str_2):
#         return False
#     for c in str_1:
#         if str_1.count(c) != str_2.count(c):
#             return False
#     return True


# print(is_anagram("hello", "ABCDEFGH"))


# ## Ushtrimi 6 ###
# Shkruani nje funksion qe merr si parameter nje numer arbitrash dictionary-sh
# dhe kthen nje dictionary te vetem te bashkuar
# shembull:
# {1: 2, 3: 4, 5: 6}, {10: 20, 30: 40} -> {1: 2, 3: 4, 5: 6, 10: 20, 30: 40}


# def dict_union(*args):
#     result_dict = {}
#     for d in args:
#         result_dict.update(d)
#     return result_dict


# result = dict_union({1: 2, 3: 4, 5: 6}, {10: 20, 30: 40})
# print(result)


### Ushtrimi 7 ###
# Shkruani nje funksion qe merr si parameter nje numer integer n,
# me pas krijon nje list me n numra integer te cilet do merren si input nga perdoruesi
# ne qofte se perdoruesi vendos gabimisht ndonje karakter jo-numerik atehere
# mbushja e listes do filloj nga fillimi, ne fund funksioni do kthej kete list

# fill_list(5)

# vendosni nje numer: ... 32
# vendosni nje numer: ... 432
# vendosni nje numer: ... 21
# vendosni nje numer: ... jio43  -> Gabim! -> mbushja e listes do filloj nga fillimi
# vendosni nje numer: ... 6547

# -> [32, 432, 21, 13, 6547]


# def fill_list(n: int) -> list:
#     result_list = []
#     while True:
#         for i in range(n):
#             value = input("Vendosni nje numer integer: ")
#             if value.isnumeric():
#                 result_list.append(value)
#             else:
#                 print("Gabim!")
#                 result_list = []
#                 break
#         if len(result_list) == n:
#             break

#     return result_list


# result = fill_list(5)
# print(result)

#################### D.SH.: gjeni ndonje zgjidhje tjeter #####################


################### D.SH.: ######################################
### Ushtrimi 8 ####
# Shkruani nje funksion qe merr si parameter nje string (sentence) dhe kthen nje list
# me te gjitha fjalet me karaktere reverse

# shembull:  per "Hello World"  -> "olleH dlroW"
