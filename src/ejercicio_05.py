def encontrar_palabras(lista_palabras,palabra_ingresada):
    palabra_encontrada = []
    for palabra in lista_palabras:
        for caracter in palabra:
            if caracter.lower() == palabra_ingresada.lower():
                palabra_encontrada.append(palabra)
                break
    if palabra_encontrada:
        print("la palabra que contiene el caracter ingresado es:".format(caracter_ingresada))
        print(palabra_encontrada)
         
    if not palabra_encontrada:
        print("Dentro de la lista de palabras no se encuentra una palabra con ese caracter")
    return palabra_encontrada

lista = ["programación", "python", "desarrollo", "inteligencia", "chatbot"]
caracter_ingresada = input("Ingrese la letra a buscar: ")
encontrar_palabras(lista,caracter_ingresada)
