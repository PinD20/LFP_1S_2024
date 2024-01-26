#Esto es un comentario de una línea

"""
Comentario de
varias líneas
"""

'''
Comentario multilínea
con comillas simples
'''

#Imprimir
print("Hola mundo")

#Declarar variables
variable1 = 55.2

#Concatenar, forma 1
#print("El valor de mi variable es: " + str(variable1))

#Concatenar, forma 2
#print("El valor de la variable 1 es:", variable1, "unidades")

#Concatenar, forma 3
variable2 = 7
print(f"El valor de la variable 1 es: {variable1} unidades y variable 2 es: {variable2}")

#Asignación de variables, el tipo de variable puede cambiar
variable1 = "diez"
print("El nuevo valor de variable 1 es:", variable1)

#Asignación con operaciones
numero = 4*8/60 - 15
print(f"Número asignado con operaciones: {numero}")


#Divisón siempre devuelve un float en Python
print(10/2)
print(1.2/1)
print(5/5.9)
print(5.8/7.8)

#Tipos de datos
entero = 5
decimal = 5.789789
booleano1 = True
booleano2 = False

print(booleano1, booleano2)

#Listas

#Declaración de listas
lista1 = [1, "texto1", 90, 80.5]

#Impresión de listas
print(lista1)

#Imprimir un elemento de la lista
print(lista1[1])

#Imprimir último elemento de la lista
print(lista1[-1])

#Agregar elementos al final de la lista
lista1.append(45.7)


#Insertar elemento en la lista
lista1.insert(1, "nuevo texto")

lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#Agregar elementos de una lista a otra
lista1.extend(lista2)

#Tamaño de una lista
print("tamaño de la lista: " + str(len(lista2)))

#Tuplas
tupla1 = (1, "precio", 5.8)

#Una tupla no puede ser editada luego de ser declarada
#tupla1[1] = "nuevo texto" #Esto genera error
print(tupla1)


#Condicionales

#If
if 5 > 0:
    print("Es cierto")
else:
    print("No es cierto")

#if else if
if 0 == 5:
    print("Primera")
elif 0 == 0:
    print("Segunda")
else:
    print("Tercera")

#Ciclos
#For
for i in range(0, 10):
    print(i)

#For con paso 2
for i in range(0, 10, 2):
    print(i)


listaFor = ["a", "b", "c", "d"]
for element in listaFor:
    print(element)

string = "Palabra"
for letra in string:
    print("Deletreando: " + letra)



