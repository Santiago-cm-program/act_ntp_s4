def Conjuntos():
    conjuntos_pares = set()
    for i in range(1,21):
        i % 2 == 0
        conjuntos_pares.add(i)
    
    conjunto_multiplo_3 =  set()
    for i in range (3,31):
        i % 3 == 0
        conjunto_multiplo_3.add(i)
    
    #Cojuntos 
    print(f"Conjuntos pares {conjuntos_pares}")
    print(f"Conjunto multiplos de 3 {conjunto_multiplo_3}")
    # Operaciones
    print("Operaciones con conjuntos")
    union = conjuntos_pares | conjunto_multiplo_3
    print(f"union { union}")

    interseccion = conjuntos_pares  & conjunto_multiplo_3
    print("Intersección", interseccion)

    diferencia = conjuntos_pares - conjunto_multiplo_3
    print(f"Diferencia {diferencia}")

    diferencia_simetrica = conjuntos_pares ^ conjunto_multiplo_3
    print(f"Diferencia {diferencia_simetrica}")

