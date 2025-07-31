import math
def distancia_total(puntos):
    distancia_total_puntos = 0.0
    for i in range(len(puntos)-1):
        x1,y1 = puntos[i]
        x2,y2 = puntos[i+1]
        distancia = math.sqrt((x2-x1)**2+(y2-y1)**2)
        distancia_total_puntos += distancia
        
    return distancia_total_puntos
puntos = (
    (0, 0),
    (3, 4),   
    (6, 8),   
    (9, 12)   
)

resultado = distancia_total(puntos)
print(f"Distancia total {resultado:.2f}")