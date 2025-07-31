def palabras_conjunto():
    Palabras_unicas = set()
    palabras_repetidas = set()

    while True:
        palabra = input("Para salir, escriba la palabra 'salir'\nIngrese una palabra: ").strip().lower()
        
        if palabra == "salir":
            break
        
        if palabra in Palabras_unicas:
            palabras_repetidas.add(palabra)
        else:
            Palabras_unicas.add(palabra)

    print(f"\nCantidad de palabras únicas: {len(Palabras_unicas)}")
    print(f"Palabras únicas: {Palabras_unicas}")
    print(f"Palabras repetidas: {palabras_repetidas if palabras_repetidas else 'Ninguna'}")


palabras_conjunto()
