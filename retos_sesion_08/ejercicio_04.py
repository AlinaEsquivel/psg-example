#Notas de un estuduiante
print ("Las notas de un estudiante durante un semestre son:")
notas = (10, 61, 00, 21, 22, 0, 32, 30, 41, 51, 5, 23, 100)
print (notas)
suma = sum(notas)
cantidad = len(notas)
promedio = suma / cantidad
print ("¿el estudiante aprobo?: ", promedio)
print (promedio > 51)