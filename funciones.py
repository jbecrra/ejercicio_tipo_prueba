trabajadores=[]
cargos=("ceo","desarrollador","analista")

def opc1():
    print("REGISTRO TRABAJADOR")
    nombre_apellido=input("ingrese su nombre y apellido: ")
    cargo=int(input("ingrese cargo(1:CEO, 2:DESARROLLADOR, 3:ANALISTA): "))
    sueldo_bruto=int(input("ingrese sueldo bruto: "))
    desc_salud=int(7/100*sueldo_bruto)
    desc_afp=int(12/100*sueldo_bruto)
    sueldo_liquido=sueldo_bruto-desc_salud-desc_afp
    trabajador=[nombre_apellido,cargos[cargo-1],sueldo_bruto,desc_salud,desc_afp,sueldo_liquido]
    trabajadores.append(trabajador)
    print("TRABAJADOR AGREGADO CON ÉXITO!")
    
def opcion2():
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

def opc3():
    if len(trabajadores)==0:
        print("NO EXIXTEN TRABAJADORES, ELIJA OPCION 1")
    else:   
        opc2=int(input("que cargo desea imprimir(1:CEO, 2:DESARROLLADOR, 3:ANALISTA,4:TODOS)?: "))
        if opc2==4:
            with open("todos_trabajadores.txt","a", newline="\n")as archivo:
                for t in trabajadores:
                    texto=f"nombre: {t[0]}\ncargo: {t[1]}\nbruto: {t[2]}\ndesc. salud: {t[3]}\ndesc. afp: {t[4]}\nliquido: {t[5]}\n\n"
                    archivo.write(texto)
        else:
            with open("trabajadores_por_cargo.txt","w")as archivo:
                for t in trabajadores:
                    if cargos[opc2-1]==t[1]:
                        texto=f"nombre: {t[0]}\ncargo: {t[1]}\nbruto: {t[2]}\ndesc. salud: {t[3]}\ndesc. afp: {t[4]}\nliquido: {t[5]}\n\n"
                        archivo.write(texto)
        print("archivo creado con éxito")


def opc4():
    print("Gracias por usar el programa, adios")
    exit()

