# stadistic mean geometric_mean

import statistics as st
import random as rd
import csv

def asignarSueldos(trabajadores):

    sueldos_trabajadores = {}
    for trabajador in trabajadores:
        sueldo = rd.randint(300000, 2500000)
        sueldos_trabajadores[trabajador] = sueldo
    print ("\nNombre trabajador / Sueldos")
    for nombre, sueldo in sueldos_trabajadores.items():
        print(f"{nombre} = $ {sueldo}")
    print()
    return sueldos_trabajadores
def clasificarSueldo(sueldos_trabajadores):
    sueldosMenores = {}
    sueldosMedios  = {}
    sueldosMayores = {}
    sueldoTotal = 0
    for trabajador, sueldo in sueldos_trabajadores.items():
        if sueldo<800000:
            sueldosMenores[trabajador]=sueldo
        elif sueldo<2000000:
            sueldosMedios[trabajador]=sueldo
        else:
            sueldosMayores[trabajador]=sueldo
    print(f"\nSueldos menores a $800.000. Total = {len(sueldosMenores)}")
    for nombre, sueldo in sueldosMenores.items():
        print(f"{nombre} = $ {sueldo}")
    print(f"\nSueldos entre $800.000 y $2.000.000. Total = {len(sueldosMedios)}")
    for nombre, sueldo in sueldosMedios.items():
        print(f"{nombre} = $ {sueldo}")
    print(f"\nSueldos superiores a $2.000.000. Total = {len(sueldosMayores)}")
    for nombre, sueldo in sueldosMayores.items():
        print(f"{nombre} = $ {sueldo}")
    for trabajador, sueldo in sueldos_trabajadores.items():
        sueldoTotal = sueldoTotal + sueldo

    print(f"\nTotal Sueldos: {sueldoTotal}\n")

def estadisticas(sueldos_trabajadores):
    sueldosEstadisticas=list(sueldos_trabajadores.values())
    sueldoBajo = min(sueldosEstadisticas)
    sueldoAlto = max(sueldosEstadisticas)
    sueldoProm = sum(sueldosEstadisticas) / len(sueldosEstadisticas)
    sueldoMedGeo = st.geometric_mean(sueldosEstadisticas)

    print(f"\nEl sueldo más bajo es de: ${sueldoBajo}")
    print(f"El sueldo más alto es de: ${sueldoAlto}")
    print(f"El promedio de sueldos es de: ${sueldoProm}")
    print(f"La media geométrica es de: {sueldoMedGeo}\n")

def reporteSueldos(sueldos_trabajadores):
    sueldoImprimir={}
    #print("Nombre empleado / Sueldo Base / Desc. Salud / Desc. AFP / Sueldo Líquido  ")
    for trabajador, sueldo in sueldos_trabajadores.items():
        sueldoImprimir[trabajador]=[sueldo, (sueldo*0.07), (sueldo*0.12), (sueldo*0.82)]
    #for trabajador, sueldo in sueldoImprimir.items():
        #print(f"{trabajador}    -    {sueldo[0]}    -    {int(sueldo[1])}    -    {int(sueldo[2])}    -    {int(sueldo[3])}")
    
    with open("Reporte_sueldos.csv", "w", newline="") as archivo:
        escritor=csv.writer(archivo)
        escritor.writerow(["Nombre Empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo líquido"])
        for trabajador, sueldo in sueldoImprimir.items():
            escritor.writerow([trabajador, sueldo[0], sueldo[1], sueldo[2], sueldo[3]])
        print("Registro realizado con éxito\n")