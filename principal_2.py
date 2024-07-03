import time, os
from deltio import *
while True:
    os.system("cls")
    print("\tMENÚ")
    print("1. Agregar un contacto")
    print("2. Mostrar contactos")
    print("3. Guardar contactos en archivo CSV")
    print("4. Eliminar contacto")
    print("5. Salir")
    while True:
        try:
            opc = int(input("Ingrese una opción: "))
            if opc in (1, 2, 3, 4):
                break
            else:
                print("LAS OPCIONES SOLO SON 1, 2, 3 Y 4")
        except:
            print("Solo deben ser números enteros")
    os.system("cls")
    if opc==1:
        agregar_contactos()
    elif opc==2:
        mostrar_contactos()
    elif opc==3:
        guardar_contactos()
    elif opc==4:
        eliminar_contacto()
    else:
        salir()
    time.sleep(3)