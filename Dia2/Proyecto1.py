nombre=(input("¿Cual es tu Nombre? :"))
ventas = float(input("¿Cual fue el monto total de ventas que generaste?:"))
comision = round((ventas * 13)/100,2)

print(f"Muy bien {nombre}, este es el monto de comision que ganaste : {comision} , !Felicidades¡")