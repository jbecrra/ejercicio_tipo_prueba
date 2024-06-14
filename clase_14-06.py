import os, time
trabajadores=[]
while True:
    print("MENU DE TRABAJADORES")
    print("1. Registrar trabajador")
    print("2. Liatar todos los trabajadores")
    print("3. Imprimir planilla de sueldos")
    print("4.  salir del programa")
    opc=int(input("ingrese opcion: "))
    if opc==1:
        print("REGISTRO TRABAJADOR")
        nombre_apellido=input("ingrese su nombre y apellido: ")
        cargo=int(input("ingrese cargo(1:CEO, 2:DESARROLLADOR, 3:ANALISTA): "))
        sueldo_bruto=int(input("ingrese sueldo bruto: "))
        desc_salud=int(7/100*sueldo_bruto)
        desc_afp=int(12/100*sueldo_bruto)
        sueldo_liquido=sueldo_bruto-desc_salud-desc_afp
        trabajador=[nombre_apellido,cargo,sueldo_bruto,desc_salud,desc_afp,sueldo_liquido]
        trabajadores.append(trabajador)
        print("TRABAJADOR AGREGADO CON ÉXITO!")
    elif opc==2:
        pass
    elif opc==3:
        pass
    else:
        print("Gracias por usar el programa, adios")
        break
    time.sleep(3)