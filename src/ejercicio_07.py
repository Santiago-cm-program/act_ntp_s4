def estudiante_tupla (tupla):
    estudiante_aprovados = []
    for estudiante in tupla:
        nombre,edad,promedio = estudiante
        if promedio > 8.0:
            estudiante_aprovados.append(estudiante)
    
    return tuple(estudiante_aprovados)  
    
tupla_estudiantes = (
    ("Ana", 20, 9.1),
    ("Luis", 22, 7.8),
    ("María", 19, 8.5),
    ("Carlos", 21, 6.9),
    ("Elena", 23, 8.0),
    ("Pedro", 20, 8.2),
)
resultado = estudiante_tupla(tupla_estudiantes)

print(f"Los estudiantes que sacaron mayor calificación son")
print(resultado)