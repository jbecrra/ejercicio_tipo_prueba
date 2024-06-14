import os, time
from funciones import*

while True:
    print("MENU DE TRABAJADORES")
    print("1. Registrar trabajador")
    print("2. Liatar todos los trabajadores")
    print("3. Imprimir planilla de sueldos")
    print("4.  salir del programa")
    opc=int(input("ingrese opcion: "))
    os.system('cls')
    if opc==1:
        opc1()
    elif opc==2:
        opcion2()
    elif opc==3:
        opc3()                    
    else:
        opc4()
    time.sleep(3)