"""
jercicio 3
Creación
Crea una clase llamada Producto que tenga los atributos codigo, nombre, precio y tipo.
Crea el constructor de la clase. Añadir en el constructor un print para informar de que el producto se ha creado con éxito
Crea el método __str__ para visualizar por pantalla la información de los productos
Experimentación
Crea algunos productos
Prueba a mostrar los datos de algun producto y a modificar algun valor, por ejemplo, prueba a modificar el precio de un producto
"""

from ast import main 


class Producto(): #creamos un clase y definimos los atributos 
    def __init__(self, codigo, nombre, precio, tipo):#Constructor con los atributos
        self.codigo=codigo
        self.nombre=nombre
        self.precio=precio
        self.tipo=tipo
        print("Producto creado éxitosamente") #print para informar que la operacion ha sido éxito
    
    def __str__(self): #utilizamos __str__ para mostrar la información
        return "{} es el código de barras del producto {}, tiene un coste de {}€ y es de un articulo tipo {}.".format(self.codigo, self.nombre, self.precio, self.tipo)


#Experimentación
producto1=Producto(8480000104892, "Leche", 2.4, "Lácteos")
producto2=Producto(7501000120253, "Pan Bimbo", 1.49, "Panadería")
print(str(producto1))
print(str(producto2))
print("---Bajada de precio de {}---".format((producto1.nombre))) 
producto1.precio=1.6 #modificamos el precio
print(str(producto1))

#importamos el ejercicio para que se ejecute en el main
if __name__=="__main__":
    main()
