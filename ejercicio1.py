"""
Ejercicio 1
Creación
Crea una clase llamada Alumno que tenga los atributos nombre y nota
Crea el constructor de la clase. Añadir en el constructor un print 
para informar de que el alumno se ha creado con éxito
Crear un método llamado calificacion que imprima por pantalla 
si el alumno ha aprobado o suspendido en base a su nota
Experimentación
Crea algunos alumnos
Prueba a ejecutar el método calificacion de cada objeto que has creado
"""
class Alumno():
    def __init__(self, nombre, nota):
        self.nombre= nombre
        self.nota= nota
        print("Creaccion del usuario con éxito")


    def calificacion(self):
        return print("{} ha aprobado con {}".format(self.nombre, self.nota)) if self.nota >= 5 else print("{} ha suspendido con {}".format(self.nombre, self.nota))


if "__name__"=="__main__":
    nombre1=Alumno("Rosario", 7)
    Alumno.calificacion(nombre1)
    nombre2=Alumno("Petra", 10)
    Alumno.calificacion(nombre2)
    nombre3=Alumno("Rosa", 3)
    Alumno.calificacion(nombre3)
