#Hacer un programa que permita calcular la distancia sobre los dos puntos


import math

def calcularDistancia(punto1, punto2):

    x1, y1= punto1
    x2, y2= punto2

    distancia = math.sqrt((x2-x1)**2 + (y2 - y1)**2)
    return distancia

print("Dame el primer punto: ")
x1 = float(input("x1: "))
y1 = float(input("y1: "))

print("Dame el segundo punto: ")
x2 = float(input("x2: "))
y2 = float(input("y2: "))

punto1 = (x1, y1)
punto2 = (x2, y2)
distancia = calcularDistancia(punto1, punto2)

print(f"La distancia entre los puntos {punto1} y {punto2} es: {distancia:.2f}")
