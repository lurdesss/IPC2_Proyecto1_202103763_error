def opcionesMenu():
    print("\n   ------------------ MENÚ ------------------")
    print("   |     1. Cargar archivo                  |")
    print("   |     2. Procesar archivo                |")
    print("   |     3. Escribir archivo salida         |")
    print("   |     4. Mostrar datos del estudiante    |")
    print("   |     5. Generar gráfica                 |")
    print("   |     6. Inicializar sistema             |")
    print("   |     7. Salida                          |")
    print("   ------------------------------------------")

def menu():
    opcion = ""

    while opcion != "7":
        opcionesMenu()
        opcion = input("\nSeleccione una opcion del menú: ")

        if opcion == "1":
            try:
                print("         Cargar archivo                      ")
            except:
                print("   ------------------------------------------")
        elif opcion == "2":
            try:
                print("         Procesar archivo                    ")
            except:
                print("   ------------------------------------------")
        
        elif opcion == "3":
            try:
                print("         Escribir archivo salida             ")
            except:
                print("   ------------------------------------------")
        
        elif opcion == "4":
            try:
                print("         Datos del estudiante                ")
                print("   Jennifer Yulissa Lourdes Taperio Manuel   ")
                print("   202103763                                 ")
                print("   Introducción a la Programación            ")
            except:
                print("   ------------------------------------------")
        elif opcion == "5":
            try:
                print("         Generar gráfica                     ")
            except:
                print("   ------------------------------------------")
        
        elif opcion == "6":
            try:
                print("         Inicializar sistema                 ")
            except:
                print("   ------------------------------------------")
menu()