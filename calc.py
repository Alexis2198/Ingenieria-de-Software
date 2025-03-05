# # Estoy definiendo la variable num1 = 5
# num1 = 5

# # Estoy definiendo la variable num2 = 3
# num2 = 3

# #Estoy imprimiendo la suma de num1 + num2 
# print(num1 + num2)


# print("La suma de ",num1," + ",num2, " es igual a ",num1 + num2) # Se imprime la suma de los dos números
# print("La resta de ",num1," + ",num2, " es igual a ",num1 - num2) # Se imprime la resta de los dos números
# print("La multiplicacion de ",num1," + ",num2, " es igual a ",num1 * num2) # Se imprime la multiplicación de los dos números

# #Se verifica si el segundo número es distinto de 0 para realizar la division
# if num2!= 0:
#     print("La division de ",num1," + ",num2, " es igual a ",num1 / num2)
# else:
#     print("No se puede realizar la division por cero")
    
# print("La potencia de ",num1," + ",num2, " es igual a ",num1 ** num2)

#Titulos
print("\t\t\tIngenieria de software")
print()
print("\t\t\tCALCULADORA BÁSICA")
print()

#Entrada de datos
num1 = float(input("Ingrese el primer numero: ")) # Se solicita al usuario que ingrese un número
num2 = float(input("Ingrese el segundo numero: ")) # Se solicita al usuario que ingrese un número
print()

#Definiciones de funciones 
def sum(num1, num2):
    print("La suma de ",num1," + ",num2, " es: ",num1 + num2)
def resta(num1, num2):
    print("La resta de ",num1," + ",num2, " es: ",num1 - num2)
def mult(num1, num2):
    print("La multiplicacion de ",num1," + ",num2, " es: ",num1 * num2)

def div(num1, num2):
    if num2 != 0:
        print("La division de ",num1," + ",num2, " es: ",num1 / num2)
    else:
        print("No se puede realizar la division por cero")

# Se llama a la funcion suma
sum(num1, num2)
print()

# Se llama a la funcion resta
resta(num1,num2)
print()

#Se llama a la funcion multiplicacion
mult(num1,num2)
print()

#Se llama a la funcion division
div(num1, num2)
