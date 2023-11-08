#This part cover: 
    # lists, dictionaries, tuples, sets, strings, input, and control statements
### collections ###

# lists

lst = [1, 2.0, [True, "Flavian"], None]
# print(lst[0])


lst.append("new_value")
# print(lst)

lst.extend([100, "hello"])
# print(lst)

num_lst = [1, 5, -5]
alf_lst = ["a", "bc", "hello", "Flavian"]
num_lst.sort()
alf_lst.sort()

# print(alf_lst)
# print(num_lst)

## more methods ###
# print(lst.count(2.0))
# print(lst.index(1))
# lst.insert(2, "hello")
# print(lst)
# lst.pop()  # removes the last element of the list
# lst.pop(3)  # removes the element at the index 3
# print(lst)
# lst.remove(2.0)  # removes the first occurrency of a specific element
# print(lst)
# lst.clear()
# print(lst)

# lst.reverse()
# print(lst)


# print(help(list))


## slicing ###

# print(lst[0:3])  # start is inclusive; end is exclusive
# print(lst[:4])  # starts at the beginning of the list
# print(lst[2:])  # ends at the bottom of the list


## negative indexes ##
# print(lst[-1])
# print(lst[-3:-1])


### dictionaries ###

phonebook = {123: {"hi": "hello"}, "jurgen": 456, 12: "hello", True: False}
# print(phonebook[12])

# print(phonebook["andi"])  # get a value from the dictionary by the key
# print(phonebook.get("andi", "Not found!"))  # get a value or return None

phonebook["jurgen"] = 789  # add a pair
# print(phonebook)
# phonebook.update({"andi": 789})  # add multiple pairs

# phonebook.pop("damiano")  # deletes a pair by the key and returns it
# del phonebook["damiano"]   # deletes a pair by the key

# print(phonebook)


### tuples ###

tpl = (12, "hello", (1, 2), ["a", "b"], True)
tpl2 = tpl

tpl = 10
# print(tpl)
# print(tpl2)


# ### sets ###
# animals = {"dog", "cat", "elephant"}

# value = input("Vendosni nje kategori kafshe: ")
# if value in animals:
#     print("Kategoria ndodhet tek bashkesia e kafsheve!")
#     print("something else")
# else:
#     print("Kategoria nuk ndodhet tek bashkesia e kafsheve!")


# finding unique elements in a list
lst1 = [1, 1, 2, 3, 4, 4, 4, 4]
# print(list(set(lst1)))


### print ###
# print("a", "b", 1, 2, sep="_", end="\t")
# print("damiano")


a = "Hello"
b = "World"
# print("%s %s" % (a, b))
# print("{} {}".format(a, b))
# print(f"{a * 3} {b} !")


# percent = 0.71
# print(f"{percent: .1%}")
# print(f"{percent: .1f}")


### strings ###
# strings are immutbale, like tuples

str1 = "Flavian"
# str1["3"] = "a"

# print(str1.upper())
# print(str1)

str2 = "Hello world"
splitted_string = str2.split(" ")
# print(splitted_string)


### input ####
# input_data = input("Vendosni nje VLERE: ")
# print(type(input_data))  # always string


### control statements ###
# age = int(input("Vendosni moshen tuaj: "))

# if age < 18:
#     print("You are a minor")
# elif age < 65:  # same as 18 < age < 65
#     print("You are an adult")
# else:
#     print("You are a senior")


# x = 0
# y = 5

# if x < 0:
#     print("x is negative")

# if y > 0:
#     print("y is positive")


# lst = []

# if lst:
#     print("Lista nuk eshte boshe")
# else:
#     print("lista eshte boshe")


### converted to boolean ###
# []  {}  '' 0  None  (,) -> False
# any other value -> True


## while loop ###
name = "hello"
i = 1
while i < 20:
    print(i)
    if i % 15 == 0:
        break
    i += 1
