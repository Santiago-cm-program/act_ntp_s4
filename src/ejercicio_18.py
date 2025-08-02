def agenda_telefono():
    numeros_telefono= {}
    
    print("Bienvenido a tu agenda: \n por favor seleccione una opcion\n\n")    
    
    while True:
        opcion = int(input("Opción 1: Agregar numero\n Opción 2 : Actualizar numero \n Opción 3 : buscar por nombre \n Opción 4: Mostrar todos los contactos\n Opción 5: Salir del inventario \n Escriba su opción : "))
    
        if opcion == 1:
           while True:
                    print("\n--- Agregar contacto ---")
                    nombre = input("Nombre del contacto: ").strip().lower()
                    numero = int(input("numero: "))
                    numeros_telefono[nombre] = numero
                    continuar = input("¿Agregar más contactos? (si/no): ").strip().lower()
                    if continuar == 'no':
                        break
            
        elif opcion == 2:
            print("Actualizar contactos")
            contacto_actualizar = input("Ingrese el nombre del contacto que quiere actualizar: ")
            if contacto_actualizar in numeros_telefono:
                numero_actualizar = int(input("Ingrese el nuevo numero: "))
                
                numeros_telefono.update({contacto_actualizar: numero_actualizar})
            else:
                print("El producto no existe en la lista")
        elif opcion == 3:
            print("buscar producto por numero")
            nombre_contacto_name= input("Escriba el nombre del contacto:  ")
            if nombre_contacto_name in numeros_telefono:
               print(f"📞 {nombre_contacto_name} → {numeros_telefono[nombre_contacto_name]}")
            else:
                print(f"⚠️ El contacto '{nombre_contacto_name}' no esta en la lista de telefonos.")
        elif opcion == 4:
            print("\n--- Inventario actual ---")
            if  not numeros_telefono:
                print("⚠️ El directorio está vacío.\n")
            else:
                for nombre, numero in numeros_telefono.items():
                    print(f"📞 {nombre}: {numero}") 
        elif opcion == 5:
            print(f"Saliendo del inventario")
            break
agenda_telefono()