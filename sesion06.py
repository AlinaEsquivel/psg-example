# print("Tipos de datos booleanos")
# print (True)
# print (False)
# Operaciones aritméticas con booleanos
# print (True + True)
# print (True * True)
# print (True * False)
# print (False + False)
# print (False * False)

# print ("")
# print ("Números y booleanos")
# print (210 + True)
# print (210 + False)
# print (210 * True)
# print (210 * False)

# print ("")
# print ("Declarar variables booleanas")
# var_booleana = True
# print (var_booleana)
# print (type(var_booleana))
# var_booleana = False
# print (var_booleana)
# print (type(var_booleana))

# print ("")
# print ("Declarar mediante función bool()")
# var_booleana = bool(1)
# print (var_booleana)
# print (type(var_booleana))
# var_booleana = bool(0)
# print (var_booleana)
# print (type(var_booleana))
# var_booleana = bool(15)
# print (var_booleana)
# print (type(var_booleana))

# print ("")
# print ("Operadores de comparación")
# print (10 == 10)
# print (10 != 10)
# print (10 < 10)
# print (10 > 10)
# print (10 <= 10)
# print (10 >= 10)
# Compara datos en memoria
# a = 10
# b = 10
# print (10 is 10)
# print (10 is not 10)

# print ("Asignación de variables")
# x = 10
# mayor_que_cero = x > 0
# print (mayor_que_cero)
# diferente_de_10 = x != 10
# print (diferente_de_10)

# print ("Operadores lógicos")
# print (True and True)
# print (True and False)
# print (False or True)
# print (False or False)
# print (not True)
# print (not False)

# print ("Operador AND")
# print (True and True)
# print (True and False)
# print (False and True)
# print (False and False)

# print ("Operador OR")
# print (2 or True)
# print (True or False)
# print (False or True)
# print (False or False)

# print ("Ejemplo de uso Sensor y Batería")
# sensor = True
# bateria = True
# print (sensor, "and", bateria, "=", sensor and bateria)
# sensor = True
# bateria = False
# print (sensor, "and", bateria, "=", sensor and bateria)
# sensor = False
# bateria = True
# print (sensor, "and", bateria, "=", sensor and bateria)
# sensor = False
# bateria = False
# print (sensor, "and", bateria, "=", sensor and bateria)

# numero = 20
# print (numero >= 0 and numero <= 100)

nota_1 = 15
nota_2 = 20
nota_3 = 16
nota_aprobacion = 50
print (nota_1 + nota_2 + nota_3 > nota_aprobacion)

nota_1 = 15
nota_2 = 20
nota_3 = 16
nota_total = nota_1 + nota_2 + nota_3
print(f"{nota_total=},", nota_total > 50)

notas = [15, 20, 16]
suma_notas = sum(notas)
aprobado = suma_notas > 50
print(f"Suma total de notas: {suma_notas}")
print(f"Aprobo con nota superior a 50? {aprobado}")

print ("")
num = 15
divisible_1 = num%3==0
divisible_2 = num%5==0
divisible_3 = num%2==1
print (divisible_1 and divisible_2 and divisible_3)

# corto circuito cuando el primero esta mal y ovbia todo