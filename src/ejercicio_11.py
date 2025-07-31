def conjuntos(lista_01, lista_02):
    conjunto_1= set()
    for elemento in lista_01:
        conjunto_1.add(elemento)
    
    conjunto_2 = set()
    for elemento in lista_02:
        conjunto_2.add(elemento)
    
    union = conjunto_1 | conjunto_2
    interseccion = conjunto_1 & conjunto_2
    diferencia = conjunto_1-conjunto_2
    diferencia_simetrica = conjunto_1 ^ conjunto_2
    
    print(f"Union : {union}")
    print(f"Interseccion : {interseccion}")
    print(f"Diferencia: {diferencia}")
    print(f"Diferencia Simetrica : {diferencia_simetrica}")
    
    
lista_01 = [1,2,3,9,7,4,10]
lista_02 = [1,2,6,10,4,8,5]
conjuntos(lista_01,lista_02)