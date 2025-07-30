def carrito_compras():
    lista_productos=[]
    opcion = 0
    while True:
        opcion = int(input("""Seleccione la opción que requiera \n Opción 1: Para agregar productos \n Opción 2: Eliminar productos \n Opción 3: Mostrar productos\n Opcion 4: Salir \n Ingrese la opción:"""))
        if opcion == 1:
            productos = input("Ingrese el producto que quiere ingresar a la lista:").lower()
            lista_productos.append(productos)
            print("Producto ingresado con exito")
        elif opcion == 2:
            produto_remove = input("Ingrese el nombre del producto que quiere remover de la lista:").lower()
            if produto_remove  in lista_productos:
                lista_productos.remove(produto_remove)
                print(f"Se elimino {produto_remove} con exito")
            else:
                print(f"El producto no existe en la lista")
        elif opcion == 3:
            print(f"Los productos de la lista son : {lista_productos}")
        elif opcion == 4:
            print("Gracias por su compra")
            break
        
        
#Invocamos la función
carrito_compras()
        
    
    
     