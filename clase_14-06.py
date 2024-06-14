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
        if len(trabajadores)==0:
            print("NO EXIXTEN TRABAJADORES, ELIJA OPCION 1")
        else:
            print("LISTA DED TTRABAJDORES")
            print("trabajador\tcargo\tSueldo Bruto\tDesc. Salud\tDesc. AFP ")
            for t in trabajadores:#t: seria cada trabajador de la lista, t es una lista
                print(f"{t[0]}\t{t[1]}\t{t[2]}\t\t{t[3]}\t\t{t[4]}\t\t{t[5]}")
                #for x in range(6):
                    #print(f"{t[x]}\t",end="")
                #print()

    elif opc==3:
        pass
    else:
        print("Gracias por usar el programa, adios")
        break
    time.sleep(3)