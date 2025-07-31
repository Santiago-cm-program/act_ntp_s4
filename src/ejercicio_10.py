def  suma_tuplas(tupla_01,tupla_02):
    if len(tupla_01)!= len(tupla_02):
        print(f"La tupla tiene que tener la misma longitud")
        
    resultado = []
    for i in range(len(tupla_01)):
        suma = tupla_01[i]+ tupla_02[i]
        resultado.append(suma)
    print(f"La suma de las tuplas es {resultado}")
    return tuple (resultado)

t1 = (1, 2, 3)
t2 = (4, 5, 6)

resultado= suma_tuplas(t1,t2)