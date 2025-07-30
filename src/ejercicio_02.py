def calificaciones_totales():
    lista = []   
    suma = 0

    while True:
        Entrada = input("Para finalizar el ciclo escriba la palabra 'Fin' Ingrese las calificaciones: ")
        if Entrada.lower() == "fin":
            break
    
        calificaciones = float(Entrada)
        lista.append(calificaciones)
        suma += calificaciones
        mayor = max(lista)
        menor = min(lista)
        promedio = suma / len(lista)
    print(f"La nota promedio es: {promedio}\nLa mayor calificación es: {mayor}\nLa menor calificación es: {menor}")
    

calificaciones_totales()
