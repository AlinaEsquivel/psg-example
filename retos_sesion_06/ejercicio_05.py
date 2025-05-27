num1 = 44
num2 = 98
num3 = 111
num4 = 333
print ("Pares")
print (bool (num1%2==0 and num2%2==0))
print (bool (num1%2==0 and num3%2==0))
print (bool (num1%2==0 and num4%2==0))
print (bool (num2%2==0 and num3%2==0))
print (bool (num2%2==0 and num4%2==0))
print (bool (num3%2==0 and num4%2==0))

print("")
print ("Impares")
print (bool (num1%2==1 and num2%2==1))
print (bool (num1%2==1 and num3%2==1))
print (bool (num1%2==1 and num4%2==1))
print (bool (num2%2==1 and num3%2==1))
print (bool (num2%2==1 and num4%2==1))
print (bool (num3%2==1 and num4%2==1))
