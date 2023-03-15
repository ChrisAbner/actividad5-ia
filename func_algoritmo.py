# Funciones que se necesitan para el algoritmo de búsqueda

def hacer_nodo(
    estado: tuple[int, int], 
    distancia_al_objetivo: float, 
    i_padre: int,
    nodos: list,
    costo_entre_estado_padre: int
):
    """
    Almacena el índice del nodo actual y el índice del nodo padre.
    i_ padre sólo es -1 cuando es el nodo raíz.
    """
    costo = nodos[i_padre][4] + costo_entre_estado_padre
    nodo = [estado, len(nodos), i_padre, nodos[i_padre][3] + 1, costo, costo + distancia_al_objetivo]
    
    return nodo


def reconstruye(nodo: list, nodos: list[list]):
    """
    Reconstruye la lista de acciones en orden para hallar la solución.
    """
    solucion = []
    
    # mientras el indice del nodo no sea 0
    while nodo[1] != 0:
        # insertar la coordenada (estado) del nodo en la posicion 0 de solucion
        solucion.insert(0, nodo[0])
        # nodo es el nodo en la posicion del indice del padre de nodo
        nodo = nodos[nodo[2]]
        
    solucion.insert(0, nodo[0])
    
    return solucion
