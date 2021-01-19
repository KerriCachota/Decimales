# Area de la circunferencia
r = float(input("¿Qué radio tiene tu circunferencia? (intenta que el area no de más de 3 decimales)"))
area = float(3.1415 * r * r)
print("El area de tu circunferencia es:", area)

# Numero de cifras
x = (len(str(area)))
l = x - 1
print("El resultado tiene estas cifras: " + str(l))

# Posicion y numero de decimales
pos = str(area).find(".")
print("La posición de la coma es: " + str(pos))
dec = (l - pos)
print("Hay", dec, "decimales")

# Condición según los decimales
if (dec >= 3 and dec <= 5):
    print("¡Te has pasado!")
elif (dec > 5 and dec != 14):
    print("¡¿Dónde vas?!")
else:
    if (dec == 14):
        print("No has ganado pero has encontrado el numero secreto de decimales")
    else:
        print("¡Has ganado!")