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

from ast import main


class Alumno_copy(): #creamos un clase con los atributos deseados
    def __init__(self, nombre, nota):#Constructor con los atributos
        self.nombre= nombre
        self.nota= nota
        


    def calificacion(self): #definimos un metodo que evalue si la persona ha aprobado
        return "{} ha aprobado con {}".format(self.nombre, self.nota) if self.nota >= 5 else "{} ha suspendido con {}".format(self.nombre, self.nota)

    def __str__(self): #utilizamos __str__ para mostrar la información
        return "{} ha sacado un {}".format(self.nombre, self.nota)
 
#experimentación
nombre1=Alumno_copy("Rosario", 7)
print(str(nombre1))
nombre2=Alumno_copy("Cristina", 10)
print(str(nombre2))


#importamos el ejercicio para que se ejecute en el main
if __name__=="__main__":
    main()