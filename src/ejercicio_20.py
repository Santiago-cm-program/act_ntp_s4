def registro_temperaturas():
    temperaturas = {}

    dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]

    while True:
        print("\n🌡️ Menú - Registro de Temperaturas por Ciudad")
        print("1. Registrar temperatura")
        print("2. Mostrar temperaturas")
        print("3. Estadísticas por ciudad")
        print("4. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            ciudad = input("Ingrese el nombre de la ciudad: ").strip().lower()
            if ciudad not in temperaturas:
                temperaturas[ciudad] = {}

            for dia in dias_semana:
                try:
                    temp = float(input(f"Ingrese la temperatura del día {dia} para {ciudad.title()}: "))
                    temperaturas[ciudad][dia] = temp
                except ValueError:
                    print("❌ Valor inválido, se omite este día.")

        elif opcion == "2":
            print("\n📋 Temperaturas registradas:")
            if not temperaturas:
                print("⚠️ No hay datos registrados.")
            for ciudad, dias in temperaturas.items():
                print(f"\nCiudad: {ciudad.title()}")
                for dia, temp in dias.items():
                    print(f"  {dia.title()}: {temp}°C")

        elif opcion == "3":
            print("\n📊 Estadísticas por ciudad:")
            for ciudad, dias in temperaturas.items():
                if dias:
                    promedio = sum(dias.values()) / len(dias)
                    print(f"{ciudad.title()} - Promedio semanal: {promedio:.2f}°C")
                else:
                    print(f"{ciudad.title()} - Sin temperaturas registradas.")

        elif opcion == "4":
            print("👋 Saliendo del sistema.")
            break

        else:
            print("❌ Opción inválida. Intente de nuevo.")

# Ejecutar la función
registro_temperaturas()
