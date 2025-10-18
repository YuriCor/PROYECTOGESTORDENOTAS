cursos = []
historial = []
cola_revision = ()

def registrar_curso():
    print("REGISTRAR NUEVO CURSO")

    # Solicitar nota con validaciones
    while True:
        nombre_curso = input("Ingrese el nombre del curso: ")

        if nombre_curso.strip() == "":
            print("Error: El nombre del curso no puede estar vacio. ")
            print("Ingresa el nombre del curso.")
        else:
            break
    
    # solicitar nota
    while True:
        try:
            nota_input = input("Ingrese la nota obtenida: ")

            # validar vacio
            if nota_input.strip() == "":
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
    
    #Guardar curso en lista
    cursos.append({"nombre": nombre_curso, "nota": nota})
    historial.append(f"Se registro el curso '{nombre_curso}' con nota {nota:.2f}")
    
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
#-----------------------------------------------------------------------

def mostrar_curso():
    print("CURSOS REGISTRADOS")
    if not cursos:
        print("No hay cursos registrados.")
    else:
        for i, (curso, nota) in enumerate(cursos, start=1):
            print(f"{i}. {curso} - {nota:.2f}")
    print()
#-------------------------------------------------------------------------------------

def calcular_promedio():
    print("PROMEDIO GENERAL")
    if not cursos:
        print("No hay cursos registrados.")
    else:
        promedio = sum(nota for _, nota in cursos) / len(cursos)
        print(f"El promedio general es: {promedio:.2f}")

#-------------------------------------------------------------------------------------------

def contar_aprobados_reprobados():
    print("CURSOS APROBADOS Y REPROBADOS")
    if not cursos:
        print("No hay cursos registrados.")
    else:
        aprobados = sum(1 for _, nota in cursos if nota >= 61)
        reprobados = len(cursos) - aprobados
        print(f"Cursos aprobados: {aprobados}")
        print(f"Cursos reprobados: {reprobados}")

#---------------------------------------------------------------------------------------------------

def buscar_curso_lineal(nombre):
    print("BUSCAR CURSO")
    for curso, nota in cursos:
        if curso["nombre"].lower() == nombre.lower():
            print(f"Curso encontrado: {curso['nombre']} - Nota: {curso['nota']:.2f}")
            return curso, nota
    print("Curso no encontrado.")
    return None

#-----------------------------------------------------------------------------------------------------------------
def actualizar_nota():
    print("ACTUALIZAR NOTA DE UN CURSO")
    if not cursos:
        print("No hay cursos registrados")
        return

nombre = input("Ingrese el nombre del curso a actualizar: ")
for i, (curso, nota) in enumerate(cursos):
    if curso.lower() == nombre.lower():
        while True:
            try:
                nueva_nota = float(input("Ingrese la nueva nota (0-100): "))
                if nueva_nota < 0 or nueva_nota > 100:
                    print("Error: La nota debe estar entre 0 y 100.")
                    continue
                cursos[i] = (curso, nueva_nota)
                historial.append(f"Se actualizo la nota del curso '{curso}' a {nueva_nota:.2f}")
                print(f"Nota del curso '{curso}' actualizada a {nueva_nota:.2f}.\n")
              
            except ValueError:
                print("Error: Debe ingresar un valor numerico.")
print("Curso no encontrado")

#-----------------------------------------------------------------------------------------------

def eliminar_curso():
    print("ELIMINAR UN CURSO")
    if not cursos:
        print("No hay cursos registrados")
        return
    
    nombre = input("Ingrese el nombre del curso a eliminar")
    for i, (curso, _) in enumerate(cursos):
        if curso.lower() == nombre.lower():
            eliminado = cursos.pop(i)
            print(f"Curso '{eliminado[0]}' eliminado con exito. ")
            return
    print("Curso no encontrado")
          
#-----------------------------------------------------------------------------------------------------

def ordenar_burbuja():
    print("ORDENAR CURSOS POR NOTA (BURBUJA)")
    if not cursos:
        print("No hay cursos registrados.")
        return
    lista = cursos[:]
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lista[j][1] > lista[j + 1][1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
        
    for curso, nota in lista:
        print(f"{curso} - {nota:.2f}")
    print()

#------------------------------------------------------------------------------------
def ordenar_insercion():
    print("ORDENAR CURSOS POR NOMBRE(INSERCION)")
    if not cursos:
        print("No hay cursos registrados")
        return
    
    lista = cursos[:]
    for i in range(1, len (lista)):
        clave = lista [i]
        j = i - 1
        while j >= 0 and lista[j][0].lower() > clave[0].lower():
            lista[j + 1] = lista[j]
            j -= 1
        lista[j+1] = clave
    
    for curso, nota in lista:
        print(f"{curso} - {nota:2f}")
    print()

#----------------------------------------------------------------------------------------------
def buscar_binaria(nombre):
    if not cursos:
        return None
    
    lista = sorted(cursos, key=lambda x: x[0].lower())
    inicio, fin = 0, len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio][0].lower() == nombre.lower():
            return lista[medio]
        elif lista[medio][0].lower() < nombre.lower():
            inicio = medio + 1
        else:
            fin = medio -1
    return None
#-----------------------------------------------------------------------------------------------------------

def simular_cola_revision():
    print("COLA DE SOLICITUDES DE REVISION")
    while True:
        print("1. Agregar solicitud")
        print("2. Atender solicitud")
        print("3. Mostrar cola")
        print("4. volver al menu principal")
        opcion = input("Seleccione una opcion: ")
        
        if opcion == "1":
            nombre = input("Ingrese el curso a revisar: ").strip()
            cola_revision.append(nombre)
            print(f"Solicitud para revisar '{nombre}' agregada.\n")

        elif opcion == "2":
            if cola_revision:
                atendido = cola_revision.popleft()
            else:
                print("No hay solicitudes en la cola.\n")
            
        elif opcion == "3":
            print("Cola de solicitudes:", list(cola_revision), )

        elif opcion == "4":
            break

        else:
            print("opcion invalida.")
#-------------------------------------------------------------------------------------------

def mostrar_historial():
    print("HISTORIAL DE CAMBIOS")
    if not historial:
        print("No hay cambios registrados.")
    else:
        for i, cambio in enumerate(reversed(historial), start=1):
            print(f"{i}, {cambio}")       
        print()


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
        calcular_promedio()
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
        nombre = input("Ingrese el nombre del curso a buscar: ").strip()
        curso = buscar_binaria(nombre)
        if curso:
            print(f"curso encontrado: {curso[0]} - {curso[1]:.2f} \n")
        else:
            print("Curso no encontrado.\n")
    elif opcion == "11":
        simular_cola_revision()
    elif opcion == "12":
        mostrar_historial()
    elif opcion == "13":
        print("Saliendo del sistema.")
        break
    else:
        print("Opcion invalida. Intente de nuevo. \n")




