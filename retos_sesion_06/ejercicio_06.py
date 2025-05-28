# ¿El cubo de 300 se encuentra en el siguiente rango? 
# [N > 0 & N < 27_000_000]

num = 300**3
en_el_rango = num>0 and num<27_000_000
print (num, "= ¿el numero esta en el rango?")
print (bool (en_el_rango))