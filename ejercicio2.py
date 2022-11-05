"""
Ejercicio 2
Creación
Copia el ejercicio anterior y realicemos una modificación:
Junto al método init y calificacion, vamos a crear otro método especial de Python, el método str. Al igual que init, debe ir encerrado entre dobles guiones bajos, y debe tener el siguiente formato:
def __str__(self): return "Lo que quiero mostrar"
Este método nos sirve para imprimir por pantalla la información de un objeto, si tenemos un objeto alumno1 creado y realizamos print(alumno1), Python ejecutará el contenido del método str (el método str lo que tiene que hacer es maquetar la información que desea en un string).
Experimentación
Implementa el método str y haz que muestre el nombre y la nota del alumno
Crea algun objeto de la clase Alumno
Realiza print de esos objetos para visualizar por pantalla la información del str
"""

class Alumno2():
    def __init__(self, nombre, nota):
        self.nombre= nombre
        self.nota= nota
        


    def calificacion(self):
        return print("{} ha aprobado con {}".format(self.nombre, self.nota)) if self.nota >= 5 else print("{} ha suspendido con {}".format(self.nombre, self.nota))

    def __str__(self):
        print("{} ha sacado un {}".format(self.nombre, self.nota))
        return 

nombre1=Alumno2("Rosario", 7)
nombre1.__str__()