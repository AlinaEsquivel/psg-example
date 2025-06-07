# 1. removeprefix(): elimina el prefijo especificado al inicio de la cadena, si existe.
texto = "Pythonista_Anibal"
resultado = texto.removeprefix("Pythonista_")
print("removeprefix:", resultado)

# 2. removesuffix(): elimina el sufijo especificado al final de la cadena, si existe.
archivo = "informe_final.pdf"
resultado = archivo.removesuffix(".pdf")
print("removesuffix:", resultado)

# 3. casefold(): convierte la cadena a minúsculas "fuertes", útil para comparaciones Unicode sin distinción de mayúsculas/minúsculas.
palabra1 = "straße"
palabra2 = "STRASSE"
print("casefold:", palabra1.casefold() == palabra2.casefold())

# 4. zfill(): rellena la cadena con ceros a la izquierda hasta alcanzar el largo especificado.
numero = "42"
resultado = numero.zfill(5)
print("zfill:", resultado)

# 5. partition(): divide la cadena en una tupla (antes, separador, después) usando la primera aparición del separador.
texto = "clave:valor"
antes, separador, despues = texto.partition(":")
print("partition:", antes, separador, despues)
