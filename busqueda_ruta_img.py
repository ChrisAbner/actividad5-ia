import math
import cv2
import numpy as np
import numpy.typing as npt


class BusquedaRutaImg:

    def __init__(self, img_path: str):
        self.img = cv2.imread(img_path, cv2.IMREAD_COLOR)
        self.hilo = self._crear_hilo_desde_img(self.img)
        self.inicio = (0, 0)
        self.objetivo = (253, 253)

    def _crear_hilo_desde_img(self, img_matriz_3d: npt.NDArray) -> npt.NDArray:
        """
        Toma una matriz 3d ndarray de valores rgb  y los transforma en una matriz 2d
        ndarray con valor 1 cuando el rgb es 0,0,0 y 0 cuando el rgb es 255,255,255
        """
        nueva_matriz_2d = []

        for img_matriz_2d in img_matriz_3d:
            nueva_lista = [1 if img_lista.sum() == 0 else 0 for img_lista in img_matriz_2d]
            nueva_matriz_2d.append(nueva_lista)

        return np.array(nueva_matriz_2d, np.int32)

    def en_pantalla(self, lista_estados: list[tuple[int, int]]):
        """
        Cambia los colores de los pixeles recorridos a amarillo y
        abre una ventana con la imagen.
        """
        for coordenada in lista_estados:
            coordenada_derecha = (coordenada[0] + 1, coordenada[1])
            coordenada_abajo = (coordenada[0], coordenada[1] + 1)
            coordenada_abajo_derecha = (coordenada[0] + 1, coordenada[1] + 1)
            
            self.img[coordenada] = (0, 255, 255)
            
            if coordenada_derecha[0] <= 255:
                self.img[coordenada_derecha] = (0, 255, 255)
                
            if coordenada_abajo[1] <= 255:
                self.img[coordenada_abajo] = (0, 255, 255)
                
            if coordenada_abajo_derecha[0] <= 255 and coordenada_abajo_derecha[1] <= 255:
                self.img[coordenada_abajo_derecha] = (0, 255, 255)
            
            # show the image, provide window name first
            cv2.imshow('image window', self.img)
            # add wait key. window waits until user presses a key
            cv2.waitKey(1)
        # show the image, provide window name first
        cv2.imshow('image window', self.img)
        print("Presione cualquier tecla para continuar...")
        # add wait key. window waits until user presses a key
        cv2.waitKey(0)
        # and finally destroy/close all open windows
        cv2.destroyAllWindows()

    def es_objetivo(self, estado: tuple[int, int]) -> int:
        """
        Verifica si estamos en el objetivo
        """
        return 1 if estado[0] >= self.objetivo[0] and estado[1] >= self.objetivo[1] else 0

    def determinar_sucesores(self, estado: tuple[int, int]) -> list[tuple[int, int] | None]:
        """
        1. Se obtienen las coordenadas arriba, abajo, izquierda y derecha a partir del estado
        recibido.
        2. Se verifica si las coordenadas obtenidas son pixeles validos y si son pixeles negros.
        3. Se crea una lista con las 4 coordenadas y se retorna.
        
        * Se asume que estamos al limite de la imagen si recibimos estados que,
        restados 1, resultan en una coordenada x o y negativa.
        """

        def verificar_coordenada(coordenada: list[int, int]) -> tuple[int, int] | None:            
            """
            Verifica si una coordenada está al límite de la imagen
            y verifica si el pixel en la coordenada es un sucesor válido (1).
            """
            if coordenada[0] >= 0 and coordenada[1] >= 0:
                
                if coordenada[0] == 256:
                    coordenada[0] -= 1
                    
                if coordenada[1] == 256:
                    coordenada[1] -= 1
                    
                coordenada_tupla = tuple(coordenada)
                
                pixel = self.hilo[coordenada_tupla]
            
                if pixel:
                    return coordenada_tupla
                
            return None
        
        coordenada_arriba = [(estado[0] - 1), estado[1]]
        coordenada_abajo = [(estado[0] + 1), estado[1]]
        coordenada_izquierda = [estado[0], (estado[1] - 1)]
        coordenada_derecha = [estado[0], (estado[1] + 1)]
        
        posibles_sucesores = [
            verificar_coordenada(coordenada_abajo),
            verificar_coordenada(coordenada_derecha),
            verificar_coordenada(coordenada_izquierda),
            verificar_coordenada(coordenada_arriba),
        ]
        
        return posibles_sucesores

    def costo_entre_dos(self) -> int:
        return 1

    def distancia_al_objetivo(self, estado: tuple[int, int]) -> float:
        x1 = estado[0]
        x2 = estado[1]
        y1 = self.objetivo[0]
        y2 = self.objetivo[1]

        return math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
