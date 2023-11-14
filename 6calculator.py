# Makine llogaritese qe kerkon input te vazhdueshem nga perdoruesi:
# - nese perdoruesi venods input "exit" atehere programi perfundon
# - nese perdoruesi venods input "+" atehere programi kerkon 2 inpute te tjera dhe ....
# - nese perdoruesi venods input "-" atehere programi kerkon 2 inpute te tjera dhe ....
# - nese perdoruesi venods input "/" atehere programi kerkon 2 inpute te tjera dhe ....
# - nese perdoruesi venods input "*" atehere programi kerkon 2 inpute te tjera dhe ....
# - nese perdoruesi venods input te pavlefshem athere
#   programi do i shfaqi nje mesazh gabimi dhe do kerkoj prap input

# while True:
#     operation = input("Vendosni operacionin qe doni te kryeni: (+, -, /, *)")
#     if operation == "exit":
#         break
#     elif operation in ["+", "-", "/", "*"]:
#         a = float(input("Vendosni numrin e pare: "))
#         b = float(input("Vendosni numrin e dyte: "))
#         # if operation == '+':
#         #     result = a + b
#         # elif operation == '-':
#         #     result = a - b
#         # elif operation == '/':
#         #     result = a / b
#         # else:
#         #     result = a * b
#         ### or this...
#         result = eval(f"{a}{operation}{b}")
#         print(f"Rezultati: {result}")
#     else:
#         print("Inputi eshte i gabuar...")