def combinar_listas(lista_1,lista_2):
    lista_nueva = []
    for X ,Y in zip(lista_1,lista_2):
        lista_nueva.append(X)
        lista_nueva.append(Y)
    print(lista_nueva)      
        
lista_1=[1,2,3] 
lista_2=['a','b','c']
combinar_listas(lista_1,lista_2)