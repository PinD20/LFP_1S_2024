#Continuación Ciclos

#For - else
print("For - else")
for i in range(0, 5):
    print("número:", i)
else:
    print("Fin del ciclo")

#While
print("While")
tmp = 10
while tmp > 0:
    print(tmp)
    tmp -= 1

#Diccionarios
print("Diccionarios")
#Los diccionarios funcionan como clave-valor
diccionario = {"clave1": 1, "clave2": "texto", "clave3": 5.8}
#La clave puede ser de cualquier tipo de dato

#Obtener un elemnto según su clave
print(diccionario["clave1"])

#Agregar un elemento
diccionario["clave4"] = 45
print(diccionario)


#Funciones
def miFuncion():
    return "Hola, llamaste a mi primer función"

def suma(n1, n2, n3):
    return n1 + n2 + n3


def suma2(n1: int, n2: int, n3: int) -> int:
    return n1 + n2 + n3

print(suma2(5, 10, 15.5))


#OBJETOS

#Creación de una clase
class Persona:
    #Constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años")


#Instanciar un objeto
persona1 = Persona("Pedro", 30)
persona1.saludar()

#Cambiar un atributo de un objeto
persona1.nombre = "Juan"
persona1.saludar()

#Acceder a un atributo de un objeto
print(persona1.nombre)

#ARCHIVOS
archivo = open("hola.txt", "r", encoding="utf-8")
#Permisos de apertura de archivos
#Sólo lectura: "r"
#Lectura y escritura: "r+"
#Sólo escritura: "w"
#Sólo escritura, posicionándose al final del archivo: "a"
#Lectura y escritura, posicionándose al final del archivo: "a+"

lineas = archivo.readlines() #Retorna una lista con todas las líneas del archivo
for l in lineas:
    #La parte de "[:-1] es para quitar el salto de línea al final de cada línea"
    if l[-1] == "\n":
        print(l[:-1])
    else:
        print(l)


#Leer todo el archivo en una sola cadena
txt = archivo.read()
#Recorrer por caracter
for c in txt:
    print(c)

archivo.close() #Cerrar el archivo


#Escritura de archivos
archivoNuevo = open("archN.txt", "w", encoding="utf-8")
variableTexto = "Hola, este es un archivo nuevo\n"
variableTexto += "Otra línea\n"

#Escribir en archivo
archivoNuevo.write(variableTexto)

archivoNuevo.close()