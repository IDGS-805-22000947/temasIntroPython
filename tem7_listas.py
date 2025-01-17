

#listas

lista1=[10,5,3]
lista2=[1.5,2.66,1.70,89.2]
lista3=["Lunes", "Martes", "Miercoles", "Jueves"]
lista4=["Juan", 45, 1.92]

print(type(lista1))
print(len(lista1))

print(lista1[0])

x=0
suma=0
while x<len(lista1):
    suma=suma+lista1[x]
    x=x+1

print("La suma es: {}".format(suma))  # ?????

print(lista1)
print(lista1[0])
lista1.append(100)
print(lista1)
print(lista1[3])


lista5=[]

for x in range(5):
    valor=int(input("Ingresa valor: "))
    lista5.append(valor)

print(lista5)



#Elimknar elementos de una lista

print(lista1)
lista1.pop()
print(lista1)



#Crear un programa pedir una cantidad de numeros y almacenarlos en un arreglo la salida debara ser la siguiente:
# Lista completa:
# Numeros pares de la lista:
# Numero impares de la lista:
listaOr = []
for x in range(4):
    numero = int(input("Dame unumeros enteros: "))
    listaOr.append(numero)
print("Lista completa:")
print(listaOr)



lista1.sort()#ordenar lista
print(lista1)
lista1.reverse()
print(lista1)

lista1.remove(10)
print(lista1) # ?

lista1.clear()
print(lista1) # ?


