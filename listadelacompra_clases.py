from typing import Any

class Producto:
    def __init__(self, nombre:str, precio:float, categorias:str, etiquetas:list[tuple], prioridad:int):
        self.nombre = nombre
        self.precio = precio
        self.categorias = categorias
        self.etiquetas = etiquetas
        self.prioridad = prioridad
        self.comprado = False
class ListaCompra:
    def __init__(self, productos:list[Producto]):
        self.productos = productos
    def insertar(self, producto:Producto)->None:
        """Esta función añade productos a la lista"""
        if producto not in self.productos:
            self.productos.append(producto)
    def borrar(self, producto)->None:
        """ Esta función borra productos de la lista"""
        if producto in self.productos:
            self.productos.remove(producto)
        else:
            print("Este producto no existe en la lista")
    def actualizar_precio(self, indice:int, precio:float):
        """Esta función cambia el precio de un producto de la lista"""
        ind = int(indice)
        self.productos[indice].precio = precio
    def ordenar(self) -> list[Producto]:
        '''
        Se ordena la lista de productos, poniendo aquellos con mayor prioridad al principio.
        Los productos ya comprados se colocal al final.
        '''

        for i in range(1, len(self.productos)):     #ordenar productos por prioridad
            producto_actual = self.productos[i]
            j = i - 1

        while j >= 0 and (
            self.productos[j].prioridad < producto_actual.prioridad or
             (self.productos[j].prioridad == producto_actual.prioridad and not self.productos[j].comprado and producto_actual.comprado)
        ):
            self.productos[j + 1] = self.productos[j]
            j -= 1                                               #desplazar productos con menor prioridad hacia la derecha

        self.productos[j + 1] = producto_actual                 #insertar el producto en su posición correcta
       

        for i in range(1, len(self.productos)):
            producto_actual = self.productos[i]
            j = i - 1

            while j >= 0 and self.productos[j].comprado and not producto_actual.comprado:
                self.productos[j + 1] = self.productos[j]
                j -= 1

            self.productos[j + 1] = producto_actual
            
            
    def cambiar_estado(self, indice:int):
        """Esta función cambia un producto a comprado/no comprado"""
        ind = int(indice)
        self.productos[ind].comprado = not self.productos[ind].comprado
    def mostrar_productos(self,comprados=True, etiquetas=(), categorias=[]):
        """Esta función muestra los productos de la lista"""
        for producto in self.productos:
            if comprados == False and producto.comprado: 
                continue
            if etiquetas: #verificamos si tiene algún elemento en la lista etiquetas, sino es así pasa automáticamente
                    tiene_eti = False
                    for etiqueta in etiquetas:
                        if etiqueta in producto.etiquetas:
                            tiene_eti = True #se encuentra esa etiqueta en producto[etiquetas], ya no hay que buscar, salir del bucle
                            break
                    if not tiene_eti: #si al final del bucle sigue siendo falso quiere decir que no coincide la etiqueta para ningún caso por lo que pasa al siguente producto(continue)
                        continue #L82 decide si se añade o se omite(si la bandera sigue siendo falsa, se pasa al sgte producto, sino se añade y se pasa al mensaje)
            if len(categorias)!= 0:
                if producto.categorias in categorias:
                    continue
            
            msg: str = ''
            if producto.comprado== True:
                msg += '[X] '
            else:
                msg += '[ ] '
            ast = "*"*producto.prioridad
            et = ''
            for etiqueta in producto.etiquetas:
                et += " #"+etiqueta #a cada etiqueta le atribuyo un # (así no limito los )
            msg += producto.categorias + " - " + producto.nombre + " - " + ast + " - " + str(producto.precio) + " - " + et
            print(msg)
def salir():
    """Esta función termina la ejecución del programa"""
    print("Adiós")  
    exit()
def ayuda(*params:Any):
    '''Esta función saca un mensaje de ayuda...'''
    print('No disponible. Escoja entre:')
    for nombre, funcion in funciones.items():
            print(nombre, "->", funcion.__doc__.strip())   
    
funciones: dict = {
    "mostrar": ListaCompra.mostrar_productos,
    "insertar": ListaCompra.insertar,
    "borrar": ListaCompra.borrar,
    "ordenar": ListaCompra.ordenar,
    "actualizar": ListaCompra.actualizar_precio,
    "comprado": ListaCompra.cambiar_estado,
    "ayuda": ayuda,
    "salir": salir
    }
def menu():
    lista = ListaCompra([])
    while True:
        orden = input("Introduce el comando: ")
        match orden.split():
            case [comando]:
                funcion = funciones.get(comando, ayuda)
                funcion()
            case [comando, *params]:
                funcion = funciones.get(comando, ayuda)
                params = [param.replace(';', '') for param in params]
                funcion(*params)
if __name__ == "__main__":
    menu()