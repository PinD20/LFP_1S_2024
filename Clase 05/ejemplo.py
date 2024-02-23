#Estudiantes
202004707:"Juanito"


#Notas
202004707: 10, 50, 100, 90


#Programa

#Ejemplo clase Estudiante
class Estudiante:
    def __init__(self, carnet, nombre):
        self.carnet = carnet
        self.nombre = nombre
        self.notas = []

    def agregarNota(self, nota):
        self.notas.append(nota)

    def calcularPromedio(self):
        suma = 0
        for nota in self.notas:
            suma += nota
        return suma / len(self.notas)

#Agregar estudiantes
estudiantes = {202004707: Estudiante(202004707, "Juanito")}

#Agregar notas
estudiantes[202004707].agregarNota(10)