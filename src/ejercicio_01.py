lista_nueva = []
def numeros_pares (lista):
    for i in lista:
        if i % 2 == 0:
            lista_nueva.append(i)
    print(f"Lista con numeros pares {lista_nueva}")
   
lista_inicial= [1,2,3,4,5,6,7,8,9,10] 
numeros_pares(lista_inicial)