# Algoritmos de ordenamiento

def bubbleSort(numeros: list):
    n = len(numeros)
    for i in range(n):
        for j in range(n - i - 1):
            if numeros[j] > numeros[j + 1]:
                ''' La línea de abajo es equivalente a estas tres líneas
                temp = numeros[j]
                numeros[j] = numeros[j + 1]
                numeros[j + 1] = temp
                '''
                numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

def bubbleSortWithWhile(numeros: list):
    intercambio = True
    while intercambio:
        intercambio = False
        for i in range(len(numeros) - 1):
            if numeros[i] > numeros[i + 1]:
                numeros[i], numeros[i + 1] = numeros[i + 1], numeros[i]
                intercambio = True

def ordenamientoInsercion(numeros: list):
    for i in range(1, len(numeros)):
        actual = numeros[i]
        j = i - 1
        while j >= 0 and actual < numeros[j]:
            numeros[j + 1] = numeros[j]
            j -= 1
        numeros[j + 1] = actual

def ordenamientoSeleccion(numeros: list):
    for i in range(len(numeros)):
        indice_minimo = i
        for j in range(i + 1, len(numeros)):
            if numeros[j] < numeros[indice_minimo]:
                indice_minimo = j
        numeros[i], numeros[indice_minimo] = numeros[indice_minimo], numeros[i]

lista = [64, 34, 25, 12, 22, 11, 90]

ordenamientoSeleccion(lista)
print("Lista ordenada", lista)


# Algoritmos de búsqueda

def busqueda_lineal(objetivo: int, numeros: list):
    for num in numeros:
        if num == objetivo:
            return True
    return False

def busqueda_binaria(objetivo: int, numeros: list):
    if len(numeros) == 0:
        return False
    
    #El signo // divide pero redondea al entero más cercano
    medio = (len(numeros) - 1) // 2

    if objetivo == numeros[medio]:
        return True
    elif objetivo < numeros[medio]:
        return busqueda_binaria(objetivo, numeros[:medio])
    else:
        return busqueda_binaria(objetivo, numeros[medio + 1:])

lista2 = [50, 20, 15, 40, 10, 100, 30]

#print(busqueda_lineal(40, lista2))

print(busqueda_binaria(11, lista))