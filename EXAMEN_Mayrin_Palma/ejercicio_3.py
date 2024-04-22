numero = int(input("ingrese un numero: "))

i = 1
while i < 201:
    if i % numero == 0:
        print(f"{i} / {numero} divisible")
    else:
        print(f"{i} / {numero} no es divisible")
    i += 1

# numero = int(input("ingrese un numero: "))

# i = 1
# while i < 201:
#     if (i % numero == 0):
#         print(f'{i} es divisible')
#     else:
#         print(f'{i} no es divisible')
#     i += 1