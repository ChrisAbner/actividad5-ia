from busqueda_ruta_img import BusquedaRutaImg
from func_algoritmo import hacer_nodo, reconstruye

def main():
    # Consulta al usuario
    img_path = input("Escriba el path a la imagen a analizar: ")
    print("Escribe la estrategia que quieres seguir para la búsqueda escribiendo el número que corresponda")
    print("1: Búsqueda en Profundidad")
    print("2: Búsqueda en Amplitud")
    print("3: Búsqueda primero el mejor, por costos")
    print("4: Búsqueda A*")
    estrategia = input("Tu elección: ")
    
    '''
    img_path = "imgs/hilo2.png"
    estrategia = '1'
    '''
    
    # Inicia el problema a solucionar
    problema = BusquedaRutaImg(img_path)

    # INICIA PROCEDIMIENTO DE BÚSQUEDA #
    
    # esta lista guarda estados ya vistos
    visto = []
    
    # Para ahorrar memoria hacemos una lista que guarde todos los nodos
    nodos = [] # nodo = [estado, índice de este nodo, índice del padre, profundidad, costo, heurística de A*]
    
    # se declara la frontera como una lista vacía  
    frontera = []

    # INICIA ALGORITMO DE BÚSQUEDA DE ÁRBOLES #
    
    # crea nodo a partir del estado incial y lo inserta dentro de la frontera
    nodo_raiz = [problema.inicio, 0, -1, 1, 0, 0, problema.distancia_al_objetivo(problema.inicio)]
    
    nodos.append(nodo_raiz)
    frontera.append(nodo_raiz)

    # mientras la frontera no esté vacía
    while len(frontera) != 0:
        # saca un elemento de la frontera para explorar sus sucesores
        if estrategia == "1":
            nodo = frontera.pop()
        else:
            nodo = frontera.pop(0)  # pop(0) saca el primer elemento
            
        visto.append(nodo[0])
        
        if problema.es_objetivo(nodo[0]):
            print("*****solución encontrada*****")
            print(f"Pasos para llegar a la solución: {nodo[3] - 1}")
            print(f"Costo total de la solución: {nodo[4]}")
            print(f"Nodos totales explorados: {len(nodos)}")
            
            lista_estados_solucion = reconstruye(nodo, nodos)
            
            problema.en_pantalla(lista_estados_solucion)     
            
            break
        
        sucesores = problema.determinar_sucesores(nodo[0])
        
        for sucesor in sucesores:
            
            if not sucesor:
                continue
            
            if sucesor not in visto:
                visto.append(sucesor)
                
                nuevo_nodo = hacer_nodo(
                    sucesor, 
                    problema.distancia_al_objetivo(sucesor), 
                    nodo[1], 
                    nodos, 
                    problema.costo_entre_dos()
                )
                nodos.append(nuevo_nodo)
                
                if estrategia == "4":
                    # esta es una inserción ordenada
                    cuenta = len(frontera)
                    
                    for i in range(cuenta):
                        if nuevo_nodo[5] < frontera[i][5]:
                            frontera.insert(i, nuevo_nodo)
                            break
                        
                    if cuenta == len(frontera):
                        frontera.append(nuevo_nodo)
                        
                if estrategia == "3":
                    cuenta = len(frontera)
                    
                    for i in range(cuenta):
                        if nuevo_nodo[4] < frontera[i][4]:
                            frontera.insert(i, nuevo_nodo)
                            break

                    if cuenta == len(frontera):
                        frontera.append(nuevo_nodo)
                        
                if estrategia == "1" or estrategia == "2":
                    frontera.append(nuevo_nodo)
                    

if __name__ == "__main__":
    main()