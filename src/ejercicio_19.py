def gestor_calificaciones():
    calificaciones = {}

    while True:
        print("\n--- Menú de Gestión de Calificaciones ---")
        print("1. Agregar estudiante")
        print("2. Agregar calificación")
        print("3. Mostrar promedios")
        print("4. Salir")
        
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            nombre = input("Ingrese el nombre del estudiante: ").strip().lower()
            if nombre in calificaciones:
                print(f"⚠️ El estudiante '{nombre}' ya existe.")
            else:
                calificaciones[nombre] = []  # ✅ lista vacía, no diccionario
                print("✅ Estudiante agregado con éxito.")

        elif opcion == 2:
            nombre = input("Ingrese el nombre del estudiante: ").strip().lower()
            if nombre in calificaciones:
                while True:
                    try:
                        nota = float(input("Ingrese la calificación del estudiante: "))
                        calificaciones[nombre].append(nota)  # ✅ agregar a la lista
                        print("✅ Calificación agregada.")
                    except ValueError:
                        print("❌ Ingrese un número válido.")
                    
                    nota_extra = input("¿Quiere ingresar otra nota? (si/no): ").strip().lower()
                    if nota_extra == 'no':
                        break
            else:
                print("⚠️ El estudiante no está registrado.")

        elif opcion == 3:
            print("\n📊 Promedios:")
            for estudiante, notas in calificaciones.items():
                if notas:
                    promedio = sum(notas) / len(notas)
                    print(f"{estudiante}: {promedio:.2f}")
                else:
                    print(f"{estudiante}: No tiene calificaciones.")

        elif opcion == 4:
            print("👋 Saliendo del sistema de calificaciones.")
            break
        else:
            print("❌ Opción no válida. Intente de nuevo.")

gestor_calificaciones()
