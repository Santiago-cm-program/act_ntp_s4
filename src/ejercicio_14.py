def sistema_votacion():
    votos = set()
    
    print("Sitema de Votación\n para finalizar votación escriba 'fin'")
    while True:
        votar = input("Ingrese el nombre del candidato por el cual quiere votar: ").lower()
        if votar == 'fin':
            break
        
        votos.add(votar)
    
    print(f"Los candidatos por los que votaron fueron : {votos}")
    
sistema_votacion()
    