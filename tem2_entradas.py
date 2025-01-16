
'''
print("Dame dos números: ")
num1=input('Num1: ')
num2=input('Num2: ')
suma=int(num1)+int(num2)
print("La suma de los dos números es: ", suma)
print("La suma de {} + {} es: {}" .format(num1,num2,suma))

'''

def tabla():
    # Solicitar el número al usuario
    numero = int(input("Dame un numero: "))

    
    # Generar e imprimir la tabla de multiplicar
    for i in range(1, 11):
        print(f"{i} x {numero} = {i * numero}")

# Llamar a la función
tabla()