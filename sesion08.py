print ("Tupla de enteros")
enteros = (1,2,3,4,5,6)
print (enteros)
print (type(enteros))

print ("")
print ("Tupla de cadenas")
cadenas = ("hola","mundo","desde","python")
print (cadenas)
print (type(cadenas))

print ("")
print ("Tupla de mixta")
mixta = (1, "hola", True, 2.5)
print (mixta)
print (type(mixta))

print ("")
print ("Tupla de vacia")
vacia = ()
print (vacia)
print (type(vacia))

print ("")
print ("Tupla de un elemento")
uno = (1,)
print (uno)
print (type(uno))

print ("")
print ("Tupla utilizando la funcion tuple ()")
constructor = tuple("Hola")
print (constructor)
print (type(constructor))

print ("")
print ("indexado positivo de una tupla")
tupla = (1,2.0,"hola", True)
print (tupla[0], type(tupla[0]))
print (tupla[1], type(tupla[1]))
print (tupla[2], type(tupla[2]))
print (tupla[3], type(tupla[3]))

print ("")
print ("indexado positivo de una tupla")
tupla = (1,2.0,"hola", True)
print (tupla[-1], type(tupla[-1]))
print (tupla[-2], type(tupla[-2]))
print (tupla[-3], type(tupla[-3]))
print (tupla[-4], type(tupla[-4]))

print ("")
print ("Slicing de una tupla")
tupla = (0,1,2,3,4,5,6,7,8,9,10)
print (tupla)
sub_tupla = tupla[0:5]
print (sub_tupla)
print (type(sub_tupla))

#pasos de 2
print ("")
print ("Slicing de una tupla")
tupla = (0,1,2,3,4,5,6,7,8,9,10)
print (tupla)
sub_tupla = tupla[0:10:2]
print (sub_tupla)
print (type(sub_tupla))

#pasos de 2
print ("")
print ("Slicing de una tupla")
tupla = (0,1,2,3,4,5,6,7,8,9,10)
print (tupla)
sub_tupla = tupla[7:2:-2]
print (sub_tupla)
print (type(sub_tupla))

print ("Concatenacion de tuplas")
tupla1 = (1,2,3)
tupla2 = (4,5,6)
concatenar = tupla1 + tupla2
print (tupla1, tupla2)
print (concatenar)
print (type(concatenar))

print ("")
print ("Repetir tuplas")
tupla = (1,2,3)
repetir = tupla * 3
print (tupla)
print (repetir)
print (type(repetir))

print ("")
print ("Asignacion multiple")
persona = ("Jhon", "Doe", 22, 1.75)
nombre, apellido, edad, estatura = persona
print (persona)
print (nombre)
print (apellido)
print (edad)
print (estatura)

#Nos dice en que posicion esta
print ("")
print ("Metodo Index(valor)")
tupla = (1,2.0, "hola", True)
print (tupla.index(2.0))
print (tupla.index("hola"))

#Nos dice cuantas veces aparece un valor 
#el True cuneta como 1
print ("")
print ("Metodo count (valor)")
tupla = (1,2.0, "hola", True, "hola", "HOLA")
print (tupla.count(1))
print (tupla.count("hola"))
print (tupla.count(10))

print("")
print ("Función len()")
tupla = (1,2.0, "hola", True)
longitud = len(tupla)
print (tupla)
print (longitud)

print ("")
print ("Función max()")
tupla = (1,2,10,5,8,0)
maximo = max(tupla)
print (tupla)
print (maximo)

print ("")
print ("Función min()")
tupla = ("a","z","c","b","f","d")
minimo = min(tupla)
print (tupla)
print (minimo)

print ("")
print ("Función sum()")
tupla = (1.0, 0.5, 2.5, 3.1)
suma = sum(tupla)
print (tupla)
print (suma)

print ("")
print ("Tuplas anidadas")
tupla = (1,2,3, (4,5,6))
print (tupla)
print (tupla, type(tupla))
print (tupla[3], type(tupla[3]))
print (tupla[3][0], type(tupla[3][0]))

print ("")
print ("Tuplas anidadas")
tupla = (1,2,3, (4,5,6))
print (tupla, type(tupla))
anidado = tupla[3]
print (anidado, type(anidado))
valor_anidado_0 = anidado[0]
print (valor_anidado_0, type(valor_anidado_0))
valor_anidado_1 = tupla[3][1]
print (valor_anidado_1, type(valor_anidado_1))

