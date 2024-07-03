import csv
personas = []
def agregar_contactos():
    print("\tAGREGAR CONTACTO")
    while True:
        try:
            nombre = input("Ingrese nombre: ")
            if len(nombre)>=3 and nombre.isalpha:
                break
            else:
                print("El nombre debe tener mas de 3 letras")
        except:
            print("Solo se deben ingresar letras")
    while True:
        try:
            num = int(input("Ingrese número sin identificador: "))
            if len(str(num))==9 and str(num)[0]=="9":
                break
            else:
                print("""El número debe comenzar con 9.
                    El número debe contener exactamente 9 dígitos""")
        except:
            print("Deben ser solo numeros enteros")
    while True:
            correo = input("Ingrese correo: ")
            if correo.endswith("@gmail.com") and correo.isalpha:
                break
            else:
                print("El correo solo debe tener letras y además terminar en '@gmail.com")

    contacto = {"nombre":nombre,
                "numero":num,
                "correo":correo,}
    personas.append(contacto)
    print("CONTACTO REGISTRADO CON EXITO!")
    
def mostrar_contactos():
    print("\tMOSTRAR CONTACTOS")
    if not personas:
        print("NO EXISTEN CONTACTOS REGISTRADOS")
    else:
        print("\tLISTA DE CONTACTOS")
        for per in personas:
            print("NOMBRE:", per["nombre"])
            print("NÚMERO:", per["numero"])
            print("CORREO:", per["correo"])
            print()


def guardar_contactos():
    if not personas:
        print("\tGUARDAR CONTACTOS")
        print("NO EXISTEN CONTACTOS REGISTRADOS")
    else:
        nombre_archivo = input("Ingrese nombre para el archivo (SIN NINGUNA EXTENSIÓN): ")
        with open (nombre_archivo+".csv","w") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(personas)
            print("EL ARCHVO SE HA CRADO CON EXITO")

def eliminar_contacto():
    if not personas:
        print("NO EXISTEN CONTACTOS REGISTRADOS")
    else:
        print("\tELIMINAR CONTACTO.")
        nombre_eliminar = input("Ingrese el nombre del contacto que desea eliminar: ")
        for per in personas:
            if nombre_eliminar.lower==per["nombre"].lower():
                personas.remove(per)
                print("CONTACTO ELIMNADO CON ÉXITO")
                return


def salir():
    print("Saliendo del sistema...")
    exit()

