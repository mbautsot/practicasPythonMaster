x=3
y=5
z=10

print(f"{x} + {y} es igual a {x+y}")
print(f"{x} - {y} es igual a {x-y}")
print(f"{x} x {y} es igual a {x*y}")

#Division el typo resultante es un FLOAT
print(f"{z} / {y} es igual a {z/y}")
print(type(z/y)) #Resultado FLOAT

#Division entera sin decimales
print(f"{z} / {y} es igual a {z//y}")
print(type(z//y)) #Resultado INT

#Division MODULO O RESIDUO
print(f"{x} / {y} es igual a {x%y}")


#Elevar numero a cualquier factor
print(f"{x} elevado a la {y} es igual a {x**y}")

#Raiz cuadrada
print(f"La raiz cuadrada de {x} es : {x**0.05}")


numero = 783
raiz_cuadrada = numero ** 0.5
print(raiz_cuadrada)

num1 = round(13/2)
print(num1)
print(type(num1))

num2 = round(13/2,0)
print(num2)
print(type(num2))




