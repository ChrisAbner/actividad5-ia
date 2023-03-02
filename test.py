import cv2
import numpy as np
import numpy.typing as npt

img_matriz_3d = cv2.imread("imgs/hilo1.png", cv2.IMREAD_COLOR)

print(img_matriz_3d.shape)

# print(img)

nueva_matriz_2d = []

for img_matriz_2d in img_matriz_3d:
    nueva_lista = [1 if img_lista.sum() == 0 else 0 for img_lista in img_matriz_2d]
    nueva_matriz_2d.append(nueva_lista)

art_matriz_2d = np.matrix(nueva_matriz_2d, np.int32)

print(art_matriz_2d.shape)
print(art_matriz_2d[0, 0])
print(art_matriz_2d[255, 255])

# print(img[0][6][0])

# print(img[0][5].sum())

# print(img[1])
