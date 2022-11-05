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


from ast import main


class Alumno(): #creamos un clase
    def __init__(self, nombre, nota): #Constructor con los atributos
        self.nombre= nombre
        self.nota= nota
        print("Creaccion del usuario con éxito") #print para informar que la operacion ha sido éxito


    def calificacion(self): #definimos un metodo que evalue si la persona ha aprobado
        return "{} ha aprobado con un {}".format(self.nombre, self.nota) if self.nota >= 5 else "{} ha suspendido con un {}".format(self.nombre, self.nota)


#experimentación
nombre1=Alumno("Rosario", 7)
print(Alumno.calificacion(nombre1))
nombre2=Alumno("Cristina", 10)
print(Alumno.calificacion(nombre2))
nombre3=Alumno("Rosa", 3)
print(Alumno.calificacion(nombre3))


#importamos el ejercicio para que se ejecute en el main
if "__name__"=="__main__":
    main()

