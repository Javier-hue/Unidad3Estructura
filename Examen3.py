class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def agregar_hijo(nodo_padre, valor_hijo):
    if nodo_padre.izquierdo is None:
        nodo_padre.izquierdo = NodoArbol(valor_hijo)
        return "Hijo izquierdo añadido."
    elif nodo_padre.derecho is None:
        nodo_padre.derecho = NodoArbol(valor_hijo)
        return "Hijo derecho añadido."
    else:
        return "El nodo ya tiene dos hijos."

def mostrar_arbol_completo(nodo, nivel=0):
    if nodo:
        print("    " * nivel + "- " + nodo.valor)
        mostrar_arbol_completo(nodo.izquierdo, nivel + 1)
        mostrar_arbol_completo(nodo.derecho, nivel + 1)

def localizar_nodo(nodo, valor_buscado):
    if nodo is None:
        return None
    if nodo.valor == valor_buscado:
        return nodo
    resultado_izq = localizar_nodo(nodo.izquierdo, valor_buscado)
    if resultado_izq:
        return resultado_izq
    return localizar_nodo(nodo.derecho, valor_buscado)

def renombrar_nodo(nodo, valor_actual, valor_nuevo):
    nodo_encontrado = localizar_nodo(nodo, valor_actual)
    if nodo_encontrado:
        nodo_encontrado.valor = valor_nuevo
        return "El nombre del nodo ha sido actualizado."
    else:
        return "Nodo no encontrado."

def borrar_nodo(nodo, valor_borrar):
    if nodo is None:
        return None, "Nodo no hallado."

    if nodo.izquierdo and nodo.izquierdo.valor == valor_borrar:
        nodo.izquierdo = None
        return nodo, "Nodo izquierdo eliminado."
    if nodo.derecho and nodo.derecho.valor == valor_borrar:
        nodo.derecho = None
        return nodo, "Nodo derecho eliminado."

    nodo.izquierdo, mensaje_izquierdo = borrar_nodo(nodo.izquierdo, valor_borrar)
    if mensaje_izquierdo != "Nodo no hallado.":
        return nodo, mensaje_izquierdo

    nodo.derecho, mensaje_derecho = borrar_nodo(nodo.derecho, valor_borrar)
    return nodo, mensaje_derecho

def listar_hijos(nodo):
    if not nodo or (nodo.izquierdo is None and nodo.derecho is None):
        return "El nodo no tiene hijos."
    
    lista_hijos = []
    if nodo.izquierdo:
        lista_hijos.append(nodo.izquierdo.valor)
    if nodo.derecho:
        lista_hijos.append(nodo.derecho.valor)
    return "Hijos: " + ", ".join(lista_hijos)

# Programa principal
raiz_arbol = None

while True:
    print("\nGestión del Árbol Genealógico")
    print("1. Crear nodo raíz")
    print("2. Añadir hijo")
    print("3. Visualizar árbol")
    print("4. Cambiar nombre de nodo")
    print("5. Eliminar nodo")
    print("6. Buscar nodo y ver hijos")
    print("7. Finalizar")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        if raiz_arbol is None:
            nombre_raiz = input("Introduce el nombre del nodo raíz: ")
            raiz_arbol = NodoArbol(nombre_raiz)
            print("Nodo raíz creado con éxito.")
        else:
            print("El nodo raíz ya existe y no puede ser cambiado.")
    
    elif opcion == "2":
        if raiz_arbol is None:
            print("Primero debes crear el nodo raíz.")
        else:
            nombre_padre = input("Introduce el nombre del nodo padre: ")
            nodo_padre = localizar_nodo(raiz_arbol, nombre_padre)
            if nodo_padre:
                if nodo_padre.izquierdo and nodo_padre.derecho:
                    print("El nodo ya tiene dos hijos. No se pueden agregar más.")
                else:
                    nombre_hijo = input("Introduce el nombre del hijo: ")
                    print(agregar_hijo(nodo_padre, nombre_hijo))
            else:
                print("Nodo padre no encontrado.")
    
    elif opcion == "3":
        if raiz_arbol is None:
            print("El árbol está vacío.")
        else:
            mostrar_arbol_completo(raiz_arbol)

    elif opcion == "4":
        if raiz_arbol is None:
            print("Primero debes crear el nodo raíz.")
        else:
            nombre_actual = input("Introduce el nombre actual del nodo: ")
            nuevo_nombre = input("Introduce el nuevo nombre: ")
            print(renombrar_nodo(raiz_arbol, nombre_actual, nuevo_nombre))

    elif opcion == "5":
        if raiz_arbol is None:
            print("Primero debes crear el nodo raíz.")
        else:
            nombre_eliminar = input("Introduce el nombre del nodo a eliminar: ")
            raiz_arbol, mensaje = borrar_nodo(raiz_arbol, nombre_eliminar)
            print(mensaje)

    elif opcion == "6":
        if raiz_arbol is None:
            print("Primero debes crear el nodo raíz.")
        else:
            nombre_busqueda = input("Introduce el nombre del nodo a buscar: ")
            nodo_encontrado = localizar_nodo(raiz_arbol, nombre_busqueda)
            if nodo_encontrado:
                print("Nodo localizado.")
                print(listar_hijos(nodo_encontrado))
            else:
                print("Nodo no localizado.")
    
    elif opcion == "7":
        print("Saliendo del programa.")
        break
    
    else:
        print("Opción no válida. Por favor, intenta de nuevo.")
