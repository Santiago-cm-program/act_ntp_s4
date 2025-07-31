def tupla_fibonacci():
    fibonnacci = []
    a,b=0,1
    contador = 0
    
    while contador < 20:
        fibonnacci.append(a)
        a,b=b,a+b
        contador +=1
        
    tupla_fibonacci = tuple(fibonnacci)
    for numero in tupla_fibonacci:
        if numero % 2 != 0:
            print(numero)
            
tupla_fibonacci()