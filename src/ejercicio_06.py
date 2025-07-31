import random
import math

def coordenadas():
    puntos = []  

    # Generar 10 puntos aleatorios
    for _ in range(10):
        x = random.uniform(-10, 10)
        y = random.uniform(-10, 10)
        puntos.append((x, y))   
    puntos = tuple(puntos)

    print("Puntos generados:")
    for punto in puntos:
        print(punto)

    print("\nPuntos dentro del círculo de radio 5 centrado en el origen:")
    for x, y in puntos:
        distancia = math.sqrt(x**2 + y**2)
        if distancia <= 5:
            print((x, y))

# Ejecutar la función
coordenadas()
