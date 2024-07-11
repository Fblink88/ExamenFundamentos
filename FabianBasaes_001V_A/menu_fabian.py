import funciones_fabian as fn
trabajadores = ["Juan Pérez", "María García", "Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez", "Isabel Gómez", "Francisco Díaz","Elena Fernández"]
sueldos_trabajadores = {}
while True:
    try:
        print("\n   Menu sueldos   ")
        print("******************")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")

        opc = int(input("Ingrese opción: "))

        if opc == 1:
            sueldos_trabajadores = fn.asignarSueldos(trabajadores)
        elif opc == 2:
            if not sueldos_trabajadores:
                print("Error: Debe asignar sueldo previamente")
            else:
                fn.clasificarSueldo(sueldos_trabajadores)
        elif opc == 3:
            if not sueldos_trabajadores:
                print("Error: Debe asignar sueldo previamente")
            else:
                fn.estadisticas(sueldos_trabajadores)
        elif opc == 4:
            if not sueldos_trabajadores:
                print("Error: Debe asignar sueldo previamente")
            else:
                fn.reporteSueldos(sueldos_trabajadores)
        elif opc == 5:
            print("\nFinalizando programa \nDesarrollado por Fabián Basaes \nRut 16.813.822-9\n")
            break
        else: 
            print("Ingrese una opción válida")

    except ValueError:
        print("Error: Ingrese una opción válida")
