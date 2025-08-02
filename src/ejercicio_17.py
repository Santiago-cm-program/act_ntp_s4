def contar_palabras(frase):
    frecuencia={}
    
    frase = frase.lower()
    palabras= frase.split()
    
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    frecuencia_ordenada = dict(sorted(frecuencia.items(), key=lambda item: item[1], reverse=True))
    
    #Resultado
    for palabra,cantidad in frecuencia_ordenada.items():
        print(f"{palabra}:{cantidad}")
frase = input("Ingrese una frase: ")
contar_palabras(frase)