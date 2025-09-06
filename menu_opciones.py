def registrar_curso():
    print("REGISTRAR NUEVO CURSO")

    # Solicitar nota con validaciones
    while True:
        nombre_curso = input("Ingrese el nombre del curso: ")

        if nombre_curso == "":
            print("Error: El nombre del curso no puede estar vacio. ")
            print("Ingresa el nombre del curso.")
        else:
            break
    
    # solicitar nota
    while True:
        try:
            nota_input = input("Ingrese la nota obtenida: ")

            # validar vacio
            if nota_input == "":
                print("Error: La nota no puede estar vacia. ")
                continue

            # convertir a numero
            nota = float(nota_input)

            # validar rango
            if nota < 0 or nota > 100:
                print("Error: La nota debe estar entre 0 y 100. ")
                continue
            break

        except ValueError:
            print("Error: Debe ingresar un valor numerico. ")

    # confirmacion
    print(f"Curso '{nombre_curso}' con nota {nota:.2f} registrado con exito.")

    return nombre_curso, nota

def main():
    curso, nota = registrar_curso()

    # mostrar resumen del registo
    print("Curso registrado:")
    print(f"Curso: {curso}")
    print(f"Nota: {nota:.2f}")
    print ("Registro exitoso.")
if __name__== "__main__":
    main()
#----------------------------------------------------------------------------
cursos= registrar_curso


def mostrar_cursos():
    if not cursos:
        print("\n No hay cursos registrados. \n")
    else:
        print("\n Cursos registrados:\n")
        for i, curso in enumerate(cursos, 1):
            print(f"{i}. {curso['nombre']} - Nota: {curso['nota']}")
            print()
mostrar_cursos()

while True:
    print("==== GESTOR DE NOTAS ACADEMICAS ====")
    print("1. Registrar nuevo curso")
    print("2. Mostrar todos los cursos y notas")
    print("3. Calcular promedio general")
    print("4. Contar cursos aprobados y reprobados")
    print("5. Buscar curso por nombre (busqueda lineal)")
    print("6. Actualizar nota de un curso")
    print("7. Eliminar un curso")
    print("8. Ordenar cursos por nota (ordenamiento burbuja)")
    print("9. Ordenar cursos por nombre (ordenamiento insercion)")
    print("10. Buscar curso por nombre (busqueda binaria)")
    print("11. Simular cola de solicitudes de revision")
    print("12. Mostrar historial de cambios (pila)")
    print("13. Salir")
    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        registrar_curso()
    elif opcion == "2":
        mostrar_curso()
    elif opcion == "3":
        calcular_promediol()
    elif opcion == "4":
        contar_aprobados_reprobados()
    elif opcion == "5":
        nombre = input("Ingresed el nombre del curso a buscar: ")
        curso = buscar_curso_lineal(nombre)
        print(curso if curso else "Curso no encontrado. \n")
    elif opcion == "6":
        actualizar_nota()
    elif opcion == "7":
        eliminar_curso()
    elif opcion == "8":
        ordenar_burbuja()
    elif opcion == "9":
        ordenar_insercion()
    elif opcion == "10":
        nombre = input("Ingrese el nombre del curso a buscar: ")
        curso = buscar_binaria(nombre)
        print(curso if curso else "Curso no encontrado. \n")
    elif opcion == "11":
        simular_cola_revision()
    elif opcion == "12":
        mostrar_historial()
    elif opcion == "13":
        print("Saliendo del sistema.")
        break
    else:
        print("Opcion invalida. Intente de nuevo. \n")




