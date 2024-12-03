'''
Módulo de gestión la lista de la compra

Un producto es un diccionario con las siguientes claves:

* nombre, prioridad, precio, etiquetas, categoria, comprado

Por ejemplo:

producto = {
  "nombre": "Huevo",
  "precio": 12.50,
  "etiquetas": ("huevos fritos", "empanada"),
  "categoria": "Alimentación",
  "comprado": False
}

En la parte 4 de está práctica veremos cómo transformar esto en una estructura más elegante.
'''
from typing import Any

productos: list[dict] = []

def insertar(nombre: str, precio: float, categoria: str, etiquetas: tuple[str]=(), prioridad: int = 3) -> None:
    '''Añade un producto nuevo a la lista con los parámetros dados'''
    if type(etiquetas) == str:
        etiquetas = tuple(etiquetas.split(','))
        
    producto: dict[str, Any] = {
        "nombre": str(nombre),
        "precio": float(precio),
        "categoria": str(categoria),
        "etiquetas": tuple(etiquetas),
        "prioridad": int(prioridad),
        "comprado": False
        }
    productos.append(producto)


def borrar(indice:int)-> None:
    '''Borra de la lista el producto que se encuentra en la posición indicada'''
    del productos[int(indice)]

def actualizar_precio(indice:int, precio:float)->None:
    '''Actualiza el precio del producto con el índice dado'''
    ind = int(indice)
    productos[ind]["precio"] = float(precio) #Como buscar dentro de un diccionario en una posicion específica de la lista

def cambiar_estado(indice: int) -> None:
    '''Cambia el estado del producto con el índice dado entre comprado o no'''
    indice = int(indice)
    productos[indice]["comprado"] = not productos[indice]["comprado"]
        
def mostrar_productos(comprados=True, etiquetas=(), categorias=[]):
    for producto in productos:
        if comprados == False and producto["comprado"]: 
                continue
        if etiquetas: #verificamos si tiene algún elemento en la lista etiquetas, sino es así pasa automáticamente
            tiene_eti = False
            for etiqueta in etiquetas:
                if etiqueta in producto["etiquetas"]:
                    tiene_eti = True #se encuentra esa etiqueta en producto[etiquetas], ya no hay que buscar, salir del bucle
                    break
            if not tiene_eti: #si al final del bucle sigue siendo falso quiere decir que no coincide la etiqueta para ningún caso por lo que pasa al siguente producto(continue)
                continue #L82 decide si se añade o se omite(si la bandera sigue siendo falsa, se pasa al sgte producto, sino se añade y se pasa al mensaje)
        if len(categorias)!= 0:
            if categorias and producto["categoria"] not in categorias:
                continue
        
        msg: str = ''
        if producto["comprado"]== True:
            msg += '[X] '
        else:
            msg += '[ ] '
        ast = "*"*producto["prioridad"]
        et = ''
        for etiqueta in producto["etiquetas"]:
            et += " #"+etiqueta #a cada etiqueta le atribuyo un # (así no limito los )
        msg += producto['categoria'] + " - " + producto['nombre'] + " - " + ast + " - " + str(producto["precio"]) + " - " + et
        print(msg)
def ordenar():
    '''
    Se ordena la lista de productos, poniendo aquellos con mayor prioridad al principio.
    Los productos ya comprados se colocal al final.
    '''

    for i in range(1, len(productos)):
        producto_actual = productos[i]
        j = i - 1                           #ordenar productos según prioridad

        while j >= 0 and productos[j]["prioridad"] < producto_actual["prioridad"]:
            productos[j + 1] = productos[j]
            j -= 1                                       #desplazar productos con menor prioridad hacia la derecha
        
        productos[j + 1] = producto_actual               #insertar el producto en su posición correcta

    for i in range(1, len(productos)):
        producto_actual = productos[i]
        j = i - 1

        while j >= 0 and productos[j]["comprado"] and not producto_actual["comprado"]:
            productos[j + 1] = productos[j]
            j -= 1

        productos[j + 1] = producto_actual
def ayuda(*params: Any) -> None:
    '''Esta función saca un mensaje de ayuda...'''
    print('No disponible. Escoja entre:')
    
    for nombre, funcion in funciones.items():
        print(nombre, "->", funcion.__doc__.strip())
    
def salir():
    '''Esta función hace que el programa termine.'''
    print("Adiós")
    exit()
    
funciones = {
  "mostrar": mostrar_productos,
  "insertar": insertar,
  "borrar": borrar,
  "ordenar": ordenar,
  "actualizar": actualizar_precio,
  "comprado": cambiar_estado,
  "ayuda":ayuda,
  "salir": salir
}
      

def menu():
    
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
        
def prueba_manual():
    print('Insertando 3 productos')
    insertar('Desmaquillante', 4.5, 'Cosméticos', ('fiesta', 'teatro'), 5)
    insertar('Garbanzos', 0.68, 'Alimentación', ('cocido', 'hummus'), 3)
    insertar('Hierbabuena', 1.5, 'Alimentación', ('cocktail', 'postres'), 1)
    actualizar_precio(1, 4.6)
    cambiar_estado(0)



if __name__ == "__main__":
    prueba_manual()
    menu()
