si_targeta_valida = 1
no_targeta_valida = 0
si_huella_dactilar = 1
no_huella_dactilar = 0
print (bool (si_targeta_valida ^ si_huella_dactilar))
print (bool (si_targeta_valida ^ no_huella_dactilar))
print (bool (no_targeta_valida ^ si_huella_dactilar))
print (bool (no_targeta_valida ^ no_huella_dactilar))