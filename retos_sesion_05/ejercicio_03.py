# Escribe un programa en Python que convierta 
# 1000000 de segundos en semanas, días, horas, 
# minutos y segundos

cantidad = 1000000
# Para los segundos
segundos = cantidad % 60
residuo_seg = cantidad // 60

# para los minutos
minutos = residuo_seg % 60
residuo_min = residuo_seg // 60

# Para horas
horas = residuo_min % 24
residuo_horas = residuo_min // 24

# Para dias
dias = residuo_horas % 7

# Para semanas
semana = residuo_horas//7

print ("Semanas:")
print ((semana))

print ("dias:")
print ((dias))

print ("horas:")
print ((horas))

print ("minutos:")
print ((minutos))

print ("segundos:")
print ((segundos))

