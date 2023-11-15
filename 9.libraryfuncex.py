### functions ###


## with parameters
# def do_something(value_1, value_2):  # value_1 and value_2 are parameters
#     print(f"The first parameter is {value_1}")
#     print(f"The second parameter is {value_2}")


# do_something(10, 20)


## without parameters


# def print_hello() -> None:    #function does not return anything
#     print("hello")


# print_hello()


## function with return statement
# def pitagora(a: float, b: float) -> float:
#     c = ((a**2) + (b**2)) ** (1 / 2)
#     return c


# hypotenuze = pitagora(3, 4)
# print(hypotenuze)


## optional parameters ##
# def greet(name: str = "John"):
#     print(f"Hello {name}")


# greet()
# greet("Flavian")
# greet(name="Flavian")


## *args ##
# def args_sum(*args):
#     # args = (1, 2, 10, 100) -> tuple
#     print(sum(args))


# args_sum(1, 2, 10, 100)


## **kwargs ##
# def kwargs_sum(**kwargs):
#     print(kwargs.keys())  # print keys of dictionary
#     print(kwargs.values())  # print values of dictionary


# def args_and_kwargs(*args, **kwargs):
#     print(args)
#     print(kwargs)


# args_and_kwargs(1, 2, 3, 4, a="hello", b="world")


# def all_parameters(a, b, *args, c="Hello", **kwargs):
#     print(a)
#     print(b)
#     print(args)
#     print(c)
#     print(kwargs)


# all_parameters(1, 2, 10, 20, 30, c="World", d="Hi", e="!")


## modules ##
# import math  # import the whole module

# from math import *  # import everything from the module math
# from lecture_1 import *  # import everything from lecture_1 -> conflict regarding the pi variable

# from lecture_1 import multiplication_of_2_values

# from lecture_1 import multiplication_of_2_values as m2v  ## alias
# from utils.util_functions import ping


# product = m2v(2, 5)   # using alias
# product = multiplication_of_2_values(2, 5)  # using alias
# print(product)

# r = 5
# print(math.pi)
# P = 2 * math.pi * r
# print(P)


### file operations ###
# file = open("test_example.txt", "r+")

# print(file.readlines())
# file.seek(0)  # resets the cursor position at the start of the file
# file.write("hello")
# file.seek(0)
# print(file.readlines())

# file.close()


### `with` context manager ###
# with open("test_example.txt", "r") as file:
#     print(file.readlines())


# import json

# with open("example.json") as file:
#     data = json.load(file)  # deserialization
# print(data)
# print(data["data"][0]["id"])


# my_list = list()
# my_list = []


### OOP ###


# class Vehicle:
#     def __init__(self, wheels_nr) -> None:
#         self.wheels = (
#             wheels_nr  # object attribute (accessible only from an object of the class)
#         )

#     def sound(self):  # object method (executable only from an object of the class)
#         print("Vrooom!!!")


# my_vehicle = Vehicle(6)
# my_vehicle.sound()  # ->  same as  sound(my_car)
# print(my_vehicle.wheels)
