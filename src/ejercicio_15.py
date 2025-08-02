def numeros_duplicados(lista_numeros):
    conjunto_numeros_unicos = set()
    
    for numero in lista_numeros:
        conjunto_numeros_unicos.add(numero)
        
    original= len(lista_numeros)
    unicos = len(conjunto_numeros_unicos)
    duplicados = original - unicos
    
    print(f"Lista original: {lista_numeros}")
    print(f"Números únicos: {conjunto_numeros_unicos}")
    print(f"Cantidad de elementos originales: {original}")
    print(f"Cantidad de números únicos: {unicos}")
    print(f"Cantidad de duplicados: {duplicados}")
    
numeros = [1, 2, 3, 4, 2, 3, 5, 1, 6, 7, 5]
numeros_duplicados(numeros)