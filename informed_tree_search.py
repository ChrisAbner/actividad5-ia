import math


class AradBucarest:
    """
    las siguientes funciones definen al problema. Si se quiere usar el mismo algoritmo en este
    código para resolver otro problema, se plantea el nuevo problema con las mismas 6 funciones,
    con el mismo nombre.
    """

    def __init__(self, ruta_objetivo):
        self.estado_inicial = ruta_objetivo[0]
        self.objetivo = ruta_objetivo[1]
        self.ciudades = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "L", "M", "N", "O", "P", "R", "S", "T", "U", "V",
                         "Z"]
        self.sucesores = [["T", "S", "Z"], ["F", "G", "P", "U"], ["D", "P", "R"], ["C", "M"], ["H"], ["B", "S"], ["B"],
                          ["E", "U"], ["N", "V"], ["M", "T"], ["D", "L"], ["I"], ["S", "Z"], ["B", "C", "R"],
                          ["C", "P", "S"], ["A", "F", "O", "R"], ["A", "L"], ["B", "H", "V"], ["I", "U"], ["A", "O"]]
        self.costos_ind = [[118, 140, 75], [211, 90, 101, 85], [120, 138, 146], [120, 75], [86], [211, 99], [90],
                           [86, 98], [87, 92], [70, 111], [75, 70], [87], [151, 71], [101, 138, 97], [146, 97, 80],
                           [140, 99, 151, 80], [118, 111], [85, 98, 142], [92, 142], [75, 71]]
        print("En esta ocasión se busca el camino:")
        self.en_pantalla(self.estado_inicial)
        self.en_pantalla(self.objetivo)

    def en_pantalla(self, estado):
        if estado == self.objetivo:
            print(estado)
            return

        print("{} ->".format(estado), end=' ')

    def test_objetivo(self, estado):
        if estado == self.objetivo:
            return 1
        return 0

    def funcion_sucesor(self, estado):
        return self.sucesores[self.ciudades.index(estado)]

    def costo_entre_dos(self, estado1, estado2):
        i = self.ciudades.index(estado1)
        j = self.sucesores[i].index(estado2)
        return self.costos_ind[i][j]

    def distancia_al_objetivo(self, estado):
        i = self.ciudades.index(estado)
        j = self.ciudades.index(self.objetivo)
        coordenadas = [[44.82029, 279.40248], [401.54287, 90.12111], [230.46163, 43.40744], [129.14757, 57.96755],
                       [585.97086, 48.86748], [292.34208, 231.47547], [371.20931, 24.60064], [554.42397, 114.99463],
                       [485.87014, 295.7826], [129.75424, 148.36153], [132.18092, 103.46788], [408.21625, 331.57619],
                       [91.53396, 371.61648], [309.93554, 136.22811], [208.0148, 185.36847], [178.89459, 240.57553],
                       [47.85365, 185.97514], [465.85, 114.99463], [525.91043, 223.58874], [65.44711, 326.72282]]
        x1 = coordenadas[i][0]
        x2 = coordenadas[j][0]
        y1 = coordenadas[i][1]
        y2 = coordenadas[j][1]
        return math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))


###funciones que se necesitan para el algoritmo de búsqueda

# Aquí cambiamos la función de hacer_nodo. Almacena el índice del nodo actual y el índice del nodo padre
# nodo = [estado, índice de este nodo, índice del padre, profundidad, costo, heurística de A*]
# i_ padre sólo es -1 cuando es el nodo raíz
def hacer_nodo(estado, i_padre):
    d = problema.distancia_al_objetivo(estado)
    if i_padre == -1:
        n = [estado, 0, -1, 1, 0, 0, d]
    else:
        c = nodos[i_padre][4] + problema.costo_entre_dos(estado, nodos[i_padre][0])
        n = [estado, len(nodos), i_padre, nodos[i_padre][3] + 1, c, c + d]
    nodos.append(n)
    return n


# esta función reconstruye la lista de acciones en orden para hallar la solución
def reconstruye(nodo):
    solucion = []
    n = list(nodo)
    while n[1] != 0:
        solucion.insert(0, n)
        n = nodos[n[2]]
    solucion.insert(0, n)
    for x in solucion:
        problema.en_pantalla(x[0])


# esta función la puse aquí para revisar la lista de estados ya visitados
def dentro_de(estado, lista_de_estados):
    rep = 0
    for y in lista_de_estados:
        eq = 0
        for i in range(len(estado)):
            if estado[i] != y[i]:
                break
            eq = eq + 1
        if eq == len(estado):
            # print("repetido encontrado")
            return 1
    return 0


# consulta al usuario
A = input("Escribe la inicial, en mayusculas y sin espacios, del estado del que quieres partir: ")
B = input("Escribe el objetivo: ")
print("Escribe la estrategia que quieres seguir para la búsqueda. Elige escribiendo el número que corresponde")
print("1: Búsqueda en Profundidad")
print("2: Búsqueda en Amplitud")
print("3: Búsqueda primero el mejor, por costos")
print("4: Búsqueda A*")
E = input("Tu elección: ")
######## Inicia el problema a solucionar
problema = Arad_Bucarest([A, B])

####### INICIA PROCEDIMIENTO DE BÚSQUEDA
# esta lista guarda estados ya vistos
visto = []
# Para ahorrar memoria hacemos una lista que guarde todos los nodos
nodos = []
# se declara la frontera como una lista vacía  
frontera = []

######INICIA ALGORITMO DE BÚSQUEDA DE ÁRBOLES
# crea nodo a partir del estado incial y lo inserta dentro de la frontera
frontera.append(hacer_nodo(problema.estado_inicial, -1))

# mientras la frontera no esté vacía
while len(frontera) != 0:
    # saca un elemento de la frontera para explorar sus sucesores
    if E == "1":
        nodo = frontera.pop()  # 0 saca el primero
    else:
        nodo = frontera.pop(0)  # 0 saca el primero
    visto.append(nodo[0])
    if problema.test_objetivo(nodo[0]) == 1:
        print("*****solución encontrada*****")
        print("Pasos para llegar a la solución: {}".format(nodo[3] - 1))
        print("Costo total de la solución: {}".format(nodo[4]))
        reconstruye(nodo)
        break
    else:
        sucesores = problema.funcion_sucesor(nodo[0])
        for x in sucesores:
            if dentro_de(x, visto) == 0:
                nuevo_nodo = hacer_nodo(x, nodo[1])
                if E == "4":
                    # esta es una insención ordenada
                    cuenta = len(frontera)
                    for i in range(cuenta):
                        if nuevo_nodo[5] < frontera[i][5]:
                            frontera.insert(i, nuevo_nodo)
                            break
                    if cuenta == len(frontera):
                        frontera.append(nuevo_nodo)
                if E == "3":
                    cuenta = len(frontera)
                    for i in range(cuenta):
                        if nuevo_nodo[4] < frontera[i][4]:
                            frontera.insert(i, nuevo_nodo)
                            break
                    if cuenta == len(frontera):
                        frontera.append(nuevo_nodo)
                if E == "1" or E == "2":
                    frontera.append(nuevo_nodo)
print("búsqueda finalizada con {} nodos explorados".format(len(nodos)))
