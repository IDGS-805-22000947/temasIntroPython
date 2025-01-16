
## VARIABLES INT, FLOAT, STRING, NO EXISTE EL TIPADO POR DEFECTO

num1=2
num2=3.5
nombre="Mario"
print()

(print("Dame un numero: "))
numero=input('numero: ')

def tabla(numero):
    for i in range(1, 11):  # Recorre del 1 al 10
        resultado = i * numero
        print(f"{i} x {numero} = {resultado}")

# Ejemplo de uso

