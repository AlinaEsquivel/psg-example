cadena = input("Ingresa una cadena: ")

cadena_minuscula = cadena.lower()

lista_por_espacios = cadena_minuscula.split(" ")

cadena_unida = "".join(lista_por_espacios)


print(cadena_unida)


print(cadena_unida == cadena_unida[::-1])
